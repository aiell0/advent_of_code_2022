import string

alphabet_array = list(string.ascii_lowercase) + list(string.ascii_uppercase)

# PART ONE
priority_sum: int = 0
with open("input.txt", "r") as file:
    for line in file:
        half = len(line) // 2
        first_compartment = line[:half]
        second_compartment = line[half:]
        common_items = [v for v in first_compartment if v in second_compartment]
        for letter in set(common_items):
            priority_sum += alphabet_array.index(letter) + 1

print("Priority Sum: ", priority_sum)

# PART TWO
priority_sum: int = 0
with open("input.txt", "r") as file:
    while True:
        line1 = file.readline().strip()
        line2 = file.readline().strip()
        line3 = file.readline().strip()
        if not line1 or not line2 or not line3:
            break
        common_items_first_two = [v for v in line1 if v in line2]
        common_items_all = [v for v in set(common_items_first_two) if v in line3]
        priority_sum += alphabet_array.index(common_items_all[0]) + 1

print("Priority Sum: ", priority_sum)
