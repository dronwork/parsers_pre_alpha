# Python 3.5
import requests
from bs4 import BeautifulSoup

def get_html(url):
    resp = requests.get(url)
    return resp.text

def get_data(html):
    sp = BeautifulSoup(html, 'lxml')
    h1 = sp.find('div', id='home-welcome').find('header').find('h1').text
    return h1

def main():
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))

if __name__ == '__main__':
    main()










