#4.	Program to input three  numbers and display the largest num
n1=float(input("Enter a number"))
n2=float(input("Enter a number"))
n3=float(input("Enter a number"))
if n1>n2 and n1>n3:
 print(n1,"is greatest")
elif n2>n1 and n2>n3:
 print(n2,"is greatest")
else:
    print(n3,"is greatest")
