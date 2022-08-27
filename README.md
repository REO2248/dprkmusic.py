# dprkmusic.py
This library gets dprk musics data from dprk sites

[조선어](README_KO.md)
[日本語](README_JP.md)

## uriminzokkiri

Get musics from uriminzokkiri.com

[Music](http://uriminzokkiri.com/index.php?ptype=cmusic)

### Example

```py
import dprkmusic.uriminzokkiri as uriminzokkiri

s = uriminzokkiri.search("우리는 당신밖에 모른다")
for m in s.lists:
    music = m.music()
    print(music.title) # music title
    print(music.no) # music No
    print(music.url) # music url
    print(music.imgsrc) # score image url
    print(music.src) # audio url
    print("\n")
```
### Reference

#### functions
##### def get_music(no: int)
get music class from music No

Arguements:

no: int

Return: uriminzokkiri.Music

##### def search(skey: str = "" , lang: str = "kor")
search music from keyword

Arguments:

skey: str = ""

lang: str = "kor"

Return: uriminzokkiri.Search or uriminzokkiri.SearchOtherLang

#### class uriminzokkiri.Music
Music 
##### Parameters
- no:int : music No
##### Attributes
title (str) : music title

title_html (str) : title with html tags

title_bold (str) : title with bold tags

no (int) : music No

url (str) : music url

src (str) : audio data url

imgsrc (str) : score image url

feels (list[Music.Feel])

##### class uriminzokkiri.Music.Feel

Feel

name (str) : feel poster's name

address (str) : feel poster's address

job (str) : feel poster's job

reg_date (str) : feel registration date (YYYY-MM-DD)

reg_time (str) : feel registration time (HH:MM:SS)

contents (str) : feel contents

contents_html (str) : feel contents with html tags

contents_bold (str) : feel contents with bold tags

title (str) : feel title

title_html (str) : feel title with html tags

title_bold (str) : feel title with bold tags

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

#### class uriminzokkiri.Search
Search (Korean)

##### Parameters
-skey:str = ""  : search keyword

-no_pagination:int = 1 : page number

-num_per_page:int = 40 : number of music per page

-orderby:str = "reg_date desc" : order by


##### Attributes
counts_music (int) : number of music

lists (list[Search.Music]) : music list

#### class uriminzokkiri.Search.Music
Search.Music
##### Attributes
no (int) : music No

title (str) : music title

title_html (str) : music title with html tags

title_bold (str) : music title with bold tags

sub_title (str)

reg_date (str) : registration date (YYYY-MM-DD)

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

music() : get Music object of this music (Return type : uriminzokkiri.Music)



#### class uriminzokkiri.SearchOtherLang
Search

##### Parameters
-skey:str = ""  : search keyword

-no_pagination:int = 1 : page number

-num_per_page:int = 40 : number of music per page

-orderby:str = "reg_date desc" : order by

-lang:str = "eng" : language


##### Attributes
counts_music (int) : number of music

lists (list[SearchOtherLang.Music]) : music list

#### class uriminzokkiri.SearchOtherLang.Music
SearchOtherLang.Music
##### Attributes
no (int) : music No

title (str) : music title

title_html (str) : music title with html tags

title_bold (str) : music title with bold tags

sub_title (str)

reg_date (str) : registration date (YYYY-MM-DD)

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

music() : get Music object of this music (Return type : uriminzokkiri.Music)

