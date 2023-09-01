import pandas as pd
import pyarrow as pa
import pyarrow.parquet as paq

#read from a parquet file.
parquet_file_path = "C:\\Users\\scharuga\\Downloads\\userdata1.parquet"

#temp_df = pd.read_parquet(parquet_file_path)
#df = temp_df.head(10) #limits the number of columns to be displayed
#print(df)

#write data to a parquet file from a csv
csv_file_path = "C:\\Users\\scharuga\\OneDrive - Capgemini\\Desktop\\Satyaraj\\csv files\\limited_netflix_titles.csv"
to_parquet_file = "C:\\Users\\scharuga\\OneDrive - Capgemini\\Desktop\\Satyaraj\\csv files\\limited_netflix_titles.parquet"

#req_cols = ['title','director','rating','duration','listed_in']
csv_df = pd.read_csv(csv_file_path, index_col= False)
#print(csv_df)

#create a parquet file
csv_df.to_parquet(to_parquet_file, index= False)