"""def add(a,b):
    c=a+b
    print(c)

add(10,20)
"""
"""
def odd_even():
    a=int(input("enetr  no for check ="))
    if a%2==0:
        print("even")
    else:
        print("odd")

odd_even()
"""
def tri():
    line=int(input("enter no of lines="))
    for i in range(1,line+1):
        for j in range(i):
            print("*",end="")
        print()
tri()
