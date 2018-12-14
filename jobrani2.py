a=int(input("adad="))
b=int(input("dar mabnaye chand ast?"))
s=0
t=1
while(a>0):
    r=int(a%10)
    s=s+r*t
    t=t*2
    a=int(a/10)
#print(s)
c=int(input("dar mabnay e chand mikhahid?"))
p=0
i=0
list=[0]*10
while(s>0):
    list[i]=int(s%c)
    s=int(s/c)
    i=i+1
i=i-1
while(i>=0):
    print(list[i],end='')
    i=i-1
