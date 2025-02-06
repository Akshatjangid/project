def sum():
    lst = []
   user = int(input("how many list create="))
    for i in user:
        choice=int(input(f"lst are creating {i} = "))
        lst.append(choice)

    total = 0
    for i in range(len(lst)):
        total = total+ lst[i]

    
    return f"total is {total}"
            
s=sum()  
print(s)  