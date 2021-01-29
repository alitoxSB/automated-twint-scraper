import twint
import colorama
from colorama import Fore,Back, Style
# Configure
from twint.twint import Config, run
c = Config()
colorama.init(autoreset=True)

def searching():
    """

    """
    menu_art()
    first_word = input(f"{Fore.RED}Write word for search in Twitter: ")
    option = int(input('You need other word in tweet to scraping? 1: Yes or 2: No '))
    if (option == 1):
        second_word = input(f"{Fore.RED}Write second word for search in Twitter: ")
    else:
        pass

    c.Search = first_word+ "\"" +second_word + "\""
    print(f"{Fore.RED}Since date do you want in Twitter?")
    print(f"{Fore.RED}Enter date like this: Year: 2021, Month: 01, Day: 01")
    year = input(f"{Fore.RED}Year: ")
    month = input(f"{Fore.RED}Month: ")
    day = input(f"{Fore.RED}Day: ")
    since = year+"-"+month+"-"+day+" "+"00:00:00"
    c.Since = since
    c.Output = "tweets.csv"
    run.Search(c)

def menu_art():
    print(f"{Fore.BLUE}████████╗░██╗░░░░░░░██╗██╗████████╗████████╗███████╗██████╗░")
    print(f"{Fore.BLUE}╚══██╔══╝░██║░░██╗░░██║██║╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗")
    print(f"{Fore.BLUE}░░░██║░░░░╚██╗████╗██╔╝██║░░░██║░░░░░░██║░░░█████╗░░██████╔╝")
    print(f"{Fore.BLUE}░░░██║░░░░░████╔═████║░██║░░░██║░░░░░░██║░░░██╔══╝░░██╔══██╗")
    print(f"{Fore.BLUE}░░░██║░░░░░╚██╔╝░╚██╔╝░██║░░░██║░░░░░░██║░░░███████╗██║░░██║")
    print(f"{Fore.BLUE}░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝")
    print(f"{Fore.RED}[*] Welcome to Twitter scraper")

if __name__ == '__main__':
    searching()
