# Consider the following puzzle: “On one side of a river are three humans, one big
# monkey, two small monkeys, and one boat. Each of the humans and the big monkey are
# strong enough to row the boat. The boat can fit one or two bodies (regardless of size). If at
# any time at either side of the river the monkeys outnumber the humans, the monkeys will
# eat the humans. How do you get everyone on the other side of the river alive?” Show that
# the language of solutions to the puzzle is regular. Write a finite automaton for the puzzle
# to a file (perhaps using a script if you need it). Using the previously written program find
# and print a solution to the puzzle. The printing should be done to be “understandable by
# humans”2


import tkinter as tk
from tkinter import *

NFA_Check = 0
GRAM_Check = 0
SOL_Check = 0

# Main loop
window = tk.Tk()
window.title(string="FLAT project 8")
# Options
options = ["Problem Solution", "Grammar Display", "NFA Display"]
# For DropDown
clicked = StringVar()
clicked.set(options[0])
# Canvas
canvas = tk.Canvas(window, width=1920, height=1080)

# TopLabel
WelcomeLabel = tk.Label(window, text="Welcome to the project. For it, we had to solve the following puzzle:\n\n")
ProblemLabel = tk.Label(window,
text="On one side of a river are three humans, one big monkey, two small monkeys, and one boat. Each of the humans and the big monkey arestrong enough to row the boat. The boat can fit one or two bodies (regardless of size). If at any time at either side of the river the monkeys outnumber the humans, the monkeys will eat the humans.\n\nHow do you get everyone on the other side of the river alive?\n")
WelcomeLabel.grid(row=0, column=0, sticky=W)
ProblemLabel.grid(row=1, column=0, sticky=W)
# DropDown
drop = OptionMenu(window, clicked, *options)
drop.grid(columnspan=5)
# Button
button = tk.Button(window, text="Display")
button.grid()
# Images
NFA_image = PhotoImage(file="FLAT Project\Grammar\Proper_NFA.png")
GRAM_image = PhotoImage(file="FLAT Project\Grammar\Grammar.png")
SOL_image = PhotoImage(file="FLAT Project\Drawing_States\All_States_Long.png")
# MainLabels
NFA_label = tk.Label(window, image=NFA_image)
NFA_text = tk.Label(window,
                    text="This is the NFA automata created in order to solve the problem. We have the following: \n\n Let a & b belong to Vt\n ab | a & b are on the boat\n aa | a is on the second island\n bbb | b returns to the first island\n Also has newlines and spaces accordingly ( '\ n' ,'  ')\n The program will display the process of travel of the NFA in the console.")
GRAM_label = tk.Label(window, image=GRAM_image)
GRAM_text = tk.Label(window, text="This is the grammar of the problem made for the NFA. It uses simple type-3 rules.")
SOL_label = tk.Label(window, image=SOL_image)
SOL_text = tk.Label(window, text="The solution requires procedural trasnition - step by step as presented from left to right in the images. Represents a stack & queue problem.")

NFA_label.grid()
NFA_text.grid()
GRAM_label.grid()
GRAM_text.grid()
SOL_label.grid()
SOL_text.grid()


# FunctionOfDisplay

def NFA(Check):
    if (Check == 1):
        NFA_label.grid()
        NFA_text.grid()
    else:
        NFA_label.grid_remove()
        NFA_text.grid_remove()


def Grammar(Check):
    if (Check == 1):
        GRAM_label.grid()
        GRAM_text.grid()
    else:
        GRAM_label.grid_remove()
        GRAM_text.grid_remove()


def Solution(Check):
    if (Check == 1):
        SOL_label.grid()
        SOL_text.grid()
    else:
        SOL_label.grid_remove()
        SOL_text.grid_remove()


def DropDownFunction(event):
    the_option = clicked.get()
    if (the_option == options[0]):
        GRAM_Check = 0
        NFA_Check = 0
        SOL_Check = 1
        NFA(NFA_Check)
        Grammar(GRAM_Check)
        Solution(SOL_Check)
    elif (the_option == options[1]):
        GRAM_Check = 1
        NFA_Check = 0
        SOL_Check = 0
        NFA(NFA_Check)
        Grammar(GRAM_Check)
        Solution(SOL_Check)
    else:
        GRAM_Check = 0
        NFA_Check = 1
        SOL_Check = 0
        NFA(NFA_Check)
        Grammar(GRAM_Check)
        Solution(SOL_Check)


button.bind('<Button-1>', DropDownFunction(0))
button.bind('<Button-1>', DropDownFunction)

