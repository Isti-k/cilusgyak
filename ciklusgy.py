def  feladat():
    a: int = int(input("Adjon meg egy pozitív egész számot!"))
    b: int = 1
    while (b<=a):
        if b==a:
            print(b, end=" ")
        else:
            print(b, end=", ")
        b+=1

def feladat2():
    a: int = int(input("Adjon meg egy pozitív egész számot!"))
    i: int = 1
    osszeg: int = 0
    while (i<=a):
        if a % i==0:
            print(f"{i}")
            osszeg +=i
        i+=1
    print("Az összeg:" + str(osszeg))

def feladat3():
    a: int = int(input("Adjon meg egy számot!"))
    b: int = int(input("Adjon meg egy számot!"))
    i: int = a
    while (b>=i):
        if i % 2 == 0:
            print(i)
        i+=1

def feladat4():
    i: int = 0
    while i<=20:
        if i==0:
            print(i)
    i+=1
