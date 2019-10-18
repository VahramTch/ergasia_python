prnum=[]
s=[]
for num in range(1,1000):
 if num > 1:
    
    for i in range(2,num):
        if (num % i) == 0:
            
         
            break
    else:
      
        prnum.append(num)
       
print("All the prime numbers are:")
for i in prnum:
    print(i)

for i in range(1,len(prnum)):
    s.append(prnum[i]-prnum[i-1])
print("All the differnces between the prime numbers are:")    
for i in s:
   print(i)

max=-1
for i in s:
    if i>max:
        max=i

print("The biggest difference is",max)           


 
