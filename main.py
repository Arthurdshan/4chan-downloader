from commons import *
from img_crawler import *
from webm_crawler import *

logo()

def main():
    url = get_url()

    print('''
    1. Download images
    2. Download webms + gifs
    ''')
    
    choice = input('Choose an option from above: ').strip()
    if choice == '1':
        get_images(url)
    elif choice == '2':
        get_webms(url)
    else:
        print('Invalid option.')

    choice = input('Do you want to use the tool again?[Y/N]: ').lower().strip()
    if choice == 'y':
        logo()
        main()
    else:
        exit()

if __name__ == '__main__':
    main()