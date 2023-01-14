with open('day1_input.txt') as input_file:
    contents = input_file.readlines()

sum_list = []
total = 0
for line in contents:
    line = line.strip()
    if line != '':
        total += int(line)
    else:
        print('Met a new line')
        print(f"current total is {total} calories")
        sum_list.append(total)
        total = 0

top1 = max(sum_list)
sum_list.remove(top1)
top2 = max(sum_list)
sum_list.remove(top2)
top3 = max(sum_list)

print(top1 + top2 + top3)
