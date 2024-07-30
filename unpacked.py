import os
from colorama import init, Fore

init(autoreset=True)

def clear_screen():
     os.system('cls' if os.name == 'nt' else 'clear')

def print_blue(text):
    print(Fore.BLUE + text)

ascii_art = """
██████╗ ██████╗ ██╗██╗   ██╗ █████╗ ████████╗███████╗    ███████╗███████╗██████╗ ██╗   ██╗██╗ ██████╗███████╗███████╗
██╔══██╗██╔══██╗██║██║   ██║██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝██╔════╝██╔══██╗██║   ██║██║██╔════╝██╔════╝██╔════╝
██████╔╝██████╔╝██║██║   ██║███████║   ██║   █████╗      ███████╗█████╗  ██████╔╝██║   ██║██║██║     █████╗  ███████╗
██╔═══╝ ██╔══██╗██║╚██╗ ██╔╝██╔══██║   ██║   ██╔══╝      ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██║██║     ██╔══╝  ╚════██║
██║     ██║  ██║██║ ╚████╔╝ ██║  ██║   ██║   ███████╗    ███████║███████╗██║  ██║ ╚████╔╝ ██║╚██████╗███████╗███████║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝╚══════╝╚══════╝
"""

footer_text = "Made by gdzo https://discord.gg/eGVhhkHMhz"
clear_screen()

print_blue(ascii_art)
print_blue(footer_text)
print(" ")
print(" ")
print(" ")
print(" ")
webhook = input(Fore.BLUE + "Enter Your Webhook => ")
print_blue(f"Dostal Jsi Scam Brasko :D")

