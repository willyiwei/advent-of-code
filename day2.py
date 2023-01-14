choices = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

score_for_shapes = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}


def who_wins(opponent: str, myself: str):
    """

    :param opponent:
    :param myself:
    :return: 0 if you lost, 3 if the round was a draw, and 6 if you won
    """
    if opponent == myself:
        return 3

    if opponent == 'rock':
        return 6 if myself == 'paper' else 0

    if opponent == 'paper':
        return 6 if myself == 'scissors' else 0

    if opponent == 'scissors':
        return 6 if myself == 'rock' else 0


letter_to_results = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}


def what_to_do(opponent: str, expectation: str):
    if expectation == 'draw':
        return opponent

    if opponent == 'rock':
        return 'paper' if expectation == 'win' else 'scissors'
    if opponent == 'paper':
        return 'scissors' if expectation == 'win' else 'rock'
    if opponent == 'scissors':
        return 'rock' if expectation == 'win' else 'paper'


with open('day2_input.txt') as input_file:
    contents = input_file.readlines()

# score = 0
# for line in contents:
#     you, me = line.strip().split(' ')
#     score += score_for_shapes[choices[me]]
#     score += who_wins(choices[you], choices[me])

# print(f"{score=}")

score = 0  # reset
score_card = {
    'X': 0,  # lose
    'Y': 3,  # draw
    'Z': 6,  # win
}
for line in contents:
    you, result_letter = line.strip().split(' ')
    score += score_card[result_letter]
    my_turn = what_to_do(choices[you], letter_to_results[result_letter])
    score += score_for_shapes[my_turn]

print(f"{score=}")
