a=int(input("enter number one:"))
b=int(input("enter number two:"))
if(a>b):
    min=b
else:
    min=a
if(b>a):
    max=b
else:
    max=a
i=1
for i in range(i,min+1):
    if(max%i==0 and min%i==0):
        print(i)
