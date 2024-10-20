class Palindrome:

    def __init__(self):
        self.Number=0
        self.Compare=0
        self.Compare1=0
        self.TempStore=0

    def input(self):
        while True:
            try:
                self.Number=int(input("enter the input:-"))
                break
            except ValueError:
                print("ERROR!...Only enter integer value")
        self.Compare=self.Number
        while self.Number!=0:
            self.TempStore=self.Number%10
            self.Compare1=self.Compare1*10+self.TempStore
            self.Number=self.Number//10
            if self.Number==0:
                break
            
        
    def display(self):
        self.input()
        if self.Compare !=0:
            if self.Compare==self.Compare1:
                print(f"Given Number {self.Compare} is palindrome")
            else:
                print(f"given Number {self.Compare} is not palindrome")

Pal=Palindrome()
Pal.display()