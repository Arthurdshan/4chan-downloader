from commons import *
from img_crawler import *
from webm_crawler import *
from archiver import *
from full_crawler import *

logo()

def main():
    url = get_url()

    print('''
    1. Download images
    2. Download webms and gifs
    3. Download all
    4. Archive thread
    5. Exit
    ''')
    
    choice = input('Choose an option: ').strip()
    if choice == '1':
        get_images(url)
    elif choice == '2':
        get_webms(url)
    elif choice == '3':
        scrap_everything(url)
    elif choice == '4':
        get_screenshot(url)
    elif choice == '5':
        exit()
    else:
        print('Invalid option.')

    choice = input('\nDo you want to use the tool again?[Y/N]: ').lower().strip()
    if choice == 'y':
        logo()
        main()
    else:
        print('\nByebye!')
        exit()

if __name__ == '__main__':
    main()