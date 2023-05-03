num_arr = [i for i in range(100)]

# PART ONE
result = 0
with open("input.txt", "r") as file:
    for line in file:
        pair = line.strip().split(',')
        first_elf_assignment = pair[0]
        second_elf_assignment = pair[1]

        first_elf_assignment_begin = int(first_elf_assignment.split('-')[0])
        first_elf_assignment_end = int(first_elf_assignment.split('-')[1])
        first_elf_assignment_range = set(num_arr[first_elf_assignment_begin:first_elf_assignment_end + 1])

        second_elf_assignment_begin = int(second_elf_assignment.split('-')[0])
        second_elf_assignment_end = int(second_elf_assignment.split('-')[1])
        second_elf_assignment_range = set(num_arr[second_elf_assignment_begin:second_elf_assignment_end + 1])

        if (first_elf_assignment_range.issubset(second_elf_assignment_range)) or (second_elf_assignment_range.issubset(first_elf_assignment_range)):
            result += 1

print("Pairs: ", result)

# PART TWO
result = 0
with open("input.txt", "r") as file:
    for line in file:
        pair = line.strip().split(',')
        first_elf_assignment = pair[0]
        second_elf_assignment = pair[1]

        first_elf_assignment_begin = int(first_elf_assignment.split('-')[0])
        first_elf_assignment_end = int(first_elf_assignment.split('-')[1])
        first_elf_assignment_range = set(num_arr[first_elf_assignment_begin:first_elf_assignment_end + 1])

        second_elf_assignment_begin = int(second_elf_assignment.split('-')[0])
        second_elf_assignment_end = int(second_elf_assignment.split('-')[1])
        second_elf_assignment_range = set(num_arr[second_elf_assignment_begin:second_elf_assignment_end + 1])

        for num in first_elf_assignment_range:
            if num in second_elf_assignment_range:
                result += 1
                break

print("Pairs: ", result)
