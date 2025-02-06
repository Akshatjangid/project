class student:
  
   
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("adding new student in database")


s1=student("karan",97)
print(s1.name,s1.marks) 
s2=student("arjun",88)
print(s2.name,s2.marks) 
