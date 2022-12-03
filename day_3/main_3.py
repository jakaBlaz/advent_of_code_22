# constants
summary = 0
filename = "input.txt"
x = []
# Functions


def have_same_characters(str1, str2):
    for char in str1:
        if char in str2:
            return char

def have_same_character(str1, str2,str3):
    for char in str1:
        if char in str2:
            if char in str3:
                return char

def part_1():
    with open(filename) as file:
        for line in file:
            x = line.strip()[:len(line.strip())//2]
            y = line.strip()[len(line.strip()) // 2:]
            duplicate = have_same_characters(x, y)
            if 64 < ord(duplicate) < 91:
                duplicate = ord(duplicate) - 64 + 26
            elif 96 < ord(duplicate) < 123:
                duplicate = ord(duplicate) - 96
            print(duplicate)
            summary += duplicate
    print(summary)


# Main
if __name__ == "__main__":
    with open(filename) as file:
        for line in file:
            x.append(line)
            if len(x) == 3:
                print(have_same_character(x[0], x[1], x[2]))
                duplicate = have_same_character(x[0], x[1], x[2])
                if 64 < ord(duplicate) < 91:
                    duplicate = ord(duplicate) - 64 + 26
                elif 96 < ord(duplicate) < 123:
                    duplicate = ord(duplicate) - 96
                print(duplicate)
                summary += duplicate
                x = []
    print(summary)

    '''
        for i in range(3):
            x.append((file.readline().strip()))
        print(have_same_character(x[0], x[1], x[2]))
        x = []'''