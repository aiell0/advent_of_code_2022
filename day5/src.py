import re
import copy

part_one_dict = {}

with open("input.txt", "r") as file:
    lines = file.readlines()
    stripped_lines = [i.rstrip("\n") for i in lines]
    # find empty row
    empty_row = stripped_lines.index("")

    for row in range(empty_row - 1, -1, -1):
        # only for first line, build dictionary
        if row == (empty_row - 1):
            part_one_dict = {i: [] for i in stripped_lines[row] if i != " "}
        # else build stacks in dictionary
        else:
            split_row = stripped_lines[row].split(' ')
            for i, c in enumerate(split_row):
                if c == '':
                    del split_row[i:i+3]

            for i, crate in enumerate(split_row):
                search_crate = re.search(r'[[A-Z](?=])', crate)
                if search_crate:
                    part_one_dict[str(i+1)].append(search_crate.group())

    part_two_dict: dict = copy.deepcopy(part_one_dict)

    for row in range(empty_row+1, len(stripped_lines)):
        split_row = stripped_lines[row].split(" ")
        move: str = str(split_row[1])
        fr: str = str(split_row[3])
        to: str = str(split_row[5])

        # PART ONE
        for i in range(int(move)):
            part_one_dict[to].append(part_one_dict[fr].pop())

        # PART TWO
        part_two_dict[to].extend(part_two_dict[fr][-int(move):])
        del part_two_dict[fr][-int(move):]

    print("Part One Answer: ", [part_one_dict[key][len(part_one_dict[key])-1] for key in part_one_dict.keys()])
    print("Part Two Answer: ", [part_two_dict[key][len(part_two_dict[key])-1] for key in part_two_dict.keys()])

