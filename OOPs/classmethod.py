"""class person:
    name="Golu"
    def changename(self,name):
        person.name=name

s1=person()
s1.changename("Akshat")
print(s1.name)
print(person.name)"""

class person:
    name="Golu"
    def changename(self,name):
        self.__class__.name="Akshat"
        # sel.<  __class__  >. name   here in <> its
        #  present main parents class (person) and
        # after . present which attribute we want to access
s1=person()
s1.changename("Akshat Jangid")
print(s1.name)
print(person.name)
        