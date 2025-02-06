class student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
    @property
    def percentage(self):
        return str(( self.phy + self.chem +self.maths)/3)+ "%"
    

s1=student(10,12,13)
print(s1.percentage)
s1.phy=100
s1.chem=98
s1.maths=99
print(s1.percentage)
        