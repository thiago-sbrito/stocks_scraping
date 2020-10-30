import requests
from bs4 import BeautifulSoup
import pandas as pd

ticker = input("Insert a ticker of a specific brazilian asset (B3-listed): ").upper()
url = f"https://finance.yahoo.com/quote/{ticker}.SA"

request = requests.get(url).text
html = BeautifulSoup(request, "lxml")

try:    
    asset_name = html.find("h1", class_="D(ib) Fz(18px)").text
    price_var = html.find("div", class_="D(ib) Mend(20px)")
except AttributeError:
    print("Invalid ticker")
    quit()

price = price_var.contents[0].text
variation = price_var.contents[1].text 
print(f"\nAsset name: {asset_name}\n"
    f"Price: {price} BRL\n"
    f"Today's variation: {variation}\n"
)

url_statistics = f"https://finance.yahoo.com/quote/{ticker}.SA/key-statistics"
request_statistics = requests.get(url_statistics).text
html_statistics = BeautifulSoup(request_statistics, 'lxml')

header_html = html_statistics.table.find_all("th")
header = []
for column in header_html:
    header.append(column.text)
else:
    header[0] = 'Multiple'
print(header)

index_html = html_statistics.tbody.find_all("tr")
for i in index_html:
   print(i.get_text(separator = ','))

#header vai ser utilizado para ser as columns do pandas
#In [51]: pd.DataFrame(data, columns=['C', 'A', 'B'])
#Out[51]: 
#          C  A    B
#0  b'Hello'  1  2.0
#1  b'World'  2  3.0