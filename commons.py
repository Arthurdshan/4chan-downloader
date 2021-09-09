from bs4 import BeautifulSoup
import requests as rq

def logo():
    print('''
           ___      _                  ______                    _                 _           
          /   |    | |                 |  _  \                  | |               | |          
         / /| | ___| |__   __ _ _ __   | | | |_____      ___ __ | | ___   __ _  __| | ___ _ __ 
        / /_| |/ __| '_ \ / _` | '_ \  | | | / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
        \___  | (__| | | | (_| | | | | | |/ / (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
            |_/\___|_| |_|\__,_|_| |_| |___/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                                       
    ''')

def verify_url(url) -> bool:
    # If using Linux, switch the Windows parenthesis for: (X11; Ubuntu; Linux x86_64; rv:91.0)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }
    if rq.get(url, headers=header).status_code == 404:
        print('Invalid URL.')
        return False
    else:
        return True

def get_url():
    verifier_str_1 = "https://boards.4chan.org"
    verifier_str_2 = "https://boards.4channel.org"
    while 1:
        url = input('Insert the thread URL: ').strip()
        url_checker_1 = url[:len(verifier_str_1)]
        url_checker_2 = url[:len(verifier_str_2)]
        if url_checker_1 != verifier_str_1 and url_checker_2 != verifier_str_2:    
            print('Not a 4chan URL.')
            continue
        elif not verify_url(url):
            continue
        else:
            break
    return url

def get_all(url):
    r = rq.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    x = soup.find_all('a')
    return x