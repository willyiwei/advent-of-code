"""
[P]     [C]         [M]            
[D]     [P] [B]     [V] [S]        
[Q] [V] [R] [V]     [G] [B]        
[R] [W] [G] [J]     [T] [M]     [V]
[V] [Q] [Q] [F] [C] [N] [V]     [W]
[B] [Z] [Z] [H] [L] [P] [L] [J] [N]
[H] [D] [L] [D] [W] [R] [R] [P] [C]
[F] [L] [H] [R] [Z] [J] [J] [D] [D]
 1   2   3   4   5   6   7   8   9 
"""
# first in last out (FILO)
from collections import deque

stacks = {}
for i in range(1, 10):
    stacks[i] = deque()

for counter, letters in enumerate(
        ['fhbvrqdp', 'ldzqwv', 'hlzqgrpc', 'rdhfjvb', 'zwlc', 'jrpntgvm', 'jrlvmbs', 'dpj', 'dcnwv']):
    for letter in letters:
        stacks[counter + 1].append(letter)

# for i in range(1, 10):
#     print(stacks[i])


def crate_move_9000(from_stack: int, to_stack: int, qty: int):
    """
    move N (by quantity) crates from 'from_stack' to 'to_stack'
    :param from_stack:
    :param to_stack:
    :param qty:
    :return:
    """
    for cnt in range(qty):
        stacks[to_stack].append(stacks[from_stack].pop())


def crate_move_9001(from_stack: int, to_stack: int, qty: int):
    temp_stack = []
    for cnt in range(qty):
        print(f"{cnt=}")
        temp_stack.append(stacks[from_stack].pop())
        print(f"{temp_stack=}")

    temp_stack.reverse()
    for item in temp_stack:
        stacks[to_stack].append(item)


with open('day5_input.txt') as input_file:
    lines = input_file.readlines()

for line in lines:
    results = line.strip().split(' ')
    # crate_move_9000(int(results[3]), int(results[-1]), int(results[1]))
    crate_move_9001(int(results[3]), int(results[-1]), int(results[1]))

for i in range(9):
    print(stacks[i+1][-1].capitalize(), end='')