from colorama import Fore
from QUESTION_GENERALL import GENERAL_KNOWLEDGE
class FUNNY_QUESTIONS(GENERAL_KNOWLEDGE):

    def __init__(self):
        super().__init__()

    def Funny_Q(self):
        Y = 'SELECT Questions,A,B,C,D,Answer FROM dbo.Funny_Question'
        cursor = self.Bridge.cursor()
        cursor.execute(Y)
        score = 0
        for i in cursor:
            print(i[0])
            print("A", i[1], "\n", "B", i[2], "\n", "C", i[3], "\n", "D", i[4])
            answer = input(Fore.LIGHTMAGENTA_EX + "enter the answer: " + Fore.RESET)
            if answer == i[5]:
                score += 1
                print(Fore.LIGHTGREEN_EX + "Correct" + Fore.RESET)
            else:
                print(Fore.RED + "FAILED" + Fore.RESET)
        print("Your final score is :", score, "/5")
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
