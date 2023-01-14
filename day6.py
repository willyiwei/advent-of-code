"""
Basic idea: fast pointer, slow pointer
"""
examples = [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',
    'bvwbjplbgvbhsrlpgdmjqwftvncz',
    'nppdvjthqldpwncqszvftbrmjlhg',
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw',
]


def start_packet_marker_detector(data: str):
    for slow_pointer in range(len(data)):
        temp_store = []
        for fast_pointer in range(slow_pointer, slow_pointer + 4):
            if data[fast_pointer] in temp_store:
                break
            temp_store.append(data[fast_pointer])
            # print(f"{temp_store=}")

        if len(temp_store) == 4:
            return fast_pointer + 1


def start_msg_marker_detector(data: str):
    for slow_pointer in range(len(data)):
        temp_store = []
        for fast_pointer in range(slow_pointer, slow_pointer + 14):
            if data[fast_pointer] in temp_store:
                break
            temp_store.append(data[fast_pointer])
            # print(f"{temp_store=}")

        if len(temp_store) == 14:
            return fast_pointer + 1


for example in examples:
    print(start_msg_marker_detector(example))

with open('day6_input.txt') as input_file:
    data_stream = input_file.read()

print(start_msg_marker_detector(data_stream))
