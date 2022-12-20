#Need to pause this project. Unable to figure out:
#How to keep what image_number was selected and compare that
#with what the computer has selected

#Ideally, once the player and computer have selected an image, the
#winner would be declared

from tkinter import *
from PIL import ImageTk, Image
import random
import os

root = Tk()
root.title("Rock, Paper, Scissors")

paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png"))

image_list = [paper_img, rock_img, scissors_img]
image_number = 1

#Label for the first image
paper_label = Label(image=paper_img)
paper_label.grid(row=0, column=0, columnspan=3)


#Button Functions
    #could not get all widgets to delete when 'Select' button was clicked if
    #forward button was pressed first.
    #Had to insert all buttons into each function so that they are referenced in the function
    #and can then be forgotten
def forward(image_number):
    global paper_label
    global button_forward
    global button_select
    global button_back
    #Forgets widgets
    button_forward.grid_forget()
    button_back.grid_forget()
    button_select.grid_forget()
    paper_label.grid_forget()

    paper_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    button_select = Button(root, text="Select Character", command=select)

    if image_number == 3:
        button_forward = Button(root, text=">>", state=DISABLED)

    paper_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    button_select.grid(row=1, column=1)

def back(image_number):
    global paper_label
    global button_forward
    global button_select
    global button_back
    #Forgets Widgets
    button_forward.grid_forget()
    button_back.grid_forget()
    button_select.grid_forget()
    paper_label.grid_forget()

    paper_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    button_select = Button(root, text="Select Character", command=select)

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    paper_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    button_select.grid(row=1, column=1)

def select():
    global paper_label
    global button_forward
    global button_back
    global button_select
    global button_start_game

    #Removes Buttons From Scrren
    button_forward.grid_forget()
    button_back.grid_forget()
    button_select.grid_forget()

    #Prints Image to Screen
    paper_label.grid(row=2, column=0, columnspan=3)
    #Labels
    player_label = Label(root, text="You've chosen: ")
    player_label.grid(row=0, column=1)
    comp_choice = Label(root, text="Computer has chosen: ")
    comp_choice.grid(row=0, column=3)

    #Computer's Random Choice/Put it on Screen
    computer = random.choice([paper_img, rock_img, scissors_img])
    computer_label = Label(root, image=computer)
    computer_label.grid(row=2, column=3)

    #Missing/Unsure:
    #comparing user and computer choice, determining winner

#Original Buttons
button_select = Button(root, text="Select Character", command=select)
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_back= Button(root, text="<<", command=back, state=DISABLED)

button_forward.grid(row=1, column=2)
button_select.grid(row=1, column=1)
button_back.grid(row=1, column=0)


root.mainloop()
