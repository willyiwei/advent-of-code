from collections import defaultdict

with open('day7_input.txt') as f:
    cmds = f.read().splitlines()

sizes = defaultdict(int)
stack = []

for c in cmds:
    if c.startswith('$ ls') or c.startswith('dir'):
        continue
    elif c.startswith('$ cd'):
        cd_dst = c.split()[2]  # dir name is always the third element
        if cd_dst == '..':
            stack.pop()
        else:
            stack.push()
    else:
        size, filename = c.split()
        for path in stack:
            sizes[path] += int(size)
