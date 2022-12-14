# importing the zipfile module
from zipfile import ZipFile

# loading the temp.zip and creating a zip object
with ZipFile("C:\\Users\\scharuga\\Downloads\\TMobile_interviews.zip", 'r') as zObject:

	# Extracting all the members of the zip
	# into a specific location.
	zObject.extractall(path="C:\\Users\\scharuga\\Downloads\\TMobile_interviews")