import pandas as pd
import pyarrow as pa
import pyarrow.parquet as paq
import os

csv_file_path = "C:\\Users\\scharuga\\OneDrive - Capgemini\\Desktop\\Satyaraj\\csv files\\limited_netflix_titles.csv"
parquet_file = "C:\\Users\\scharuga\\OneDrive - Capgemini\\Desktop\\Satyaraj\\csv files\\limited_netflix_titles.parquet"
temp_file = "C:\\Users\\scharuga\\OneDrive - Capgemini\\Desktop\\Satyaraj\\csv files\\joined_netflix_names.csv"

os.remove(temp_file)

csv_df = pd.read_csv(csv_file_path)
parq_df = pd.read_parquet(parquet_file)

#Merge condition will merge 2 or more dfs.
#Syntax for merge pd.merge(df1, df2, on = 'the column name', how(join) = 'inner\left\right')
#if there is no join mentioned the join will be picked as inner

#the below condition will merge 2 or more data frames
join_df = pd.merge(csv_df, parq_df)
join_df.to_csv(temp_file,index = False)