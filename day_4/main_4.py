# constants
summary = 0
filename = "input.txt"
j = 0
# Functions


def prep_data(strin):
    global j
    ranges = []
    temp = strin.strip().split(",")
    for i in temp:
        temp1 = i.split("-")
        # print(temp1)
        rng = [int(temp1[0]), int(temp1[1])]
        # print(rng)
        ranges.append(rng)
    x = ranges[0]
    y = ranges[1]

    print(ranges)

    if x[0] in range(y[0], y[1]+1) or x[1] in range(y[0], y[1]+1):
        print("yes")
        j += 1
    elif y[0] in range(x[0], x[1]+1) or y[1] in range(x[0], x[1]+1):
        print("yes")
        j += 1

    ranges = []


# Main
if __name__ == "__main__":
    with open(filename) as file:
        for line in file:
            # print("hello")
            prep_data(line)
    print("Start")
    print(j)
