# Constants
filename = "input.txt"
calories_per_elf = [0]
i = 0

with open(filename) as file:
    for line in file:
        elf_data = line.strip()
        if line != "\n":
            calories_per_elf[i] = calories_per_elf[i] + (int(elf_data))
        else:
            calories_per_elf.append(0)
            i += 1

print("Part 1 of day 1:")
max_calories = max(calories_per_elf)
print(max_calories)

print("Part 2 of day 1:")
calories_per_elf.sort()
part2 = calories_per_elf
sum(part2[-3:])
print(sum(part2[-3:]))

