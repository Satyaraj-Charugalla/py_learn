from zipfile import ZipFile
from pathlib import Path
import os

main_zip = "C:\\Users\\scharuga\\Downloads\\Testing_Zip.zip"
store_zip_extarct = "C:\\Users\\scharuga\\Downloads\\Unpack_Files"
with ZipFile(main_zip, 'r') as zObject:
    zObject.extractall(path = store_zip_extarct)

# The below code will append the file locations in the string format to the list
direct_list = []
for dirctore in Path(store_zip_extarct).glob("*.zip"):
    x = str(dirctore)
    direct_list.append(x)
#print(direct_list)

#To extarct the zip file names from the list
nested_zip_files_names = []
for x in direct_list:
    z = x.rfind("\\")
    #print(f"The position of the \\ for path {x} is at {z}")
    to_string = str(x[z+1:-4])
    nested_zip_files_names.append(to_string)
print(nested_zip_files_names)

#create the sub directories
nested_zip_files_directories= []
mode = 0o666
for sub_directory_names in nested_zip_files_names:
    Path = os.path.join(store_zip_extarct, sub_directory_names)
    os.mkdir(Path,mode)
    st = str(Path)
    nested_zip_files_directories.append(st)
print(nested_zip_files_directories)

list_len = len(direct_list)
if list_len > 0:
    print(f"The nested zip file has {list_len} zip files in it")
    for zip_list in nested_zip_files_directories:
        with ZipFile(zip_list, 'r') as zipped:
            #Since we are creating the directories with the zip file names we are appending the .zip
            # extension at the end
            extract_to_zip_directory = zip_list + ".zip" 
            # we are using the directory path and extracting data to that directory
            zipped.extractall(nested_zip_files_directories)
else:
    print('No nested zip folders')