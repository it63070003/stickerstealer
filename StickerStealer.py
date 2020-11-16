"""Sticker Stealer"""
import requests
from bs4 import BeautifulSoup


def main():
    """MainFunc"""
    #Get Website Code
    link = input("Insert Sticker URL:")
    web_code = requests.get(link).content
    soup = BeautifulSoup(web_code, "html.parser")
    #Find all Sticker Images
    url_list = list(soup.find_all("span", class_="mdCMN09Image FnPreview"))
    for i in range(len(url_list)):
        url_list[i] = str(url_list[i])
        start = url_list[i].index("url") + 4
        stop = url_list[i].index(";")
        url_list[i] = url_list[i][start:stop]
    #url_list : Sticker Image URLs
    image_url = "URL" ##URL is use image URL
    r = requests.get(image_url)
    with open("image.png", "wb") as file:
        file.write(r.content)
    #Download Every Images



main()