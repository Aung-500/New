'''
arr=['apple','banana','cherry']
for i in range (len(arr)):
  arr[i]="Eat "+arr[i]
  print(arr[i])
else:
  print("Finally")
print(arr)

#=--------------------------------------------------------------------------------
firstnum = input("Enter First Number ? : ")
secondnum = input("Enter Second Number (between 1-10) ? : ")
try :
    firstnum = int(firstnum)
    secondnum = int(secondnum)
    if secondnum <= 0 :
        print ("Second number must be greater than 0")
    elif secondnum < 1 or secondnum > 10 :
        print ("Second number must be between 1-10")
    else:
        print (firstnum, " divied by ",secondnum)
        print (firstnum/secondnum)
except ValueError:
    print ("Please enter number only")

#=--------------------------------------------------------------------------------
x = input("Enter first value : ")
y = input("Enter second value : ")
op = input("Operator (+ - * /) : ")
try :
    x = int(x)
    y = int(y)
    output = True
    if op == "+" :
      result = x+y
    elif op == "-" :
      result = x-y
    elif op == "*" :
      result = x*y
    elif op == "/" :
      result = x/y
    else :
      output = False
      print("Wrong Operator")
    if output :
      print("Result is ",result)
except ValueError:
    print("Please enter number only")
    print(ValueError);
#=--------------------------------------------------------------------------------

for x in range(6):
  for k in range(x):
    print("*", end="")
  print("")

#=-------------------------------------------------------------------------------
aa = 0;
for x in range(7):
    aa = aa + 1
    # print(aa)
    if (aa%2) == 0 :
      print(aa, "is Even.")
    else:
      print(aa, "is Odd.")
#=-------------------------------------------------------------------------------

#=-------------------------------------------------------------------------------

#=-------------------------------------------------------------------------------

#=-------------------------------------------------------------------------------

#=-------------------------------------------------------------------------------

#=-------------------------------------------------------------------------------
'''
# class animal:
#     number_of_legs = 0
#     def sleep(slef):
#       print("zzz")
# dog = animal()
# dog.sleep()

# class animal:
#   number_of_legs = 0
#   def sleep(slef) :
#     print("zzz")
#   def count_legs(self) :
#     print("I have {} legs".format(self.number_of_legs))
#   def test(egg, oil) : # Ask+++++++++
#     print(egg, oil) # Ask+++++++
# class dog(animal):
#   def bark(self):
#     print("Woof")
# mydog = dog()
# mydog.bark();
# mydog.sleep();
# mydog.count_legs();
# mydog.test('egg','oil'); # Ask+++++++++++


# class Stack:  ############ Stack ########
#   def __init__(self):
#     self.items = []
#     def is_empty(self):
#       return self.items == []
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#       return self.items.pop()
#     def peek(self):
#       return self.items[len(self.items) - 1]
#     def size(self):
#       return len(self.items)
#       s = Stack()
#       print(s.is_empty())
#       s.push(4)
#       s.push('dog')
#       print(s.peek())
#       s.push(True)
#       print(s.size())
#       s.push(8.4)
#       print(s.pop())
#       print(s.pop())
#       print(s.size())

class Queue:  # Queue #########
    def __init__(self):
        self.items = []
        def isEmpty(self):
            return self.items == []
        def enqueue(self, item):
            self.items.insert(0, item)
        def dequeue(self):
            return self.items.pop()
        def size(self):
            return len(self.items)


# =-------------------------------------------------------------------------------

# ===============================================================================================================
#                                    Projects
#                                    Projects

# import cv2
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
# while True:
#     success, img = cap.read()
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# =---------------------------------------------------------
# print("Welcome to my computer quiz!")

# playing = input("Do you want to play? ")

# if playing.lower() != "yes":
#     quit()

# print("Okay! Let's play :)")

# score = 0

# answer = input("What does CPU stand for? ")
# if answer.lower() == "central processing unit":
#     print('Correct!')
#     score += 1
# else:
#     print("Incorrect!")

# answer = input("What does GPU stand for? ")
# if answer.lower() == "graphics processing unit":
#     print('Correct!')
#     score += 1
# else:
#     print("Incorrect!")

# answer = input("What does RAM stand for? ")
# if answer.lower() == "random access memory":
#     print('Correct!')
#     score += 1
# else:
#     print("Incorrect!")

# answer = input("What does PSU stand for? ")
# if answer.lower() == "power supply":
#     print('Correct!')
#     score += 1
# else:
#     print("Incorrect!")

# print("You got " + str(score) + " questions correct!")
# print("You got " + str((score / 4) * 100) + "%.")
# =---------------------------------------------------------------

# Good running program
# import random
# from tkinter import *

# def next_turn(row, column):
#     global player

#     if buttons[row][column]['text'] == "" and check_winner() is False:

#         if player == players[0]:  # if its not player 1 turn then it will be else

#             buttons[row][column]['text'] = player

#             if check_winner() is False:
#                 player = players[1]
#                 label.config(text=(players[1] + " turn"))

#             elif check_winner() is True:
#                 label.config(text=(players[0] + " wins"))

#             elif check_winner() == "Tie":
#                 label.config(text=("Tie!"))
#         else:

