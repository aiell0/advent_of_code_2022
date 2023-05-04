import re

# PART ONE
stack_dict = {}
with open("input.txt", "r") as file:
    lines = file.readlines()
    stripped_lines = [i.rstrip("\n") for i in lines]
    # find empty row
    empty_row = stripped_lines.index("")

    for row in range(empty_row - 1, -1, -1):
        # only for first line, build dictionary
        if row == (empty_row - 1):
            stack_dict = {i: [] for i in stripped_lines[row] if i != " "}
        # else build stacks in dictionary
        else:
            split_row = stripped_lines[row].split(' ')
            for i, c in enumerate(split_row):
                if c == '':
                    del split_row[i:i+3]

            for i, crate in enumerate(split_row):
                search_crate = re.search(r'[[A-Z](?=])', crate)
                if search_crate:
                    stack_dict[str(i+1)].append(search_crate.group())

    for row in range(empty_row+1, len(stripped_lines)):
        split_row = stripped_lines[row].split(" ")
        move: str = str(split_row[1])
        fr: str = str(split_row[3])
        to: str = str(split_row[5])

        for i in range(int(move)):
            stack_dict[to].append(stack_dict[fr].pop())

    print("answer: ", [stack_dict[key][len(stack_dict[key])-1] for key in stack_dict.keys()])
