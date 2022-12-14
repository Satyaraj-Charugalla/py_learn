"""
import zipfile, re, os

#This code extracts all the zip files inside the zip file and writes into another folder
import zipfile, re, os

def extract_nested_zip(zippedFile, toFolder):
    #Unzip a zip file and its contents, including nested zip files 
    # Delete the zip file(s) after extraction

    with zipfile.ZipFile(zippedFile, 'r') as zfile:
        zfile.extractall(path=toFolder)
    #os.remove(zippedFile)
    for root, dirs, files in os.walk(toFolder):
        for filename in files:
            if re.search(r'\\.zip', filename):
                fileSpec = os.path.join(root, filename)
                extract_nested_zip(fileSpec, root)

extract_nested_zip("C:\\Users\\scharuga\\Downloads\\Testing_Zip.zip","C:\\Users\\scharuga\\Downloads\\TMobile_interviews")
"""

"""
from io import StringIO
def extract_nested_zipfile(path, parent_zip=None):
    #Returns a ZipFile specified by path, even if the path contains 
    # intermediary ZipFiles.  For example, /root/gparent.zip/parent.zip/child.zip 
    # will return a ZipFile that represents child.zip

    def extract_inner_zipfile(parent_zip, child_zip_path):
        #Returns a ZipFile specified by child_zip_path that exists inside parent_zip.
        memory_zip = StringIO()
        memory_zip.write(parent_zip.open(child_zip_path).read())
        return zipfile.ZipFile(memory_zip)

    if ('.zip' + os.sep) in path:
        (parent_zip_path, child_zip_path) = os.path.relpath(path).split(
            '.zip' + os.sep, 1)
        parent_zip_path += '.zip'

        if not parent_zip:
            # This is the top-level, so read from disk
            parent_zip = zipfile.ZipFile(parent_zip_path)
        else:
            # We're already in a zip, so pull it out and recurse
            parent_zip = extract_inner_zipfile(parent_zip, parent_zip_path)

        return extract_nested_zipfile(child_zip_path, parent_zip)
    else:
        if parent_zip:
            return extract_inner_zipfile(parent_zip, path)
        else:
            # If there is no nesting, it's easy!
            return zipfile.ZipFile(path)
"""

from zipfile import ZipFile

def unpack_zip(zipfile='', path_from_local=''):
    filepath = path_from_local+zipfile
    extract_path = filepath.strip('.zip')+'/'
    parent_archive = ZipFile(filepath)
    parent_archive.extractall(extract_path)
    namelist = parent_archive.namelist()
    parent_archive.close()
    for name in namelist:
        try:
            if name[-4:] == '.zip':
                unpack_zip(zipfile=name, path_from_local=extract_path)
        except:
            print('failed on', name)
            pass
    return extract_path
    
    # you can just call this with filename set to the relative path and file.

path = unpack_zip("C:\\Users\\scharuga\\Downloads","Testing_Zip.zip")