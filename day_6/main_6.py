# constants
filename = "input.txt"


# Functions
def prep_data():
    global filename
    with open(filename) as file:
        for line in file:
            print(line)


def check(in_txt):
    print(in_txt)

    for i in range(len(input_txt)):
        iter = 0
        txt = input_txt[i:(i+4)]
        for j in txt:
            if txt.count(j) > 1:
                # print("more than two")
                pass
            elif txt.count(j) == 1:
                # print("one")
                iter += 1
        if iter == 4:
            print("nothing repeats")
            print(input_txt[i:(i + 4)])
            print(input_txt.find(input_txt[i:(i + 4)]) + 4)
            return True
        else:
            iter = 0


def check_14(in_txt):
    print(in_txt)

    for i in range(len(input_txt)):
        iter = 0
        txt = input_txt[i:(i+14)]
        for j in txt:
            if txt.count(j) > 1:
                # print("more than two")
                pass
            elif txt.count(j) == 1:
                # print("one")
                iter += 1
        if iter == 14:
            print("nothing repeats")
            print(input_txt[i:(i + 14)])
            print(input_txt.find(input_txt[i:(i + 14)]) + 14)
            return True
        else:
            iter = 0


def part_1():
    input_txt = ""
    with open(filename) as file:
        for line in file:
            input_txt += line
            print(line)

            if check(input_txt):
                print("found")
            input_txt = ""


# Main
if __name__ == "__main__":
    input_txt = ""
    with open(filename) as file:
        for line in file:
            input_txt += line
            print(line)

            if check_14(input_txt):
                print("found")
            input_txt = ""