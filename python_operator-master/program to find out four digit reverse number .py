a=int(input("enter four digit number"))
b=a%10
a=a//10
b1=a%10
a=a//10
b2=a%10
a=a//10
reverse=b*1000+b1*100+b2*10+a
print("revers of entered no=",reverse)