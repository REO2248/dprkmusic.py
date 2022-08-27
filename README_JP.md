# dprkmusic.py
朝鮮民主主義人民共和国のサイトから音楽を取得するライブラリ

[English](README.md)
[조선어](README_KO.md)


## uriminzokkiri

uriminzokkiri.com から音楽を取得する

[音楽の庭](http://uriminzokkiri.com/index.php?ptype=cmusic)

### 例

```py
import dprkmusic.uriminzokkiri as uriminzokkiri

s = uriminzokkiri.Search("우리는 당신밖에 모른다")
for m in s.lists:
    music = m.music()
    print(music.title) # 音楽タイトル
    print(music.no) # 音楽No
    print(music.url) # 音楽url
    print(music.imgsrc) # 楽譜画像url
    print(music.src) # 音声url
    print("\n")
```
### リファレンス

#### 関数
##### def get_music(no: int)
Musicクラスを音楽Noで取得する

引数:

no: int

返還: uriminzokkiri.Music

##### def search(skey: str = "" , lang: str = "kor")
search music from keyword

引数:

skey: str = ""

lang: str = "kor"

返還: uriminzokkiri.Search or uriminzokkiri.SearchOtherLang

#### クラス uriminzokkiri.Music
音楽 
##### 引数
- no:int : 音楽No
##### 属性
title (str) : 音楽タイトル

title_html (str) : 音楽タイトルHTMLタグ付き

title_bold (str) : 音楽タイトル太字タグ付き

no (int) : 音楽No

url (str) : 音楽url

src (str) : 音声url

imgsrc (str) : 楽譜画像url

feels (list[Music.Feel]) : 感想のリスト

##### クラス uriminzokkiri.Music.Feel

感想

name (str) : 投稿者名前

address (str) : 投稿者住所

job (str) : 投稿者職業

reg_date (str) : 投稿日(YYYY-MM-DD)

reg_time (str) : 投稿時(HH:MM:SS)

contents (str) : 感想内容

contents_html (str) : 感想内容HTMLタグ付き

contents_bold (str) : 感想内容太字タグ付き

title (str) : 音楽タイトル

title_html (str) : 音楽タイトルHTMLタグ付き

title_bold (str) : 音楽タイトル太字タグ付き

bon_send (bool)

categ1 (int)

categ2 (int)

categ3 (int)

email (str)

email_isview (bool)

emoticon (int)

file_name (str)

firstpage_isview (bool)

hit (int)

ip (str)

is_view (bool)

listpage_isview (bool)

main_flag (int)

new_file_name (str)

new_no (int)

no (str)

view_flag (bool)

#### クラス uriminzokkiri.Search
検索 (朝鮮語)

##### 引数
-skey:str = ""  : 検索キーワード

-no_pagination:int = 1 : ページ番号

-num_per_page:int = 40 : 1ページあたりの表示件数

-orderby:str = "reg_date desc" : 検索結果の並び順


##### 属性
counts_music (int) : 検索結果の件数

lists (list[Search.Music]) : 検索結果のリスト

#### クラス uriminzokkiri.Search.Music
Search.Music
##### 属性
no (int) : 音楽No

title (str) : 音楽タイトル

title_html (str) : 音楽タイトルHTMLタグ付き

title_bold (str) : 音楽タイトル太字タグ付き

sub_title (str)

reg_date (str) : 投稿日(YYYY-MM-DD)

categ1 (int)

categ2 (int)

categ3 (int)

categ3_name (str) : カテゴリ名称

file_name (str)

firstpage_isview (str)

hit (int)

is_new (bool)

is_view (bool)

key_word (str)

lang_kind (str)

listpage_isview (bool)

old_file_name (str)

special_no (int)

summary (str)

view_order (int)


##### Methods

music() : uriminzokkiri.Musicクラスのインスタンスを返す



#### クラス uriminzokkiri.SearchOtherLang
Search

##### 引数
-skey:str = ""  : 検索キーワード

-no_pagination:int = 1 : ページ番号

-num_per_page:int = 40 : 1ページあたりの表示件数

-orderby:str = "reg_date desc" : 検索結果の並び順

-lang:str = "eng" : 検索言語


##### 属性
counts_music (int) : 検索結果の件数

lists (list[SearchOtherLang.Music]) : 検索結果のリスト

#### クラス uriminzokkiri.SearchOtherLang.Music
SearchOtherLang.Music
##### 属性
no (int) : 音楽No

title (str) : 音楽タイトル

title_html (str) : 音楽タイトルHTMLタグ付き

title_bold (str) : 音楽タイトル太字タグ付き

sub_title (str)

reg_date (str) : 投稿日(YYYY-MM-DD)

categ1 (int)

categ2 (int)

categ3 (int)

categ3_name (str) : category name

file_name (str)

firstpage_isview (str)

hit (int)

is_new (bool)

is_view (bool)

key_word (str)

lang_kind (str)

listpage_isview (bool)

old_file_name (str)

special_no (int)

summary (str)

view_order (int)


##### Methods

music() : uriminzokkiri.Musicクラスのインスタンスを返す

