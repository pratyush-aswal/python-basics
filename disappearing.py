import random

words = ["ablegate","activism","barbican","barterer","callback","coupling","deflated","duckweed","earnings","eggshell","failures","feedlots"]

def word_select():
    global puzzle
    puzzle = random.choice(words)


is_disappear = False
str_head = "^"
str_eyes = "0.0"
str_body = "/||\\"
str_legs = "/\\"
puzzle = ""
word_select()
random_index= random.sample((0,1,2,3,4,5,6,7),3)
show_puzzle_var = []
choice='a'
no_of_attempts = 0
wrong_attempts = []
win=False
for x in range(8):
    if x in random_index:
        show_puzzle_var.append(puzzle[x])
    else:
        show_puzzle_var.append("_")

def show_puzzle():
    global show_puzzle_var
    global random_index
    global puzzle
    print(*show_puzzle_var,sep=" ")


def show():
    print(" ",str_head)
    print("",str_eyes)
    print(str_body)
    print("",str_legs)


def disappear():
    global str_legs
    global str_body
    global str_eyes
    global str_head
    global is_disappear
    if len(str_legs)!=0 :
        str_legs = str_legs[:-1]
    elif len(str_body)!=0 :
        str_body = str_body[:-1]
    elif len(str_eyes)!=0 :
        str_eyes = str_eyes[:-1]
    elif len(str_head)!=0 :
        str_head = str_head[:-1]
        is_disappear = True



def input_choice():
    global choice
    choice = input("Guess a letter ")

def matcher():
    global choice
    global no_of_attempts
    global show_puzzle_var
    global puzzle
    no_of_attempts+=1
    iswrong=True
    if choice in puzzle:
        for x in range(8):
            if puzzle[x] == choice and show_puzzle_var[x] == "_":
                show_puzzle_var[x]=choice
                iswrong=False
    if iswrong:
        wrong_attempts.append(choice)
        disappear()
    print("total attempts :", no_of_attempts)
    print("wrong guesses :", wrong_attempts)

def result():
    global is_disappear
    global win
    if show_puzzle_var.count("_") == 0:
        print("Correct answer is :", puzzle)
        print("YOU WON")
    if is_disappear:
        print("Correct answer is :", puzzle)
        print("YOU LOST")

while wrong_attempts.__len__() < 10 and show_puzzle_var.count("_") != 0:
    show()
    show_puzzle()
    input_choice()
    matcher()
result()


