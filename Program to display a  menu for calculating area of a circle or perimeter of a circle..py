#5. Program to display a  menu for calculating area of a circle or perimeter of a circle.
r=float(input("Enter Radius"))
print("1.Area")
print("2.perimeter")
choice=int(input("Enter choice"))
if choice==1:
 area=3.14*r*r
 print("Area",area)
else:
 peri=2*3.14*r
 print("peri",peri)
           


