str=input("Please enter a string    : ");
vowels=cons=0
uc=lc=0
 for i in str:
    if(i == 'a' or  i == 'e' or  i == 'i' or  i == 'o' or  i == 'u'  or
         i == 'A' or  i == 'E' or  i == 'I' or  i == 'O' or  i == 'U' ):
vowels=vowels+1 
    else:
                 cons =cons +1 
if  i.isupper( ):
     uc+=1
                 elif  i.islower():
                  	lc+=1
print("The number of vowels:",vowels);
 	print(“The number of consonants:”,cons)
print(“The number of uppercase:”,uc)
print(“The number of lowercase:”,lc)
