import aiohttp
import asyncio
from bs4 import BeautifulSoup

url = "http://uriminzokkiri.com/index.php?ptype=cmusic"

endpoint = "http://uriminzokkiri.com/"

langs = [
    "kor", # 조선어 (Korean)
    "eng", # English
    "rus", # Русский (Russian)
    "chn", # 中国语 (Chinese)
    "jpn", # 日本語 (Japanese) (there are no music in japanese page)
]

class Music: # Music class from music number
    title = ""
    title_html = ""
    title_bold = ""
    no = 0
    url = ""
    src = ""
    imgsrc = ""
    feels = []

    def __init__(self, no:int):
        self.no = no
        asyncio.run(self.__fetch())

    async def __fetch(self, no:int):
        async with aiohttp.ClientSession() as session:
            async with session.post(endpoint+"index.php?ptype=cmusic&mtype=play",data={"no":str(no)+"pl"}) as r:
                __soup = BeautifulSoup(__r.json()[0]["title"], "html.parser")
                self.title = __soup.get_text()
                self.title_html = __r.json()[0]["title"]
                __strong_word__ = __soup.find("span", class_='strong_word')
                try:
                    __soup.find("span", class_='strong_word').replace_with("**"+__strong_word__.text+"**")
                    self.title_bold = __soup.get_text()
                except:
                    self.title_bold = self.title
                self.no = int(__r.json()[0]["no"])
                self.url = endpoint + "index.php?ptype=cmusic&mtype=view&no=" + str(self.no)
                self.src = endpoint + __r.json()[0]["src"].strip("./")
                self.imgsrc = endpoint + __r.json()[0]["imgsrc"].strip("./")
                self.feels = []
                try:
                    for feel in __r.json()[0]["feels"]:
                        self.feels.append(self.Feel(feel))
                except:
                    pass
    
    def __str__(self):
        return self.title
    
    class Feel:
        def __init__(self, feel):
            self.address = feel["address"]
            self.bon_send = feel["bon_send"]
            self.categ1 = feel["categ1"]
            self.categ2 = feel["categ2"]
            self.categ3 = feel["categ3"]
            self.contents_html = feel["contents"]
            __soup = BeautifulSoup(feel["contents"], "html.parser")
            self.contents = __soup.get_text()
            __strong_word__ = __soup.find("span", class_='strong_word')
            try:
                __soup.find("span", class_='strong_word').replace_with("**"+__strong_word__.text+"**")
                self.contents_bold = __soup.get_text()
            except:
                self.contents_bold = self.contents
            self.email = feel["email"]
            self.email_isview = feel["email_isview"]
            self.emoticon = feel["emoticon"]
            self.file_name = feel["file_name"]
            self.firstpage_isview = feel["firstpage_isview"]
            self.hit = feel["hit"]
            self.ip = feel["ip"]
            self.is_view = feel["is_view"]
            self.job = feel["job"]
            self.listpage_isview = feel["listpage_isview"]
            self.main_flag = feel["main_flag"]
            self.name = feel["name"]
            self.new_file_name = feel["new_file_name"]
            self.new_no = feel["new_no"]
            self.no = feel["no"]
            self.reg_date = feel["reg_date"]
            self.reg_time = feel["reg_time"]
            self.title_html = feel["title"]
            __soup = BeautifulSoup(feel["title"], "html.parser")
            self.title = __soup.get_text()
            __strong_word__ = __soup.find("span", class_='strong_word')
            try:
                __soup.find("span", class_='strong_word').replace_with("**"+__strong_word__.text+"**")
                self.title_bold = __soup.get_text()
            except:
                self.title_bold = self.title
            self.view_flag = feel["view_flag"]
        def __str__(self):
            return self.name


