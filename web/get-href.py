#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import argparse


def parser():
    # Get URL
    parser = argparse.ArgumentParser(description="Find unique links on a website")
    parser.add_argument('URL', type=str, nargs=1, help='URL')
    args = parser.parse_args()
    return args.URL[0]


def main():
    url = parser()
    get_url = requests.get(url)

    soup = BeautifulSoup(get_url.text, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))
    for link in soup.find_all('link'):
        print(link.get('href'))


if __name__ == '__main__':
    main()
