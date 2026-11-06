class MyObject():
    def __init__(self,p1,p2,p3):
        self.p1 = p1

    def get_p1(self):
        return self.p1

    def set_p1(self, new_value):
        self.p1 = new_value


    def __str__(self):
        msg = ""
        #your msg here
        return msg

x = int(3)

x = MyObject(1,2,3)
x = MyObject.__init__(1,2,3)



print(x.get_p1())

x.set_p1(5)

print(x.get_p1())

print(x)
print(x.__str__())



getter, setter, constructor (__init__), str rep of object, ToString (the string representation of an object.)