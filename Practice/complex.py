class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownum(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, other):
        new_real = self.real + other.real
        new_img = self.img + other.img
        return complex(new_real, new_img)
    
num1 = complex(3, 4)
num1.shownum()
num2 = complex(5, 6)
num2.shownum()
num3 = num1 + num2
num3.shownum()
