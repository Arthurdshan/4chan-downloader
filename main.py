from commons import *
from img_crawler import *
from webm_crawler import *
from archiver import *

logo()

def main():
    url = get_url()

    print('''
    1. Download images
    2. Download webms + gifs
    3. Archive thread
    4. Exit
    ''')
    
    choice = input('Choose an option: ').strip()
    if choice == '1':
        get_images(url)
    elif choice == '2':
        get_webms(url)
    elif choice == '3':
        get_screenshot(url)
    elif choice == '4':
        exit()
    else:
        print('Invalid option.')

    choice = input('\nDo you want to use the tool again?[Y/N]: ').lower().strip()
    if choice == 'y':
        logo()
        main()
    else:
        exit()

if __name__ == '__main__':
    main()