class Search: # Search from search keyword
    def __init__(self, skey:str, no_pagination:int=1, num_per_page:int=40, orderby:str="reg_date desc"):
        asyncio.run(self.__fetch(skey, no_pagination, num_per_page, orderby))

    async def __fetch(self, skey:str, no_pagination:int=1, num_per_page:int=40, orderby:str="reg_date desc"):
        __data = {
            "no_pagination":str(no_pagination),
            "num_per_page":str(num_per_page),
            "skey":skey,
            "orderby":orderby
        }
        self.skey = skey
        async with aiohttp.ClientSession() as session:
            async with session.post(endpoint+"index.php?ptype=cmusic&mtype=writeList",data=__data) as r:
                self.counts_music = r.json()["counts_music"]
                self.lists = []
                for music in r.json()["lists"]:
                    self.lists.append(self.Music(music))
    
    def __str__(self):
        return self.skey

    class Music:
        def __init__(self,music):
            self.no = music["no"]
            self.title_html = music["title"]
            __soup = BeautifulSoup(music["title"], "html.parser")
            self.title = __soup.get_text()
            __strong_word__ = __soup.find("span", class_='strong_word')
            try:
                __soup.find("span", class_='strong_word').replace_with("**"+__strong_word__.text+"**")
                self.title_bold = __soup.get_text()
            except:
                self.title_bold = self.title
            self.sub_title = music["sub_title"]
            self.reg_date = music["reg_date"]
            self.categ1 = int(music["categ1"])
            self.categ2 = int(music["categ2"])
            self.categ3 = int(music["categ3"])
            self.categ3_name = music["categ3_name"]
            self.file_name = music["file_name"]
            self.firstpage_isview = music["firstpage_isview"]
            self.hit = int(music["hit"])
            self.is_new = music["is_new"]
            self.is_view = music["is_view"]
            self.key_word = music["key_word"]
            self.lang_kind = music["lang_kind"]
            self.listpage_isview = music["listpage_isview"]
            self.old_filename = music["old_filename"]
            self.special_no = int(music["special_no"])
            self.summary = music["summary"]
            self.view_order = str(music["view_order"])
        def __str__(self):
            return self.title
        def music(self):
            return Music(self.no)


class SearchOtherLang: # Search from search keyword in other language
    def __init__(self, skey:str, no_pagination:int=1, num_per_page:int=40, orderby:str="reg_date desc", lang:str="eng"):
        asyncio.run(self.__fetch(skey, no_pagination, num_per_page, orderby, lang))
    
    async def __fetch(self, skey:str, no_pagination:int=1, num_per_page:int=40, orderby:str="reg_date desc", lang:str="eng"):
        __data = {
            "no_pagination":str(no_pagination),
            "num_per_page":str(num_per_page),
            "skey":skey,
            "orderby":orderby,
            "lang":lang
        }
        self.skey = skey
        async with aiohttp.ClientSession() as session:
            async with session.post(endpoint+"index.php?ptype=cmusic&mtype=writeList",data=__data) as r:
                self.counts_music = r.json()["counts_music"]
                self.lists = []
                for music in r.json()["lists"]:
                    self.lists.append(self.Music(music))
    
    def __str__(self):
        return self.skey

    class Music:
        def __init__(self,music):
            self.no = music["no"]
            self.title_html = music["title"]
            __soup = BeautifulSoup(music["title"], "html.parser")
            self.title = __soup.get_text()
            __strong_word__ = __soup.find("span", class_='strong_word')
            try:
                __soup.find("span", class_='strong_word').replace_with("**"+__strong_word__.text+"**")
                self.title_bold = __soup.get_text()
            except:
                self.title_bold = self.title
            self.sub_title = music["sub_title"]
            self.reg_date = music["reg_date"]
            self.categ1 = int(music["categ1"])
            self.categ2 = int(music["categ2"])
            self.categ3 = int(music["categ3"])
            self.categ3_name = music["categ3_name"]
            self.file_name = music["file_name"]
            self.firstpage_isview = music["firstpage_isview"]
            self.hit = int(music["hit"])
            self.is_new = music["is_new"]
            self.is_view = music["is_view"]
            self.key_word = music["key_word"]
            self.lang_kind = music["lang_kind"]
            self.listpage_isview = music["listpage_isview"]
            self.old_filename = music["old_filename"]
            self.special_no = int(music["special_no"])
            self.summary = music["summary"]
            self.view_order = str(music["view_order"])
        def __str__(self):
            return self.title
        def music(self):
            return Music(self.no)



async def get_music(no:int):
    return Music(no)

async def search(skey:str, lang:str="kor"):
    if lang == "kor":
        counts =  Search(skey, 1, 1).counts_music # search how many music in search keyword
        return Search(skey, 1, counts)
    else:
        counts =  SearchOtherLang(skey, 1, 1, lang = lang).counts_music # same as above
        return SearchOtherLang(skey, 1, counts, lang = lang)

