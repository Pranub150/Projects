num= int(input("Enter a number:"))
count=0
temp=num
while temp>0:
    digit= temp%10
    count+= 1
    temp//=10

print(count, "is the number of digits.")

