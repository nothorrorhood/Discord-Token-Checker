import requests, sys, colorama
from colorama import Fore

FILE_NAME = sys.argv[1]
TOKENS = []

def LogValid(txt:str):
    return print(f"[{Fore.GREEN}+{Fore.RESET}] {txt}")

def LogInvalid(txt:str):
    return print(f"[{Fore.RED}+{Fore.RESET}] {txt}")

def check_token(token:str):
    '''
    make a post request and get the status code and return a bool (status code will define if the authorization token is valid)
    '''
    headers = {'authorization': token}
    r = requests.get(url='https://canary.discordapp.com/api/v8/users/@me', headers=headers)

    if r.status_code == 200:
        return True
    else:
        return False


def main():
    read_file = open(FILE_NAME)
    for line in read_file:
        TOKENS.append(line.strip('\n'))
    
    for tken in TOKENS:
        if check_token(tken):
            LogValid(f"Valid token ~> {tken}")
        else:
            LogInvalid("Invalid token ~> {tken}")

    


        




if __name__ == "__main__":
    main()