import os
from pathlib import Path
from datetime import date
import xlsxwriter

daily_status_loc = "C:\\Users\\scharuga\\OneDrive - Capgemini\\CREA\\Daily Status\\2023"
sampl_loc = "C:\\Users\\scharuga\\Downloads\\Sample_Path"
status_check_loc = "C:\\Users\\scharuga\\OneDrive - Capgemini\\CREA\\For_Status_Check\\2023"
mode = 0o666

todays_date = date.today()
current_month = todays_date.month
print(current_month)

if current_month in (1,3,5,7,9,11):
    for i in range(1,31):
        x = '2023_'+str(current_month)+'_'+str(i)+'.xlsx'
        z = sampl_loc+x
        work_book = xlsxwriter.Workbook(z)

elif current_month == 2:
    for i in range(1,30):
        x = '2023_'+str(current_month)+'_'+str(i)+'.xlsx'
        z = sampl_loc+x
        work_book = xlsxwriter.Workbook(z)

else:
    for i in range(1,30):
        x = '2023_'+str(current_month)+'_'+str(i)+'.xlsx'
        z = sampl_loc+x
        work_book = xlsxwriter.Workbook(z)