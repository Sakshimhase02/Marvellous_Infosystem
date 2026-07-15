class demo:

    Value = 0

    def __init__(self,No1,No2):
        self.No1  = No1
        self.No2  = No2

    def Fun(self):
        print("Inside Instance method name as Fun")
        print("No1 is : ",self.No1)
        print("No2 is : ",self.No2)

    def Gun(self):
        print("Inside Instance method name as Gun")
        print("No1 is :",self.No1)
        print("No2 is :",self.No2)


Obj1 = demo(11,21)
Obj2 = demo(51,101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()