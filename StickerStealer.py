import PySimpleGUI as sg 
import requests
from bs4 import BeautifulSoup

layout = [  [sg.Text("Insert Sticker URL:")],
            [sg.Input()],
            [sg.Button('Ok')] ]

window = sg.Window('Window Title', layout)


event, values = window.read()

# Do something with the information gathered
def main(link):
    """MainFunc"""
    #Get Website Code
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
    #Download Every Images
    img_num = 0
    for i in url_list:
        r = requests.get(i)
        img_num += 1
        with open(str(img_num)+".png", "wb") as file:
            file.write(r.content)
main(values[0])

window.close()