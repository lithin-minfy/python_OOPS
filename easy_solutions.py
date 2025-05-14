# Easy1
class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    

rect = rectangle(5, 10)
print(rect.area()) 
print(rect.perimeter())


# Esay 2
class counter:
    def __init__(self):
        self.value=0
    def increment(self):
        self.value+=1
    def decrement(self):
        self.value-=1
    def reset(self):
        self.value=0

counter = counter()
counter.increment()
counter.increment()
print(counter.value) 
counter.decrement()
print(counter.value)  
counter.reset()
print(counter.value) 
