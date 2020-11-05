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

index_html = html_statistics.tbody.find_all("tr")

#print(len(index_html[0]))
#print(len(index_html))

rows = []
contents = []
counter = 0

while counter < len(index_html):
    for item in index_html[counter]:
        contents.append(item.text)
    else:
        rows.append(contents)
        contents = []
    counter += 1
#print(row)

table = pd.DataFrame(data = rows, columns = header)
print(table)

while True:
    report = input('Do you want to generate an CSV (.csv) report containing these information? [y/n] ')
    if report == 'y':
        table.to_csv(f'{ticker}.csv', index = False)
        print('The document was generated in the current directory')
        quit()
    elif report == 'n':
        quit()
    else:
        print('This is not a valid choice')