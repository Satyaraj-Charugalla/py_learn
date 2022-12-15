from zipfile import ZipFile
from pathlib import Path

main_zip = "/dbfs/mnt/hirevue/Testing_Zip.zip"
store_zip_extarct = "/dbfs/mnt/hirevue/Testing_Zip"
with ZipFile(main_zip, 'r') as zObject:
    zObject.extractall(path = store_zip_extarct)

# The below code will append the file locations in the string format to the list
direct_list = []
for dirctore in Path(store_zip_extarct).glob("*.zip"):
    x = str(dirctore)
    direct_list.append(x)

# The below code will check the length of the list and will proceed further if the length is > 0.
list_len = len(direct_list)
if list_len > 0:
    print(f"The nested zip file has {list_len} zip files in it")
    for zip_list in direct_list:
        with ZipFile(zip_list, 'r') as zipped:
            zipped.extractall(store_zip_extarct)
else:
    print('No nested zip folders')