#             buttons[row][column]['text'] = player
#             if check_winner() is False:
#                 player = players[0]
#                 label.config(text=(players[0] + " turn"))

#             elif check_winner() is True:
#                 label.config(text=(players[1] + " wins"))

#             elif check_winner() == "Tie":
#                 label.config(text="Tie!")


# def check_winner():
#     for row in range(3):
#         if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
#             buttons[row][0].config(bg="light green")
#             buttons[row][1].config(bg="light green")
#             buttons[row][2].config(bg="light green")
#             return True

#     for column in range(3):
#         if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
#             buttons[0][column].config(bg="light green")
#             buttons[1][column].config(bg="light green")
#             buttons[2][column].config(bg="light green")
#             return True

#     if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
#         buttons[0][0].config(bg="light green")
#         buttons[1][1].config(bg="light green")
#         buttons[2][2].config(bg="light green")
#         return True

#     elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
#         buttons[0][2].config(bg="light green")
#         buttons[1][1].config(bg="light green")
#         buttons[2][0].config(bg="light green")
#         return True

#     elif empty_spaces() is False:
#         for row in range(3):
#             for column in range(3):
#                 buttons[row][column].config(bg="yellow")
#         return "Tie"

#     else:
#         return False


# def empty_spaces():
#     spaces = 9
#     for row in range(3):
#         for column in range(3):
#             if buttons[row][column]['text'] != "":
#                 spaces -= 1
#     if spaces == 0:
#         return False
#     else:
#         return True


# def new_game():
#     global player

#     player = random.choice(players)
#     label.config(text=player + " turn")
#     for row in range(3):
#         for column in range(3):
#             buttons[row][column].config(text="", bg="#F0F0F0")


# windows = Tk()
# players = ["x", "o"]
# player = random.choice(players)
# buttons = [[0, 0, 0],
#            [0, 0, 0],
#            [0, 0, 0]]

# label = Label(text=player + " turn", font=('bell mt', 40))
# label.pack(side="top")

# reset_button = Button(text="Restart", font=('bell mt', 20), command=new_game)
# reset_button.pack(side="top")

# frame = Frame(windows)
# frame.pack()

# for row in range(3):
#     for column in range(3):
#         buttons[row][column] = Button(frame, text="", width=5, height=2, font=('ink free', 25),
#                                       command=lambda row=row, column=column: next_turn(row, column))
#         buttons[row][column].grid(row=row, column=column)

# windows.mainloop()

# =-----------------------------------------------------------------------------------

# """ Mad Libs Generator
# ----------------------
# """
# #Loop back to this point once code finishes
# from re import A


# loop = 1
# while (loop > 0):
# # All the questions that the program asks the user
#     noun = input("Choose a noun: ")
#     p_noun = input("Choose a plural noun: ")
#     noun2 = input("Choose a noun: ")
#     place = input("Name a place: ")
#     adjective = input("Choose an adjective (Describing word): ")
#     noun3 = input("Choose a noun: ")
# # Displays the story based on the users input
#     print ("------------------------------------------")
#     print ("Be kind to your",noun,"- footed", p_noun)
#     print ("For a duck may be somebody's", noun2,",")
#     print ("Be kind to your",p_noun,"in",place)
#     print ("Where the weather is always",adjective,".")
#     print ()
#     print ("You may think that is this the",noun3,",")
#     print ("Well it is.")
#     print ("------------------------------------------")
# # Loop back to "loop = 1"
#     loop = loop + 1
# =-----------------------------------------------------------------------------------

# """ Number Guessing Game
# ----------------------------------------
# """
# import random
# attempts_list = []
# def show_score():
#     if len(attempts_list) <= 0:
#         print("There is currently no high score, it's yours for the taking!")
#     else:
#         print("The current high score is {} attempts".format(min(attempts_list)))
# def start_game():
#     random_number = int(random.randint(1, 10))
#     print("Hello traveler! Welcome to the game of guesses!")
#     player_name = input("What is your name? ")
#     wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
#     # Where the show_score function USED to be
#     attempts = 0
#     show_score()
#     while wanna_play.lower() == "yes":
#         try:
#             guess = input("Pick a number between 1 and 10 ")
#             if int(guess) < 1 or int(guess) > 10:
#                 raise ValueError("Please guess a number within the given range")
#             if int(guess) == random_number:
#                 print("Nice! You got it!")
#                 attempts += 1
#                 attempts_list.append(attempts)
#                 print("It took you {} attempts".format(attempts))
#                 play_again = input("Would you like to play again? (Enter Yes/No) ")
#                 attempts = 0
#                 show_score()
#                 random_number = int(random.randint(1, 10))
#                 if play_again.lower() == "no":
#                     print("That's cool, have a good one!")
#                     break
#             elif int(guess) > random_number:
#                 print("It's lower")
#                 attempts += 1
#             elif int(guess) < random_number:
#                 print("It's higher")
#                 attempts += 1
#         except ValueError as err:
#             print("Oh no!, that is not a valid value. Try again...")
#             print("({})".format(err))
#     else:
#         print("That's cool, have a good one!")
# if __name__ == '__main__':
#     start_game()

# =-----------------------------------------------------------------------------------
