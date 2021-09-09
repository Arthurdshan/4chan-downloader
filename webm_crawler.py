import requests as rq
import os

from commons import *

def download_webms(links):
    dir = input('\nSelect the name of the folder to be created: ').strip()
    try:
        os.mkdir(dir)
    except:
        pass
    print('\nDownload started.\n')
    for link in links:
        # Getting the last string from the split
        webm_name = link.split('/')[-1]    
        print('Downloading: %s' %webm_name)
        r = rq.get(link, stream = True)
        with open(dir + '/' + webm_name, 'wb+') as f:
            for chunk in r.iter_content(chunk_size = 1024 * 1024):
                if chunk:
                    f.write(chunk)
        print('Done.\n')
    print("All webms/gifs from the link were downloaded to: ", dir)

def get_webms(url):
    print('Getting webms link..')

    x = get_all(url)
    links = []

    for i in x:
        if i['href'].endswith('webm') or i['href'].endswith('gif'):
            link = "https:" + i['href']
            if link not in links:
                links.append(link)        
    
    print('Number of webms/gifs found: ', len(links), '\n')
    
    choice = input('Show links? [y/_]: ').lower().strip()
    if choice == 'y':
        for l in links:
            print(l)
    
    download_webms(links)