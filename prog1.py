#pro1.Find the Perfect numbers.sum to 28
number=int(input("Enter number:"))
a=1
b=0
num=1
while(a<=number):
    sum=0
    for b in range(1,num):
        if(num%b==0):
            sum+=b
    if(sum==num):
         a+=1
         print(num)
    num+=1