from math import ceil
from tkinter import *
from random import random


global l

l = {"How much is a baker's dozen?":13,\
            "Vagh is Klingon for which number?":5,\
            "How many yards are there in a chain?":22,\
            "Charles Atlas marketed his fitness program for the 'how many' pound weakling?":97, \
            "If an internet user follows a broken or dead link, they will typically find an error page with which number error message?":404, \
            "The Arctic Monkeys wrote a song about which number?":505,\
            "In inches, how high is a table tennis net?":6 }


def generateGkQuestion():
    r = random()
    answer_list = [
            "How much is a baker's dozen?", #13
            "Vagh is Klingon for which number?" #5
            "How many yards are there in a chain?" #22
            "Charles Atlas marketed his fitness program for the 'how many' pound weakling?" #97
            "If an internet user follows a broken or dead link, they will typically find an error page with which number error message?" #404
            "The Arctic Monkeys wrote a song about which number?" #505
            "In inches, how high is a table tennis net?" #6
    ]
    amount_of_questions = len(answer_list)-1
    r = ceil(r*amount_of_questions)
    return answer_list[r]


def generateGkAnswer(s):
    global l
    return l[s]

def generateQuestion():
    r = random()
    x = ceil(r * 10)
    r = random()
    y = ceil(r * 10)
    op = randomOperator(ceil(r * 4))
    s = str(x) + " " + op + " " + str(y) + " = "
    return s


def generateAnswer(s):
    a = s.split(" ")
    x = int(a[0])
    op = a[1]
    y = int(a[2])
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return "{:.2f}".format(x/y)
    else:
        return x + y


def randomOperator(r):
    if r == 1:
        return '+'
    elif r == 2:
        return '-'
    elif r == 3:
        return '*'
    elif r == 4:
        return '/'
    else:
        return '+'


def click_number(num):
    s = str(answer_box.get()) + str(num)
    answer_box.delete(0, END)
    answer_box.insert(0, s)
    print(s)


def click_clear():
    answer_box.delete(0, END)


def click_enter(answer, label):
    label.config(text="")
    # if correct, allow moving to next question
    if answer_box.get() != "" and float(answer_box.get()) == answer:
        print("Correct answer")
        label.config(text="That was correct!")

        curr_score = int(score_box.get())
        updated_score = curr_score + 1
        score_box.delete(0, END)
        score_box.insert(0, str(updated_score))

        # allow move to next question
        next_btn["state"] = NORMAL
    else:
        # print incorrect answer
        print("Incorrect answer")
        label.config(text="That was incorrect! Try again!")
        answer_box.delete(0, END)


def click_next():
    global question
    question_box.delete(0, END)
    answer_box.delete(0, END)
    question = generateQuestion()
    question_box.insert(0, question)
    next_btn["state"] = DISABLED
    correct_incorrect_label.config(text="")


def click_exit():
    exit()


root = Tk()

root.title("Quiz Game")

label_score = Label(root, text="Score: ")
score_box = Entry(root, width=40)
label_score.grid(row=0, column=0, columnspan=3)
score_box.grid(row=1, column=0, columnspan=3, pady=10, padx=10)
score_box.insert(0, "0")

label_question = Label(root, text="Question: ")
question_box = Entry(root, width=40)
label_question.grid(row=2, column=0, columnspan=3)
question_box.grid(row=3, column=0, columnspan=3, pady=10, padx=10)
question = generateQuestion()
question_box.insert(0, question)

label_answer = Label(root, text="Answer: ")
answer_box = Entry(root, width=40)
label_answer.grid(row=4, column=0, columnspan=3)
answer_box.grid(row=5, column=0, columnspan=3, pady=10, padx=10)

correct_incorrect_label = Label(root, text="")
correct_incorrect_label.grid(row=6, column=0, columnspan=3)


x_pad = 40
y_pad = 20

btn1 = Button(root, text=1, padx=x_pad, pady=y_pad, command=lambda: click_number(1))
btn2 = Button(root, text=2, padx=x_pad, pady=y_pad, command=lambda: click_number(2))
btn3 = Button(root, text=3, padx=x_pad, pady=y_pad, command=lambda: click_number(3))
btn4 = Button(root, text=4, padx=x_pad, pady=y_pad, command=lambda: click_number(4))
btn5 = Button(root, text=5, padx=x_pad, pady=y_pad, command=lambda: click_number(5))
btn6 = Button(root, text=6, padx=x_pad, pady=y_pad, command=lambda: click_number(6))
btn7 = Button(root, text=7, padx=x_pad, pady=y_pad, command=lambda: click_number(7))
btn8 = Button(root, text=8, padx=x_pad, pady=y_pad, command=lambda: click_number(8))
btn9 = Button(root, text=9, padx=x_pad, pady=y_pad, command=lambda: click_number(9))
btn0 = Button(root, text=0, padx=x_pad, pady=y_pad, command=lambda: click_number(0))
decimal_point_btn = Button(root, text="-", padx=x_pad, pady=y_pad, command=lambda: click_number("-"))
minus_btn = Button(root, text=".", padx=x_pad, pady=y_pad, command=lambda: click_number("."))

clear_btn = Button(root, text="Clear", command=lambda: click_clear())
enter_btn = Button(root, text="Enter", command=lambda: click_enter(generateAnswer(question), correct_incorrect_label))
next_btn = Button(root, text="Next", state="disabled", command=lambda: click_next())
exit_btn = Button(root, text="Exit", command=lambda: click_exit())

btn1.grid(row=7, column=0)
btn2.grid(row=7, column=1)
btn3.grid(row=7, column=2)
btn4.grid(row=8, column=0)
btn5.grid(row=8, column=1)
btn6.grid(row=8, column=2)
btn7.grid(row=9, column=0)
btn8.grid(row=9, column=1)
btn9.grid(row=9, column=2)
decimal_point_btn.grid(row=10, column=0)
btn0.grid(row=10, column=1)
minus_btn.grid(row=10, column=2)


clear_btn.grid(row=11, column=0)
enter_btn.grid(row=11, column=1)
next_btn.grid(row=11, column=2)
exit_btn.grid(row=12, column=0)

root.mainloop()
