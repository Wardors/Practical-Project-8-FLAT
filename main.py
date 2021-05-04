
### Consider the following puzzle: “On one side of a river are three humans, one big
### monkey, two small monkeys, and one boat. Each of the humans and the big monkey are
### strong enough to row the boat. The boat can fit one or two bodies (regardless of size). If at
### any time at either side of the river the monkeys outnumber the humans, the monkeys will
### eat the humans. How do you get everyone on the other side of the river alive?” Show that
### the language of solutions to the puzzle is regular. Write a finite automaton for the puzzle
### to a file (perhaps using a script if you need it). Using the previously written program find
### and print a solution to the puzzle. The printing should be done to be “understandable by
### humans”2


import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

NFA_Check = 0
GRAM_Check = 0
SOL_Check = 0


#Main loop
window = tk.Tk()
window.title(string="FLAT project 8")
#Options
options=["Problem Solution","Grammar Display","NFA Display"]
#For DropDown
clicked= StringVar()
clicked.set(options[0])
#Canvas
canvas = tk.Canvas(window,width=1920,height=1080)

#TopLabel
WelcomeLabel = tk.Label(window,text="Welcome to the project. For it, we had to solve the following puzzle:\n\n")
ProblemLabel = tk.Label(window,text="On one side of a river are three humans, one big monkey, two small monkeys, and one boat. Each of the humans and the big monkey arestrong enough to row the boat. The boat can fit one or two bodies (regardless of size). If at any time at either side of the river the monkeys outnumber the humans, the monkeys will eat the humans.\n\nHow do you get everyone on the other side of the river alive?\n")
WelcomeLabel.grid(row=0,column=0,sticky=W)
ProblemLabel.grid(row=1,column=0,sticky=W)
#DropDown
drop = OptionMenu(window,clicked,*options)
drop.grid(columnspan = 5)
#Button
button = tk.Button(window,text="Display")
button.grid()
#Images
NFA_image=PhotoImage(file="FLAT Project\Grammar\Proper_NFA.png")
GRAM_image=PhotoImage(file="FLAT Project\Grammar\Grammar.png")
SOL_image=PhotoImage(file="FLAT Project\Drawing_States\All_States_Long.png")
#MainLabels
NFA_label=tk.Label(window,image=NFA_image)
NFA_text=tk.Label(window,text="This is the NFA automata created in order to solve the problem.")
GRAM_label=tk.Label(window,image=GRAM_image)
GRAM_text=tk.Label(window,text="This is the grammar of the problem.")
SOL_label = tk.Label(window, image=SOL_image)
SOL_text = tk.Label(window, text="The solution requires procedural trasnition - step by step as presented from left to right in the images.")

NFA_label.grid()
NFA_text.grid()
GRAM_label.grid()
GRAM_text.grid()
SOL_label.grid()
SOL_text.grid()



#FunctionOfDisplay

def NFA(Check):
    if(Check==1):
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
    if (the_option==options[0]):
        GRAM_Check=0
        NFA_Check=0
        SOL_Check=1
        NFA(NFA_Check)
        Grammar(GRAM_Check)
        Solution(SOL_Check)
    elif(the_option==options[1]):
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



button.bind('<Button-1>',DropDownFunction(0))
button.bind('<Button-1>',DropDownFunction)

#End gridding
canvas.grid()
window.mainloop()


## CODE TO SOLVE THE ISSUE
##0 = on starting bank, 1 = on boat, 2 = on other bank
hm1=hm2=hm3=0
BM=sm1=sm2=0
nrh=nrm=0

while(nrh!=3 and nrm!=3):
    if(BM == 0 and sm1 == 0):
        sm1=1
        BM=1
        print("BMSM1")
    elif(BM == 1 and sm1 == 1):
        sm1=2
        BM=0
        nrm=nrm+1
        print("SM1SM1 BMBMBM")
    elif(BM == 0 and hm1 == 0):
        hm1=1
        BM=1
        print("BMHM1")
    elif(BM == 1 and hm1 == 1):
        BM=0
        hm1=2
        nrh=nrh+1
        print("HM1HM1 BMBMBM")
    elif(hm2 == 0 and hm3 == 0):
        hm2 = 1
        hm3 = 1
        print("HM2HM3")
    elif(hm2 == 1 and hm3 == 1):
        hm2 = 2
        hm3 = 0
        nrh=nrh+1
        print("HM2HM2 HM3HM3HM3")
    elif(BM == 0 and hm3 == 0 ):
        hm3 = 1
        BM = 1
        print("BMHM3")
    elif(hm3 == 1 and BM == 1):
        BM = 2
        hm3 = 0
        nrm=nrm+1
        print("BMBM HM3HM3HM3")
    elif(hm3 == 0 and sm2 == 0):
        hm3 = 1
        sm2 = 1
        print("HM3SM2")
    elif(hm3 == 1 and sm2 == 1):
        hm3 = 2
        sm2 = 2
        nrh = nrh+1
        nrm = nrm+1
        print("HM3HM3 SM2SM2")
