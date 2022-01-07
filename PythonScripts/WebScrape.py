from bs4 import BeautifulSoup as bs
import requests as req
import pandas as pd
import pyodbc as db

url = "https://www.rhinohockeysiouxfalls.com/21-22-crl-winter-league-stats/"

request = req.get(url).text
soup = bs(request, "lxml")

# Database Connection Settings
serverName = "DESKTOP-8FK7M67\SQLEXPRESS"
databaseName = "RhinoHockey"
connectionString = "Driver={{SQL Server}};Server={};Database={}".format(serverName, databaseName)

# DB Operations
cnxn = db.connect(connectionString)

cursor = cnxn.cursor()

cursor.execute('''DROP TABLE IF EXISTS dbo.Test CREATE TABLE dbo.Test (Team VARCHAR(255), Wins INT, Loses INT)''')

cursor.commit()
cursor.close()

# TDOD: Properly scrap data and store to local DB.