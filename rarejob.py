#Webサイト上の表を取得し、Seriesで再構成して表示するスクリプトです

from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import Series, DataFrame

url = "https://www.rarejob.com/lesson/material/conversation/advanced/"

result = requests.get(url)
c = result.content
soup = BeautifulSoup(c,"html.parser")
summary = soup.find('div',{'class':'content_wrap'})
tables = summary.find_all('table')

data = []
rows = tables[0].find_all("tr")  #tableはひとつしかない
for tr in rows:
    cols = tr.find_all("td")
    for td in cols:
        text = td.find(text=True)
        #print(text)
        data.append(text)

exp = []
topic = []
index = 0
for item in data:
    if index % 2 == 0:
        topic.append(item)
        exp.append(data[index+1])
    index += 1

topic = Series(topic)
exp = Series(exp)
web_df = pd.concat([topic,exp],axis=1)
web_df.columns = ["Topic","Expressions"]

#web_df.to_csv("output.csv")
print(web_df)
