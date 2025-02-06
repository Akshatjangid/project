class student:
  
   
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("adding new student in database")

    def welcome(self):
       print("welcome student",self.name)

    def self_mark(self):
        return self.marks
       

s1=student("karan",97)
s1.welcome()
print(s1.marks)



