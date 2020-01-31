import time

sides = []
# get user input
def find_triples():
    side_one = int(input("Enter the length of the first side: "))
    sides.append(side_one)
    side_two = int(input("Enter the length of the second side: "))
    sides.append(side_two)
    side_three = int(input("Enter the length of the third side: "))
    sides.append(side_three)
    sides.sort()
    find_right_triangle()

def find_right_triangle():
    side_one_sq = sides[0] * sides[0]
    side_two_sq = sides[1] * sides[1]
    pythagoras_side = sides[2] * sides[2]
    if side_one_sq + side_two_sq == pythagoras_side:
        print("That's a right triangle!")
    else:
        print("That's not a right triangle.")
    re_do()

# start program over again
def re_do():
    print("Thanks for trying! To test another triangle type 'yes': ")
    user_reply = input()
    if user_reply == 'yes'.lower():
        find_triples()

print("Welcome to the right triangle tester, find out if your triangle is a right triangle.\n")
time.sleep(1)
find_triples()