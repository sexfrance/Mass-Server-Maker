import os
import glob
import random
import time
import requests
from colorama import Fore
from utils.valid import validateToken

invalid = False

choice = input(f"{Fore.YELLOW}Enter your account token: {Fore.RESET}")
token = validateToken(choice)

if not invalid:
    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'fr,fr-FR;q=0.9',
        'authorization': token,
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/channels/@me/1107247318064963624',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDQzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MzEiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImZyIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwNDMgQ2hyb21lLzEyMC4wLjYwOTkuMjkxIEVsZWN0cm9uLzI4LjIuMTAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjI4LjIuMTAiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyODgyMjAsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQ2OTUyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9',
    }
    name = input(f"{Fore.GREEN}Server Name: {Fore.RESET}")

    # Get list of filenames in the Icons folder
    icon_filenames = glob.glob("Icons/*.png")

    # If there are any icons in the folder, select one randomly
    if icon_filenames:
        icon_filename = random.choice(icon_filenames)

        # Open the icon file and read its contents
        with open(icon_filename, "rb") as f:
            icon_data = f.read()

        # Encode the icon data as base64
        import base64
        icon_base64 = base64.b64encode(icon_data).decode()

        # Include the icon data in the request data
        data = f'{{"name":"{name}","icon":"data:image/png;base64,{icon_base64}"}}'
    else:
        data = '{"name":"' + name + '","icon":null}'

    # Ask for the number of servers until a valid number is entered
    while True:
        ask = input(f"{Fore.GREEN}In how many servers are you in: {Fore.RESET}")
        if ask.isdigit():
            enablecount = int(ask)
            break
        else:
            print(f"{Fore.RED}Please enter a valid number.{Fore.RESET}")

  

    nitro = input(f"{Fore.GREEN}Do you have nitro? (y/n): {Fore.RESET}")
    if nitro == "y" or "yes":
        limit = 200
    else:
        limit = 100
    
    templateask = input(f"{Fore.GREEN}Do you wish to use a template? (y/n): {Fore.RESET}")
    
    if templateask == "y":
        templatecode = input(f"{Fore.GREEN}Enter template code (e.g: fwjWhEcnvScd): {Fore.RESET}")
        template = f'https://discord.com/api/v9/guilds/templates/{templatecode}'
    else:
        template = 'https://discord.com/api/v9/guilds/templates/fwjWhEcnvScd'

    while True:
        Timeinput = input(f"{Fore.GREEN}Enter your max waiting time for the servers to generate (Low term chance & rate limits if high, put 0 for fast): ")
        if Timeinput.isdigit():
            if Timeinput == "0":
                T = 0
                break
            else:
                T = random.uniform(0, Timeinput)
                break
            
        else:
            print(f"{Fore.RED}Please enter a valid number.{Fore.RESET}")


    while True:
        if enablecount == limit:
            print(f"{Fore.MAGENTA} [{Fore.RED} + {Fore.MAGENTA}] {Fore.RESET} You have reached the server limit")
            break
        else:
            time.sleep(T)
            response = requests.post(template, headers=headers, data=data)
            if response.status_code == 429:
                print(f"{Fore.MAGENTA}[{Fore.RED} + {Fore.MAGENTA}] {Fore.RESET} Rate limited, retrying in 1 sec")
                time.sleep(1)
            else:
                print(f"{Fore.MAGENTA}[{Fore.GREEN} + {Fore.MAGENTA}] {Fore.RESET} Made Server {name}")
                print(response)
                enablecount += 1
else:
    exit()
