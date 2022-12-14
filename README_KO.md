# dprkmusic.py
조선민주주의인민공화국의 싸이트에서 음악을 취득하는 서고프로그람

[English](README.md)
[日本語](README_JP.md)

## uriminzokkiri

uriminzokkiri.com 에서 음악을 취득하다

[음악마당](http://uriminzokkiri.com/index.php?ptype=cmusic)

### 례

```py
import dprkmusic.uriminzokkiri as uriminzokkiri

s = uriminzokkiri.search("우리는 당신밖에 모른다")
for m in s.lists:
    music = m.music()
    print(music.title) # 음악 제목
    print(music.no) # 음악 번호
    print(music.url) # 음악 URL
    print(music.imgsrc) # 악보화상URL
    print(music.src) # 음성URL
    print("\n")
```
### 참고자료

#### 함수
##### def get_music(no: int)
Music클라스를 음악번호로 취득한다

인수:

no: int

반환: uriminzokkiri.Music

##### def search(skey: str = "" , lang: str = "kor")
search music from keyword

인수:

skey: str = ""

lang: str = "kor"

반환: uriminzokkiri.Search or uriminzokkiri.SearchOtherLang

#### 클라스 uriminzokkiri.Music
음악
##### 인수
- no:int : 음악 번호
##### 속성
title (str) : 음악 제목

title_html (str) : 음악 제목(HTML꼬리표)

title_bold (str) : 음악 제목(굵은 꼬리표)

no (int) : 음악 번호

url (str) : 음악 URL

src (str) : 음성 URL

imgsrc (str) : 악보화상 URL

feels (list[Music.Feel]) : 감상글 목록

##### 클라스 uriminzokkiri.Music.Feel

감상글

name (str) : 감상글등록자 이름

address (str) : 감상글등록자 주소

job (str) : 감상글등록자 직업

reg_date (str) : 감상글등록일자 (YYYY-MM-DD)

reg_time (str) : 감상글등록시간 (HH:MM:SS)

contents (str) : 감상글내용

contents_html (str) : 감상글내용(HTML꼬리표)

contents_bold (str) : 감상글내용(굵은 꼬리표)

title (str) : 음악 제목

title_html (str) : 음악 제목(HTML꼬리표)

title_bold (str) : 음악 제목(굵은 꼬리표)

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

#### 클라스 uriminzokkiri.Search
검색 (조선어)

##### 인수
-skey:str = ""  : 검색어

-no_pagination:int = 1 : 페지 번호

-num_per_page:int = 40 : 페지당 개수

-orderby:str = "reg_date desc" : 정렬


##### 속성
counts_music (int) : 검색결과 음악개수

lists (list[Search.Music]) : 검색결과 음악목록

#### 클라스 uriminzokkiri.Search.Music
Search.Music
##### 속성
no (int) : 음악 번호

title (str) : 음악 제목

title_html (str) : 음악 제목(HTML꼬리표)

title_bold (str) : 음악 제목(굵은 꼬리표)

sub_title (str)

reg_date (str) : 음악등록일자 (YYYY-MM-DD)

categ1 (int)

categ2 (int)

categ3 (int)

categ3_name (str) : 음악 범주

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

music() : uriminzokkiri.Music클라스의 사례를 반환하다



#### 클라스 uriminzokkiri.SearchOtherLang
Search

##### 인수
-skey:str = ""  : 검색어

-no_pagination:int = 1 : 페지 번호

-num_per_page:int = 40 : 페지당 개수

-orderby:str = "reg_date desc" : 정렬

-lang:str = "eng" : 검색 언어


##### 속성
counts_music (int) : 검색결과 음악개수

lists (list[SearchOtherLang.Music]) : 검색결과 음악목록

#### 클라스 uriminzokkiri.SearchOtherLang.Music
SearchOtherLang.Music
##### 속성
no (int) : 음악 번호

title (str) : 음악 제목

title_html (str) : 음악 제목(HTML꼬리표)

title_bold (str) : 음악 제목(굵은 꼬리표)

sub_title (str)

reg_date (str) : 음악등록일자 (YYYY-MM-DD)

categ1 (int)

categ2 (int)

categ3 (int)

categ3_name (str) : 음악 범주

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

music() : uriminzokkiri.Music클라스의 사례를 반환하다

