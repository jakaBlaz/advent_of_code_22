# constants
summary = 0
filename = "input.txt"

# Functions
def prep_data():
    global filename
    instruction_set = []
    stack = ""
    row = []
    row_row = []
    with open(filename) as file:
        for line in file:
            if line.find("move") != -1:
                # print(line.strip())
                instruction_set.append(line.strip())
            elif line != "\n":
                stack += line
    # print(instruction_set)
    # print(stack)

    stack = stack.split("\n")
    num_of_row = stack[-2]
    num_rows = num_of_row.split()
    for i in range(1, len(num_rows) + 1):
        row.append(num_of_row.find(str(i)))
    # print(row)

    for i in row:
        # print("On position: ")
        # print(i)
        temp = []
        for j in stack[:-1]:
            if i <= len(j):
                # print(j[i])
                if j[i] == " ":
                    pass
                else:
                    temp.append(j[i])
        temp.pop()
        row_row.append(temp)
    # print(row_row)
    return row_row, instruction_set


def parse_instructions(instructions):
    instruction = []
    for i in instructions:
        move = i[(i.find("move")+len("move")):(i.find("from")-1)].strip()
        from_ = i[(i.find("from")+len("from")):(i.find("to")-1)].strip()
        to = i[(i.find("to")+len("to")):].strip()
        # print(f"We have move: {move} and from: {from_} and to: {to} ")
        instruction.append([move, from_, to])
    # print(instruction)
    return instruction


def move_crate(position, move_instruction):
    [move, from_, to] = move_instruction
    temp = position[(int(to)-1)][::-1]
    for j in position[int(from_)-1][:int(move)]:
        temp.append(j)
    position[(int(to) - 1)] = temp[::-1]
    position[int(from_)-1] = position[int(from_)-1][int(move):]

    # print(position)
    return position


def move_crate_whole(position, move_instruction):
    [move, from_, to] = move_instruction
    temp = position[(int(to)-1)][::-1]
    for j in position[int(from_)-1][:int(move)][::-1]:
        temp.append(j)
    position[(int(to) - 1)] = temp[::-1]
    position[int(from_)-1] = position[int(from_)-1][int(move):]

    # print(position)
    return position


def Extract(lst):
    return [item[0] for item in lst]


def part_1():
    x, y = prep_data()  # crates in rows, instructions
    print(x)
    print(y)
    instruct = parse_instructions(y)
    for i in instruct:
        x = move_crate(x, i)
    print(Extract(x))


# Main
if __name__ == "__main__":
    x, y = prep_data()  # crates in rows, instructions
    print(x)
    print(y)
    instruct = parse_instructions(y)
    for i in instruct:
        x = move_crate_whole(x, i)
    print(Extract(x))

