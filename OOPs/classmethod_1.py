class person:
    name="Golu"

    @classmethod
    def changename(cls,name):
        cls.name=name
        
   
       
s1=person()
s1.changename("Akshat Jangid")
print(s1.name)
print(person.name)
        