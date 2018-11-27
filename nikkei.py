from bs4 import BeautifulSoup
import requests

url ="https://www.nikkei.com/markets/kabu/"

resp = requests.get(url)
c = resp.content
soup = BeautifulSoup(c,"html.parser")

print(soup.select_one("#CONTENTS_LOCAL > div.cmn-lc_menu").text)
#print(soup.select_one("#CONTENTS_MARROW > div.mk-top_stock_average.cmn-clearfix > div.cmn-clearfix > div.mkc-guidepost > div.mkc-prices > span.mkc-stock_prices").text)
