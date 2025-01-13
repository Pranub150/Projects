a= int(input("Enter a number:"))
b= int(input("Enter a number:"))
c=int(input("Enter a number:"))
print("Before swapping a=" , a,"b=", b, "c=", c)
a=a+b+c
b=a-(b+c)
c=a-(b+c)
a=a-(b+c)
print("After swapping a=", a, "b=", b, "c=", c)


