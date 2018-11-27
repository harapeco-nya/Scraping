#任意のキーワードをgoogleで検索し、タイトル・URL・説明文をCSVファイルに出力するプログラムです

import requests
import bs4
import csv
import pandas as pd
from pandas import Series, DataFrame

list_keywd = input("何の情報を調べる？>>")
#list_keywd = ["新宿"]
resp = requests.get('https://www.google.co.jp/search?num=100&q=' + '　'.join(list_keywd))
resp.raise_for_status()

soup = bs4.BeautifulSoup(resp.text,"html.parser")
link_elem01 = soup.select(".r > a")
link_elem02 = soup.select(".s > .st")

if(len(link_elem02) <=len(link_elem01)):
    leng = len(link_elem02)
else:
    leng = len(link_elem01)

url_text = []
title_text = []
t01 = []
t02 = []
disc_text = []

for i in range(leng):
    url_text.append(link_elem01[i].get('href').replace('/url?q=', ''))
    title_text.append(link_elem01[i].get_text())
    #disc_text.append(link_elem02[i].get_text())
    t01 = link_elem02[i].get_text()
    t02 = t01.replace("\n", "")
    disc_text.append(t02.replace("\r",""))

url_text = Series(url_text)
title_text = Series(title_text)
disc_text = Series(disc_text)
result = pd.concat([title_text,disc_text,url_text], axis=1)
result.columns = ["Title", "Explanation","URL"]
print(result)
result.to_csv("output.csv")
