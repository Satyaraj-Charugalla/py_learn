from zipfile import ZipFile
from pathlib import Path

#zipped_file_name = dbutils.widgets.get("File_Name")

main_zip = "C:\\Users\\scharuga\\Downloads\\Testing_Zip.zip"
store_zip_extarct = "C:\\Users\\scharuga\\Downloads\\Unpack_Files"
with ZipFile(main_zip, 'r') as zObject:
    zObject.extractall(path = store_zip_extarct)


"""
with ZipFile(store_zip_nested_extarct) as zz:
    for zip_search in zz.infolist():
        if zip_search.filename.endswith(".zip"):
            zz.extractall(store_zip_extarct)
"""