class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def show_num(self):
        print(self.real, "i+", self.img, "j")

    def add_num(self, num2):
        new_real = self.real + num2.real
        new_img = self.img + num2.img
        return complex(new_real, new_img)
    
    def __str__(self):
        return f"{self.real} i + {self.img} j"

cmp1 = complex(1, 3)
cmp1.show_num()

cmp2 = complex(2, 5)
cmp2.show_num()

cmp3 = cmp1.add_num(cmp2)
print(cmp3)