# End gridding
canvas.grid()
window.mainloop()

## CODE TO SOLVE THE ISSUE
##0 = on starting bank, 1 = on boat, 2 = on other bank
print("\n--------------------------------------------------")
print("\nThe NFA states and their displays:")
hm1 = hm2 = hm3 = 0
BM = sm1 = sm2 = 0
nrh = nrm = 0

while (nrh != 3 and nrm != 3):
    if (BM == 0 and sm1 == 0):
        sm1 = 1
        BM = 1
        print("BMSM1")
    elif (BM == 1 and sm1 == 1):
        sm1 = 2
        BM = 0
        nrm = nrm + 1
        print("SM1SM1 BMBMBM")
    elif (BM == 0 and hm1 == 0):
        hm1 = 1
        BM = 1
        print("BMHM1")
    elif (BM == 1 and hm1 == 1):
        BM = 0
        hm1 = 2
        nrh = nrh + 1
        print("HM1HM1 BMBMBM")
    elif (hm2 == 0 and hm3 == 0):
        hm2 = 1
        hm3 = 1
        print("HM2HM3")
    elif (hm2 == 1 and hm3 == 1):
        hm2 = 2
        hm3 = 0
        nrh = nrh + 1
        print("HM2HM2 HM3HM3HM3")
    elif (BM == 0 and hm3 == 0):
        hm3 = 1
        BM = 1
        print("BMHM3")
    elif (hm3 == 1 and BM == 1):
        BM = 2
        hm3 = 0
        nrm = nrm + 1
        print("BMBM HM3HM3HM3")
    elif (hm3 == 0 and sm2 == 0):
        hm3 = 1
        sm2 = 1
        print("HM3SM2")
    elif (hm3 == 1 and sm2 == 1):
        hm3 = 2
        sm2 = 2
        nrh = nrh + 1
        nrm = nrm + 1
        print("HM3HM3 SM2SM2")
print("\n--------------------------------------------------")
print("\n Example 1: In a truck there are 2 big boxes and 4 small boxes.\nOn top and beneath each big box there must be a small box after the unloading.\nSmall boxes cannot be unloaded if there is a big box on top.\nBig boxes cannot be unloaded if there is a small box on top.\nPlace the boxes so that it will be easier and safer to unload them.")
print("\n\n 0 - unloaded, 1 - bottom, 2 - middle, 3 - top \n 4 - 1st stack, 5 - 2nd stack \n")

count = 0
bigbox1 = 3
bigbox2 = 2
smallbox1 = 1
smallbox2 = 1
smallbox3 = 2
smallbox4 = 3
number = 3
print("{0},{1},{2},{3},{4},{5}\n".format(bigbox1, bigbox2, smallbox1, smallbox2, smallbox3, smallbox4))

while (count < 6 and number > 0):
    if (bigbox1 == number):
        bigbox1 = 0
        count = count + 1
    if (bigbox2 == number):
        bigbox2 = 0
        count = count + 1
    if (smallbox1 == number):
        smallbox1 = 0
        count = count + 1
    if (smallbox2 == number):
        smallbox2 = 0
        count = count + 1
    if (smallbox3 == number):
        smallbox3 = 0
        count = count + 1
    if (smallbox4 == number):
        smallbox4 = 0
        count = count + 1
    print("{0},{1},{2},{3},{4},{5}\n".format(bigbox1, bigbox2, smallbox1, smallbox2, smallbox3, smallbox4))
    number = number - 1

bigbox1 = 4
bigbox2 = 4
smallbox1 = 5
smallbox2 = 5
smallbox3 = 5
smallbox4 = 5
print("{0},{1},{2},{3},{4},{5}\n".format(bigbox1, bigbox2, smallbox1, smallbox2, smallbox3, smallbox4))

print("\n--------------------------------------------------")
print("\n Example 2: The Hanoi Problem")
print("\n Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: ")
print("\n1) Only one disk can be moved at a time. \n2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack. \n3) No disk may be placed on top of a smaller disk.")
print("\nLet's call the rods D1, D2, D3.")
print("\n For n = 4, we have the following: \n")


def Hanoi(disks, origin, dest, aux):
    if (disks == 1):
        print("Move disk 1 from the origin ", origin, "to the destination: ", dest)
        return
    Hanoi(disks - 1, origin, aux, dest)
    print("Move disk", disks, "from the origin ", origin, "to the destination: ", dest)
    Hanoi(disks - 1, aux, dest, origin)


number_of_disks = 4
Hanoi(number_of_disks, 'D1', 'D2', 'D3')
