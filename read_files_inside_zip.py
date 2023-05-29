import pandas as pd
import os
from zipfile import ZipFile
from pathlib import Path

source_path = "C:\\Users\\scharuga\\Downloads\\New_Zip_File_For_Testing.zip"
destination_path = "C:\\Users\\scharuga\\Downloads\\New_Files"

with ZipFile(source_path,mode = 'r') as zObjcet:
    zObjcet.extractall(path = destination_path)

#df = pd.read_csv("C:\\Users\\scharuga\\Downloads\\New_Zip_File_For_Testing.zip")
#print(df)

files_list = []
for filespresent in Path(destination_path).glob('*.csv'):
    x= str(filespresent)
    files_list.append(x)

print(files_list)