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