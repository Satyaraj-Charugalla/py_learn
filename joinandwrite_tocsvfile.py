import pandas as pd
import os

csv_file_path = "C:\\Users\\scharuga\\OneDrive - Capgemini\\Desktop\\Satyaraj\\csv files\\limited_netflix_titles.csv"
parquet_file = "C:\\Users\\scharuga\\OneDrive - Capgemini\\Desktop\\Satyaraj\\csv files\\limited_netflix_titles.parquet"
temp_file = "C:\\Users\\scharuga\\OneDrive - Capgemini\\Desktop\\Satyaraj\\csv files\\joined_netflix_names.csv"

df1 = pd.read_parquet(parquet_file)
df2 = pd.read_csv(csv_file_path)

print(df1.head(10).to_string(index= False))