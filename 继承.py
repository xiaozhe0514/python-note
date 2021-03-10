class Animal:
    def eat(self):
        print("吃")
        
    def drink(self):
        print("喝")

    def run(self):
        print("跑")
    
    def sleep(self):
        print("睡")
    


class Dog(Animal):

    def bark(self):
        print("汪汪汪汪汪汪汪汪汪汪汪汪")



class xiaotianquan(Dog):
    def fly(slef):
        print("我是哮天犬你好啊，我会飞")
    #重写父类的方法    重名的父类方法  
    def bark(self):
        #在子类的特殊需求 调用父类的bark方法  叫声的方法   

        #super().bark()
        super()
        Dog.bark(self)
        print("我的叫声是特殊的 叫的和神一样 ")



    




    




#创建对象


wangcai = xiaotianquan()

wangcai.fly()
wangcai.sleep()
#创建的对象会调用子类重写的方法不会调用父类的方法  
#扩展父类的方法
wangcai.bark()








