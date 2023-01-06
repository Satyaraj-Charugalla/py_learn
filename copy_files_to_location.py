import shutil

src_path = r"C:\\Users\\scharuga\\Desktop\\TMO_Credentials.txt"
dst_path = r"C:\\Users\\scharuga\\Downloads\\TMO_Credentials.txt"
shutil.copy(src_path, dst_path)
print('Copied')