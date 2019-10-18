filename = input("Filename: ")
with open(filename,"r") as f:
    content = f.read()
#exoume ws dedomeno oti ta sxolia sthn c++ einai /* ......  */
symbols=list(content)
for i in range(len(symbols)):
    if (symbols[i]=="/") and (symbols[i+1]=="*"):
        y=i+2
        while True:
            print(symbols[y],end =" ")
            
            if (symbols[y+1]=="*") and (symbols[y+2]=="/"):break
            y=y+1
            
