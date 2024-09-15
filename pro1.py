#pro1.Find the Perfect numbers.
def is_perfect_number(num):
    divisors_sum=0
    for i in range(1,num):
        if num%i==0:
            divisors_sum+=i
    return divisors_sum==num
num=int(input("enter number:"))
if is_perfect_number(num):
    print("perfect number")
else:
    print("not perfect")
	