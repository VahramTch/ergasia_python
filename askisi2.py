filename = input("Filename: ")
g= open("result.txt","w+")
with open(filename,"r") as f:
    content = f.read()

symbols=list(content)
count=0
for i in symbols:
    if (i.isprintable()==False):
        count+=1

print("You will find the result on result.txt file")
g.write("The number of non printable characters are:")
g.write('{}'.format(count))
g.close()
