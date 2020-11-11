"""Sticker Stealer"""
import requests


def main():
    """MainFunc"""
    url = input()
    web_code = requests.get(url)
    print(web_code.content)



main()
