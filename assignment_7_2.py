fname = input("Enter file name: ")
count, val = 0, 0
tot_val = 0.0
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count+1
        striping = line.rstrip() 
        #A rstrip is used for removing the extra spacing at the end of the line
        x = striping.find(':') 
        #Since the requirment is to find the number and before the number there's a :
        val = float(line[x+2:-1])
        #There is a space after the colon so we have added 2 for the position of the value x
        tot_val = tot_val + val
print(f'Average spam confidence: {tot_val/count}')