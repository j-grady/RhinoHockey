from bs4 import BeautifulSoup
import requests as req
import pandas as pd

url = "https://www.rhinohockeysiouxfalls.com/21-22-crl-winter-league-stats/"

request = req.get(url).text

print(request)

# TDOD: Properly scrap data and store to local DB.