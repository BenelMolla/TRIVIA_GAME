# TRIVIA_GAME
___
## THIS PROJECT SHOWS ALL STEPS THAT HOW DOES THE TRIVIA GAME WORK
____
# Requirements for this project

 >>> * Packages
 >>> * Oop implemented
 >>> * Art ASCII Banner 
 >>> * Connecting Database SQL with python

## I used Multilevel inheritance Object oriented

This TRIVIA_GAME Includes Some Parts.

```
 1,The First class contain the method of connecting Database with python
 and some decorection and the first class called trivia_game and in this class
 shows likely here
 class trivia_game():
     def __init__(self):
        self.Bridge = pyodbc.connect('Driver={SQL Server};'
                                     'Server=LAPTOP-VR9NJF5F;'
                                     'Database=SCHOOL;'
                                     'Trusted_Connection=yes;')
        self.cursor = self.Bridge.cursor()

2,The second and thired and Forth classes contains all questions that have in three catagories
the second class called QUESTION_GENERAL the tsired one is QUESTION FUNNY and the last one is QUESTION about Trick it's
also called QUESTION_TRICKY
   
       def General_n(self):
        X = 'SELECT Question,A,B,C,D,Answer FROM dbo.Questions'
        cursor = self.Bridge.cursor()
        cursor.execute(X)
        score = 0
        for i in cursor:
            print(i[0])
            print("A", i[1], "\n", "B", i[2], "\n", "C", i[3], "\n", "D", i[4])
            answer = input(Fore.LIGHTMAGENTA_EX + "enter the answer: " + Fore.RESET)
            if answer == i[5]:
                score = score + 1
                print(Fore.LIGHTGREEN_EX + "Correct" + Fore.RESET)
            else:
                print(Fore.RED + "FAILED" + Fore.RESET)
        print("Your final score is :", score, "/8")

        PersonId = int(input(Fore.LIGHTGREEN_EX + "enter your id number:   " + Fore.RESET))
        LastName = input(Fore.LIGHTGREEN_EX + "enter your lastname:    " + Fore.RESET)
        FirstName = input(Fore.LIGHTGREEN_EX + "enter your firstname:   " + Fore.RESET)
        City = input(Fore.LIGHTGREEN_EX + "enter your city:    " + Fore.RESET)
        Result = score
        cursor.execute(
               "INSERT INTO SCHOOL.dbo.Examers(PersonId, LastName, FirstName, City, Result) VALUES (?, ?, ?, ?, ?)",
            (PersonId, LastName, FirstName, City, Result))
        self.Bridge.commit()
        exit()
  3, And the last part of the TRIVIA GAME class called UTILITIES
  In this  class order the project and all the function part are found here
  
           def Grade(self):
        while True:
            user = int(input(Fore.BLUE + "CHOOSE A CATAGORY >\n\n" + Fore.RESET + Fore.LIGHTYELLOW_EX +
                             "1, GENERAL KNOWLEDGE QUESTIONS\t\t\n" + Fore.RESET +
                             Fore.LIGHTYELLOW_EX + "2, FUNNY QUESTIONS\t\t\n" + Fore.RESET +
                             Fore.LIGHTYELLOW_EX + "3, TRICKY QUESTIONS:       " + Fore.RESET + '\n'))

            if user == 1:
                ben = GENERAL_KNOWLEDGE()
                ben.General_n()
            elif user == 2:
                lun = FUNNY_QUESTIONS()
                lun.Funny_Q()

            elif user == 3:
                thor = TRICKY_QUESTIONS()
                thor.Tricky_Q()
            else:
                print("Thanks for staying with us! byy")
hoot = Trivia_game()
hoot.print_banner()
hoot.law_entrance()
like = UTILITIES()
like.Grade() 

```

>>> # PACKAGES that I Used
> * COLORAMA Fore, Style
> 
> * COLORED
> 
> * Pyodbc
> 
> * Pip

 # INSTRUCTION
follow the instruction in the bellow
___
* All answers need to be answered with capital letter
* Give A correct answer
* No looking up information on cell phone
* Teams can't Change their answers after submitting a response

````
# Submitted day 21/12/22
````
> AUTHOR NAME BENEL MOLLA
> 
> https://github.com/BenelMolla


