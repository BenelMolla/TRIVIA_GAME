from colorama import Fore, Style
import pyodbc

class Trivia_game:

    def law_entrance(self):
        print("\t\t\t\t\t\t\tTHANKS FOR DOWNLOADING\t\t\t\t\t\t\t\t")
        print(
            Fore.LIGHTGREEN_EX + "\t\t\tbefore playing our games, you will need to agree to our privacy policy\n\t\t\tand terms of service Privacy Policy Terms of Service By Answering")
        print(
            "\t\t\t\t\t\t\tyes the Confirm space,\n\t\t\tyou confirm that you are at least 16 years old and have read, \n\t\t\tunderstood and accepted benel's game Privacy Policy and terms of service\n" + Fore.RESET)
        confirm = input("\t\t\t\t\tAre you interested to play this:   ")
        if confirm == "yes":
            return True
        else:
            exit()

    def __init__(self):
        self.Bridge = pyodbc.connect('Driver={SQL Server};'
                                     'Server=LAPTOP-VR9NJF5F;'
                                     'Database=SCHOOL;'
                                     'Trusted_Connection=yes;')
        self.cursor = self.Bridge.cursor()



    def print_banner(self):
        print(Fore.LIGHTWHITE_EX + '\n\t\t=========  WELCOME TO BENEL"S TRIVIA GAME  ========== \n' + Fore.RESET)
        banner = """\


██████╗ ███████╗███╗   ██╗███████╗██╗         ████████╗██████╗ ██╗██╗   ██╗██╗ █████╗ 
██╔══██╗██╔════╝████╗  ██║██╔════╝██║         ╚══██╔══╝██╔══██╗██║██║   ██║██║██╔══██╗
██████╔╝█████╗  ██╔██╗ ██║█████╗  ██║            ██║   ██████╔╝██║██║   ██║██║███████║
██╔══██╗██╔══╝  ██║╚██╗██║██╔══╝  ██║            ██║   ██╔══██╗██║╚██╗ ██╔╝██║██╔══██║
██████╔╝███████╗██║ ╚████║███████╗███████╗       ██║   ██║  ██║██║ ╚████╔╝ ██║██║  ██║
╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═╝

         """

        print(Fore.BLUE + banner + Fore.RESET)

