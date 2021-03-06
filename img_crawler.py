import progressbar
import requests as rq
import os

from commons import *

def download_images(links):
    dir = input('\nSelect the name of the folder to be created: ').strip()
    try:
        os.mkdir(dir)
    except OSError as exc:
        print(exc)
        return
    bar = progressbar.ProgressBar(max_value = len(links)).start()
    for index, img_link in enumerate(links):        
        img_data = rq.get(img_link).content
        with open(dir + '/' + str(index + 1) + '.jpg', 'wb+') as f:
            f.write(img_data)
        f.close()
        bar.update(index + 1)
    bar.finish()
    print("\nAll images from the link were downloaded to: ", dir)

def get_images(url):    
    print('\nGetting images link..\n')
    
    x = get_all(url)

    links = []
    for i in x:
        if i['href'].endswith('.jpg') or i['href'].endswith('.png'):
            link = "https:" + i['href']
            if link not in links:
                links.append(link)

    print('Done.\n')
    print('Number of images found: ', len(links), '\n')
    
    choice = input('Show links? [y/_]: ').lower().strip()
    if choice == 'y':
        for l in links:
            print(l)
    
    download_images(links)