# helper
def is_one_range_fully_contain_other(range1: range, range2: range):
    """
    range1 has smaller size than range2
    :param range1:
    :param range2:
    :return:
    """
    return range1.start in range2 and range1[-1] in range2


def is_overlap(range1: range, range2: range):
    return range1.start in range2 or range1[-1] in range2


def solution():
    with open('day4_input.txt') as input_file:
        lines = input_file.readlines()

    cnt = 0
    overlap_cnt = 0
    for line in lines:
        assign1, assign2 = line.strip().split(',')
        assign1_start, assign1_end = assign1.split('-')
        assign2_start, assign2_end = assign2.split('-')

        assign1_range = range(int(assign1_start), int(assign1_end) + 1)
        assign2_range = range(int(assign2_start), int(assign2_end) + 1)

        if len(assign1_range) >= len(assign2_range):
            if is_one_range_fully_contain_other(assign2_range, assign1_range):
                cnt += 1
            if is_overlap(assign2_range, assign1_range):
                overlap_cnt += 1
        else:
            if is_one_range_fully_contain_other(assign1_range, assign2_range):
                cnt += 1
            if is_overlap(assign1_range, assign2_range):
                overlap_cnt += 1

    print(f"{cnt=}")
    print(f"{overlap_cnt=}")


if __name__ == '__main__':
    solution()