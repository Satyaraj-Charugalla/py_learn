import pandas as pd
import os

file_path = "C:\\Users\\scharuga\\OneDrive - Capgemini\\Desktop\\Satyaraj\\csv files\\Books.csv"

df = pd.read_csv(file_path, infer_datetime_format= True)
print(df)

df1 = df.filter(df.Price == '500')
print(df1)