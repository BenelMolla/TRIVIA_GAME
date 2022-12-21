from colorama import Fore
from QUESTION_FUNNY import FUNNY_QUESTIONS
class TRICKY_QUESTIONS(FUNNY_QUESTIONS):

    def Tricky_Q(self):

        cursor = self.Bridge.cursor()
        z = 'SELECT Question,Answer FROM dbo.Tricky_Questions'
        cursor.execute(z)
        score = 0
        for i in cursor:
            print(i[0])
            Answer = input(Fore.LIGHTMAGENTA_EX + "enter the answer: " + Fore.RESET)
            if Answer == i[1]:
                score += 1
                print(Fore.LIGHTGREEN_EX + "Correct" + Fore.RESET)
            else:
                print(Fore.RED + "FAILED" + Fore.RESET)
        print("Your final score is :", score, "/11")
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
