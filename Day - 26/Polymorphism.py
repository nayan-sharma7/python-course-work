""""        Polymorphism        """
# there are two types in polymorphism :- 
# mthod overloading and Mthodoveriding
"""     Method Overloading       """
# class c:
#     def method2(self,a,b,c=0,d=0):
#         return a+b+c+d
# o = c()
# print(o.method2(10,20))
# print(o.method2(1,2,3))
# print(o.method2(100,200,300,400))

# class c2:
#     def method3(self,*a):
#         return sum(a)w
# b = c2()
# print(b.method3(1,2,3,4,5,6,7,8,9,10))

"""     Duck Typing     """
# class employee:
#     def work(self):
#         return "Employee is working"
# class developer:
#     def work(self):
#         return "developer is working"
# res = [employee(),developer()]
# for i in res:
#     print(i.work())

"""         Methodoveriding        """
class a:
    def m1(self):
        print("parent m1")
class b(a):
    def m1(self):
        print("child m1")
        super().m1()
c1 = b()
c1.m1()
a.m1(c1)