# Creating a small command line programming in Python to caluclate the total invoice amount for below purchase 
a=499.00 * int(input())
b=855.00 * int(input())
c=645.00 * int(input())
Rate=0.12
Delivery_Charges=250.00
s=a+b+c
s1=s*Rate
s2=s+s1+Delivery_Charges
print(s2)
