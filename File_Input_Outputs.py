f = open('Open_files.txt', mode = 'wt', encoding = 'utf-8')
# here the mode wt means Write text sometime we use wb which means Write binary
# or even at => Append text

f.write('Line 1 is added, ')
f.write('Line 1 continouation is added')
f.close()