def READ():
    F=open("test1.txt","r")
    print(F.tell())
    print(F.read())
f.seek(6)
    print(F.read())
f.seek(4)
    print(F.read(5))
    print("current location of file pointer",f.tell())
F.close
READ()
