"""
import zipfile, re, os

def extract_nested_zip(zippedFile, toFolder):
    #Unzip a zip file and its contents, including nested zip files 
    # Delete the zip file(s) after extraction

    with zipfile.ZipFile(zippedFile, 'r') as zfile:
        zfile.extractall(path=toFolder)
    os.remove(zippedFile)
    for root, dirs, files in os.walk(toFolder):
        for filename in files:
            if re.search(r'\\.zip$', filename):
                fileSpec = os.path.join(root, filename)
                extract_nested_zip(fileSpec, root)
"""

"""
#Not Working
import zipfile
import io
with zipfile.ZipFile("C:\\Users\\scharuga\\Downloads\\TMobile_interviewss.zip", 'r') as z:
    with z.open("C:\\Users\\scharuga\\Downloads\\TMobile_interviewss.zip",'r') as z2:
        z2_filedata =  io.BytesIO(z2.read())
        with zipfile.ZipFile(z2_filedata) as nested_zip:
            z.extractall("C:\\Users\\scharuga\\Downloads\\TMobile_interviews")
"""

import os
from zipfile import ZipFile
def unzip (path, total_count):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_name = os.path.join(root, file)
            if (not file_name.endswith('.zip')):
                total_count += 1
            else:
                currentdir = file_name[:-4]
                if not os.path.exists(currentdir):
                    os.makedirs(currentdir)
                with ZipFile(file_name) as zipObj:
                    zipObj.extractall(currentdir)
                os.remove(file_name)
                total_count = unzip(currentdir, total_count)
    return total_count

total_count = unzip ('.', 0)
print(total_count)