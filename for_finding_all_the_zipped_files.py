from zipfile import ZipFile
from pathlib import Path

main_zip = "C:\\Users\\scharuga\\Downloads\\Testing_Zip.zip"
store_zip_extarct = "C:\\Users\\scharuga\\Downloads\\Unpack_Files"
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

# Code to remove the zip files from the directory
for remove_zip_files in Path(store_zip_extarct).glob("*.zip"):
    try:
        remove_zip_files.unlink()
    except OSError as e:
         print("Error: %s : %s" % (remove_zip_files, e.strerror))