fname = input("Enter file name: ")
count, val = 0, 0
tot_val = 0.0
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count+1
        striping = line.rstrip()
        x = striping.find(':')
        val = float(line[x+2:-1])
        tot_val = tot_val + val
print(f'Average spam confidence: {tot_val/count}')