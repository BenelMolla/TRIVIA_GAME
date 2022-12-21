from TRIVIA_UTILITIES import Trivia_game
from QUESTION_GENERALL import GENERAL_KNOWLEDGE
from QUESTION_FUNNY import FUNNY_QUESTIONS
from colorama import Fore
from QUESTION_TRICKY import TRICKY_QUESTIONS
class UTILITIES(TRICKY_QUESTIONS):

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