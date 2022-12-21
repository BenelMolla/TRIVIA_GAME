from colorama import Fore
from TRIVIA_UTILITIES import Trivia_game

class GENERAL_KNOWLEDGE(Trivia_game):

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
        print(Fore.RED + "FOR TO START FIRST FILL YOUR PERSONAL DETAILS!" + Fore.RESET)
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
