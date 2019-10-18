x = input("Enter your input: ")
symbols=list(x)
count=0
for i in symbols:
    if i=="(":
        count +=1
    elif i==")":
        count -=1

    if count < 0:
        print("NO")
        break
if count ==0:
    print("YES")
else:
    print("NO")
