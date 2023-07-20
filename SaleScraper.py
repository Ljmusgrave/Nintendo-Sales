import pandas as pd
from bs4 import BeautifulSoup
import requests

products = []
current_prices = []
regular_prices = []
discounts = []

f = requests.get('https://www.nintendo.com/store/sales-and-deals/')
soup = BeautifulSoup(f.text, features="html.parser")
products_class = "Headingstyles__StyledH-sc-s17bth-0 vsVuC Textstyles__StyledTitle-sc-w55g5t-0 lcSxww tilestyles__Title-sc-eg7slj-2 bKKnvO"

for i in soup.findAll("div", {"class": "BasicTilestyles__Info-sc-1bsju6x-6 ktXPHv"}):
    products.append((i.find("h3", {"class": products_class})).text)

    price1 = (i.find("span", {"class": "Pricestyles__SalePrice-sc-1f0n8u6-4 ggGKyn"})).text
    current_prices.append(price1.replace("Current Price:", ""))

    price2 = (i.find("span", {"class": "Pricestyles__MSRP-sc-1f0n8u6-5 hQYifm"})).text
    regular_prices.append(price2.replace("Regular Price:", ""))

    discounts.append((i.find("div", {"class": "Pricestyles__SalesTag-sc-1f0n8u6-3 eMpMVA"})).text)

df = pd.DataFrame(
    {"Product": products,
     "Current Price": current_prices,
     "Regular Price": regular_prices,
     "% Discount": discounts
     })

df.to_csv("nintendo_sales.csv", index=False, encoding="utf8")
