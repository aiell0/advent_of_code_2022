elf = 1
elf_calories = {elf: 0}

with open("input.txt", "r") as file:
    for line in file:
        if line.strip() == "":
            elf += 1
            elf_calories[elf] = 0
        else:
            elf_calories[elf] += int(line)

sorted_elf_calories = sorted(elf_calories.items(), key=lambda item: item[1], reverse=True)
print("Calories carried by top elf: ", sorted_elf_calories[0][1])
print("Calories counted by top 3 elves: ", sorted_elf_calories[0][1] + sorted_elf_calories[1][1] + sorted_elf_calories[2][1])

