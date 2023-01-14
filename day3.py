import string


# helper methods
def get_priority(letter: str) -> int:
    """
    Give a letter 'a-z' 'A-Z', return the priority in integer
    1-26, 27-52
    :param letter:
    :return:
    """
    if letter in string.ascii_letters:
        return string.ascii_letters.index(letter) + 1


def intersect_of_lists(list1, list2, list3):
    # convert list into set.
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)

    intersect = set1.intersection(set2)
    result = intersect.intersection(set3)

    return list(result)


# testing using examples
def test1():
    with open('day3_example.txt') as example_file:
        example_lines = example_file.readlines()

    for line in example_lines:
        line_length = len(line.strip())
        if line_length % 2 != 0:
            print('Inputs are wrong. Line characters are not even number!')
        mid = int(line_length / 2)
        # 1 2 3 4
        # 1 2 3
        first_compartment, second_compartment = line[:mid], line[mid:]

        # find the common elements
        first_compartment_set = set(first_compartment)
        second_compartment_set = set(second_compartment)

        print(first_compartment_set & second_compartment_set)


def test2():
    with open('day3_example.txt') as example_file:
        example_lines = example_file.readlines()

    priority_sum = 0
    while len(example_lines) > 0:
        line1 = example_lines[0].strip()
        line2 = example_lines[1].strip()
        line3 = example_lines[2].strip()
        lst = intersect_of_lists(line1, line2, line3)
        print(lst)

        if len(lst) == 1:
            priority_sum += get_priority(lst[0])

        del example_lines[:3]

    print(priority_sum)


def solution1():
    with open('day3_input.txt') as input_file:
        lines = input_file.readlines()

    sum_priority = 0
    for line in lines:
        line_length = len(line.strip())
        if line_length % 2 != 0:
            print('Inputs are wrong. Line characters are not even number!')
        mid = int(line_length / 2)
        first_compartment, second_compartment = line[:mid], line[mid:]

        # find the common elements
        first_compartment_set = set(first_compartment)
        second_compartment_set = set(second_compartment)

        common_set = first_compartment_set & second_compartment_set

        if len(common_set) == 1:
            common_letter = list(common_set)[0]
            print(f"{common_letter=}")
            sum_priority += get_priority(common_letter)

    print(sum_priority)
    return None


def solution2():
    with open('day3_input.txt') as input_file:
        lines = input_file.readlines()

    priority_sum = 0
    while len(lines) > 0:
        line1 = lines[0].strip()
        line2 = lines[1].strip()
        line3 = lines[2].strip()
        lst = intersect_of_lists(line1, line2, line3)
        print(lst)

        if len(lst) == 1:
            priority_sum += get_priority(lst[0])

        del lines[:3]

    print(priority_sum)
    return None


if __name__ == '__main__':
    # solution1()
    # test2()
    solution2()
