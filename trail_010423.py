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
print(f'Files location:\n{direct_list}')


#To extarct the zip file names from the list
nested_zip_files_names = []
for x in direct_list:
    z = x.rfind("\\")
    #print(f"The position of the \\ for path {x} is at {z}")
    to_string = str(x[z+1:-4])
    nested_zip_files_names.append(to_string)
print(f'Zip file names in the location:\n{nested_zip_files_names}')

#create the sub directories
nested_zip_files_directories= []
mode = 0o666
for sub_directory_names in nested_zip_files_names:
    Path = os.path.join(store_zip_extarct, sub_directory_names)
    os.mkdir(Path,mode)
    st = str(Path)
    nested_zip_files_directories.append(st)
print(f'Sub directory names:\n{nested_zip_files_directories}')

for zipfileloc in direct_list:
    """
    #print(zipfileloc)
    z1 = zipfileloc.rfind(".")
    print(f'Position of . is {z1}')
    """
    z1 = zipfileloc.rfind(".")
    with ZipFile(zipfileloc, 'r') as zobj:
        zobj.extractall(zipfileloc[:z1]) 