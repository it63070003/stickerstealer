import PySimpleGUI as sg 
import requests
from bs4 import BeautifulSoup
import os

layout = [  [sg.Text("Insert Sticker URL:")],
            [sg.Input(key='stickerlink')],
            [sg.Text("Path:")],
            [sg.Input(key='path'), sg.FolderBrowse()],
            [sg.Button('Ok')]]

window = sg.Window('Window Title', layout)


event, values = window.read()

# Do something with the information gathered
def main(link, path):
    """MainFunc"""
    #Get Website Code
    link = link.split("/")
    for i in link:
        if i.isnumeric():
            sticker_id = i
            break
    link = "https://store.line.me/stickershop/product/" + sticker_id + "/en"
    web_code = requests.get(link).content
    soup = BeautifulSoup(web_code, "html.parser")
    #Find all Sticker Images
    url_list = list(soup.find_all("span", class_="mdCMN09Image FnPreview"))
    for i in range(len(url_list)):
        url_list[i] = str(url_list[i])
        start = url_list[i].index("url") + 4
        stop = url_list[i].index(";")
        url_list[i] = url_list[i][start:stop]
    #get sticker name and assign new path
    sticker_name = soup.title.text
    back_index = sticker_name.index(" – LINE stickers | LINE STORE")
    sticker_name = sticker_name[:back_index]
    for i in (":", "\\", "/", "*", "?", "\"", ">", "<", "|"):
        sticker_name = sticker_name.replace(i, "")
    newpath =path+ "\\" + sticker_name + "\\"
    #Download Every Images
    img_num = 0
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for i in url_list:
        r = requests.get(i)
        img_num += 1
        with open(newpath+str(img_num)+"_"+sticker_id+".jpg", "wb") as file:
            file.write(r.content)
main(values['stickerlink'], values['path'])

window.close()