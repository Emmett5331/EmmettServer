from colorama import Fore, Style, init
import datetime
import random
init(autoreset=True)

# Basic colored message
def say(message: str, color: str = "green"):
    colors = {"red": Fore.RED, "green": Fore.GREEN, "blue": Fore.BLUE, "yellow": Fore.YELLOW, "magenta": Fore.MAGENTA, "cyan": Fore.CYAN}
    print(colors.get(color.lower(), Fore.GREEN) + message + Style.RESET_ALL)

# Greeting / Farewell
def greet(name: str):
    print(f"{Fore.GREEN}Hello, {name}! Welcome to PromptHub!{Style.RESET_ALL}")

def farewell(name: str):
    print(f"{Fore.RED}Goodbye, {name}! See you later!{Style.RESET_ALL}")

# Information / Warnings / Errors
def info(msg: str):
    print(Fore.CYAN + "[INFO] " + msg + Style.RESET_ALL)

def warn(msg: str):
    print(Fore.YELLOW + "[WARNING] " + msg + Style.RESET_ALL)

def error(msg: str):
    print(Fore.RED + "[ERROR] " + msg + Style.RESET_ALL)

# Utilities
def current_time():
    now = datetime.datetime.now()
    print(Fore.MAGENTA + f"Current time: {now}" + Style.RESET_ALL)

def random_number(min_val: int = 0, max_val: int = 100):
    num = random.randint(min_val, max_val)
    print(Fore.BLUE + f"Random number ({min_val}-{max_val}): {num}" + Style.RESET_ALL)

def echo(text: str, repeat: int = 1):
    for _ in range(repeat):
        print(text)
