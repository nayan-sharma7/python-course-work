from abc import ABC, abstractmethod
# class shape(ABC): 
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
# class square(shape):
#     def __init__(self,side):
#         self.side = side
#     def square_details(self):
#         return f"square side is {self.side}"
#     def area (self):
#         area = self.side*self.side
#         return area
#     def perimeter(self):
#         p = 4*self.side
#         return p
# class rectangle(shape): 
#     def __init__(self,length,width):
#         self.length = length 
#         self.width = width
#     def area(self):
#         return self.length*self.width
#     def perimeter(self):
#         return 2*(self.length+self.width)

# square = square(4)
# print(square.area())
# print(square.perimeter())
# print(square.square_details())
# print()
# rectangle = rectangle(10,5)
# print(rectangle.area())
# print(rectangle.perimeter())

class socialmedia(ABC):
    @abstractmethod
    def messenger(self):
        pass
    @abstractmethod
    def calls(self):
        pass
    @abstractmethod
    def search(self):
        pass
    @abstractmethod
    def settings(self):
        pass

class whatsapp(socialmedia): 
    def messenger(self):
        print("whatsapp messenger")
    def calls(self):
        print("whatsapp call")
    def search(self):
        print("whatsapp serach")
    def settings(self):
        print("whatsapp settings")
class instagram(socialmedia):
    def messenger(self):
        print("insta messenger")
    def calls(self):
        print("insta call")
    def search(self):
        print("insta serach")
    def settings(self):
        print("insta settings")
a = whatsapp()
b = instagram()
a.messenger()
b.messenger()
a.calls()
b.calls()
a.search()
b.search()
a.settings()
b.settings()