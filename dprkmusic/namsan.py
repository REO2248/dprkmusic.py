import requests
import xmltodict
from bs4 import BeautifulSoup

endpoint = "http://www.gpsh.edu.kp/"

langs = [
    "ko" # 조선어 (Korean)
    "en" # English
    "cn" # 中国语 (Chinese)
]

class Item:
    def __init__(self, item):
        self.type = item["type"]
        self.id = item["id"]
        self.label = item["label"]
        self.visible = item["visible"]
        self.manage = item["manage"]
        self.inspector = item["inspector"]
    
    def songs(self):
        if self.type == "catalogue":
            return loadsongs(self.id)
        else:
            return []

    def song(self):
        if self.type == "song":
            return Song(self.id)
        else:
            return None

    def __str__(self):
        return self.label

class Song:
    def __init__(self, id:int):
        self.id = id
        self.url = endpoint + "index.php/ko/rmenjoy/view?id=" + str(self.id)
        __soup = BeautifulSoup(requests.get(self.url).text, "html.parser")
        for i in __soup.select("br"):
            i.replace_with("\n")
        self.title = __soup.find("h3").text
        __strongword = __soup.find("h3").find("b")
        try:
            __soup.find("h3").find("b").replace_with("**"+__strongword.text+"**")
            self.title_bold = __soup.find("h3").text
        except:
            self.title_bold = self.title
        try:
            self.meta = __soup.find("div", {"class": "acm-td meta"}).text
        except:
            self.meta = ""
        try:
            self.lyrics = __soup.find("td").text
        except:
            self.lyrics = ""
        try:
            self.img = endpoint +  __soup.find(class_="akbo")["src"].strip("/./")
        except:
            self.img = ""
        try:
            self.audio = endpoint +  __soup.find("source")["src"].strip("/./")
        except:
            self.audio = ""


def loadsongs(catcode:str=""):
    __r = requests.post(endpoint+"index.php/ko/rmenjoy/loadsongs",data={"catcode":catcode})
    __dict = xmltodict.parse(__r.text)
    __return = []
    for item in __dict["result"]["item"]:
        __return.append(Item(item))
    return __return

def searchsong(keyword:str):
    __r = requests.post(endpoint+"index.php/ko/rmenjoy/searchsong",data={"keyword":keyword})
    __dict = xmltodict.parse(__r.text)
    __return = []
    for item in __dict["result"]["item"]:
        __return.append(Item(item))
    return __return