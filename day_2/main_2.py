""" Constants """

outcome = {
    "A": 1,
    "X": 1,
    "Y": 2,
    "B": 2,
    "C": 3,
    "Z": 3
}

lose = 0
draw = 3
win = 6

filename = "input.txt"
finalScore = 0


# Functions
def compare_part_1(xloc, yloc):
    global finalScore
    opponent = outcome[xloc]
    me = outcome[yloc]
    # print(f"We have opponents {opponent} and mine {me}")

    if opponent == me:
        # print(draw + me)
        finalScore += draw + me
    elif opponent < me:
        if opponent == 1 and me == 3:
            finalScore += me + lose
            # print(me)
        else:
            finalScore += me + win
            # print(me + win)
    elif opponent > me:
        if opponent == 3 and me == 1:
            finalScore += me + win
            # print(me + win)
        else:
            finalScore += me + lose
            # print(me + lose)


def compare_part_2(xloc, yloc):
    global finalScore
    opponent = outcome[xloc]
    me = outcome[yloc]

    if me == 1:
        print("Lose")
        if opponent > 1:
            finalScore += lose + opponent - 1
        else:
            finalScore += lose + 3
    elif me == 2:
        finalScore += draw + opponent
        print("Draw")
    elif me == 3:
        if opponent < 3:
            finalScore += win + opponent + 1
        else:
            finalScore += win + 1
        print("Win")


# Main
with open(filename) as file:
    for line in file:
        x, y = line.strip().split()
        # print(f"{x} and {y}")
        compare_part_2(x,y)



print(finalScore)
