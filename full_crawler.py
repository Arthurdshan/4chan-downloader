import progressbar
import requests as rq
import os
from commons import *

def scrap_everything(url):
    print('Getting links..')

    x = get_all(url)

    img_links = []
    webm_links = []

    for i in x:
        if i['href'].endswith('.jpg') or i['href'].endswith('.png'):
            link = "https:" + i['href']
            if link not in img_links:
                img_links.append(link)
        elif i['href'].endswith('.webm') or i['href'].endswith('.gif'):
            link = "https:" + i['href']
            if link not in webm_links:
                webm_links.append(link)
            
    print('Done.\n')
    print('Number of files found: ', len(img_links) + len(webm_links), '\n')

    choice = input('Show links? [y/_]: ').lower().strip()
    if choice == 'y':
        for l in img_links:
            print(l)
        for l in webm_links:
            print(l)
    
    dir = input('\nSelect the name of the folder to be created: ').strip()
    print()

    try:
        os.mkdir(dir)
    except OSError as exc:
        print(exc)
        return
    
    i = 0

    if webm_links:
        print('Downloading webms.. \n')
        bar = progressbar.ProgressBar(max_value = len(webm_links)).start()
        for link in webm_links:
            # Getting the last string from the split
            webm_name = link.split('/')[-1]    
            r = rq.get(link, stream = True)
            with open(dir + '/' + webm_name, 'wb+') as f:
                for chunk in r.iter_content(chunk_size = 1024 * 1024):
                    if chunk:
                        f.write(chunk)
            f.close()
            i += 1
            bar.update(i)
        bar.finish()
    
    i = 0

    if img_links:
        print('\nDownloading images.. \n')
        bar = progressbar.ProgressBar(max_value = len(img_links) + len(webm_links)).start()
        for img_link in img_links:        
            img_name = img_link.split('/')[-1]
            img_data = rq.get(img_link).content
            with open(dir + '/' + img_name + '.jpg', 'wb+') as f:
                f.write(img_data)
            f.close()
            i += 1
            bar.update(i)
        bar.finish()

    print("\nAll the files were downloaded to: ", dir)