n=int(input("enter no= "))

if n%2==0:
    for n in range(2,6):
         print("Not Weired")
    for n in range(6,21,n):
        print("Weired")
    for n in range(21):
        print("Not weired")
else:
     print("weired")