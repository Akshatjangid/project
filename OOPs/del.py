class student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    
s1=student("Akshat",11)
print(s1.name)
del s1.roll_no
print(s1.roll_no)