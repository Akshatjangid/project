class student:
    def __init__(self,name,marks):
     
        self.name=name
        self.marks=marks # type: ignore

    @staticmethod          #static method
    def hello():
       print("Hello World")   

    def get_avg(self):
       sum=0
       for val in self.marks:
        sum += val
        print("h",self.name,"your avg score is:",sum/3)
                    

s1=student("samar",[100,99,98])
s1.get_avg()
s1.name="ironman"
s1.get_avg()
s1.hello()