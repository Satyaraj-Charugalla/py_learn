import pandas as pd
import os

file_path = "C:\\Users\\scharuga\\OneDrive - Capgemini\\Desktop\\Satyaraj\\csv files\\netflix_titles.csv"

#read specific columns data
cols = ['title','director','rating','duration','listed_in']
temp_df = pd.read_csv(file_path, usecols= cols)
#df =temp_df.head(20)
print(temp_df)

#to create a file or to add data from the dataframe to a csv file
to_csv_filepath = "C:\\Users\\scharuga\\OneDrive - Capgemini\\Desktop\\Satyaraj\\csv files\\limited_netflix_titles.csv"
temp_df.to_csv(to_csv_filepath, columns= cols, index= False)