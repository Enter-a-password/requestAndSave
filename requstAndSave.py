from threading import Thread

from urllib.request import urlopen
from os.path import basename
from webbrowser import open as wbopen
thisFileName = basename(__file__)
filepath = f'{__file__[:-int(len(thisFileName) + 1)]}'

url = input("Url: ")

try:
    with urlopen(url) as response:
        html = response.read()
        f = open('responce.html', 'wb')
        f.write(html)
        f.close()
except Exception as e:
    print(f'An error occured: {e}')
    input("Press enter to exit")
    exit()
