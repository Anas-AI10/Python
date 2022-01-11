str=input('Enter a string')
Lc=uc=0
dc=ac=0
for a in str:
	if a.islower():
		lc+=1
	elif a.isupper():
		uc+=1
	elif a.isdigit():
		dc+=1
	if a.isaplha():
		ac+=1
print(“No. of lowercase letters”,lc)
print(“No. of uppercase letters”,uc)
print(“No. of digits”,dc)
print(“No. of aplhabets”,ac)
