class A:
    def demo(self):
        print("A-----demo方法")
    def test(self):
        print("A-----test 方法")


class B:
    def demo(self):
        print("B-----demo方法")
    def test(self):
        print("B-----test 方法")
class C(A,B):
    pass 




#创建子类的对象
#好处  :   多继承可以让子类对象同时拥有多个父类的属性和方法


c =  C()

c.test()

c.demo()



#确定C类对象调用方法的顺序  

#查找的顺序是一个类的元组中进行查找从左向右继续查找
print(C.__mro__)