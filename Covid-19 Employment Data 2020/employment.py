import pandas as pd
import numpy as np

#load the employment data for each employment excel file
employment_data = pd.read_excel('Covid-19 Employment Data 2020/allhlcn20.xlsx')
employment_data2 = pd.read_excel('Covid-19 Employment Data 2020/allhlcn201.xlsx')
employment_data3 = pd.read_excel('Covid-19 Employment Data 2020/allhlcn202.xlsx')
employment_data4 = pd.read_excel('Covid-19 Employment Data 2020/allhlcn203.xlsx')
employment_data5 = pd.read_excel('Covid-19 Employment Data 2020/allhlcn204.xlsx')

# reading the first few lines of each employment data file to understand the data structure
print(employment_data.head())
print(employment_data2.head())
print(employment_data3.head())
print(employment_data4.head())
print(employment_data5.head())



