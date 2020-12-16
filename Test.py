fname=input('')
fh=open(fname)
count=0
for line in fh:
    count=count+1
    print(count)
