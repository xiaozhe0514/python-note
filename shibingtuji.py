# """
# 类的分析  


# """

# class Gun:
#     def __init__(self,model):
#         self.model = model

#         self.bullet_count = 0
#     def add_bullet(self,count):
#         self.bullet_count += count
    
#     def shoot(self):
#         #1. 判断子弹的数量
#         if self.bullet_count <= 0:
#             print("[%s]没有子弹了..." % self.model)
#             return

#         #2.发射子弹 -1 
#         self.bullet_count -= 1
#         #3.提示发射信息  
#         print("[%s]突突突.... [%d]" % (self.model,self.bullet_count))


# class Solder:
#     def __init__(self,name):
#         #1.姓名
#         self.name = name 
#         #2.枪 新兵没有枪对象       在初始化环境进行把属性设置好 需要修改的时候在在外部进行修稿    不知道初始值使用None
#         self.gun = None
#     def fire(self):
#         # 1.判断士兵是不是由枪
#         #if self.gun == None:
#         if self.gun is None:   
#             print("[%s]还没有枪" % self.name)
#             return


#         # 2. 高喊口号  
#         print("冲......[%s]" % self.name)



#         # 3. 枪安装子弹  
#         self.gun.add_bullet(50)




#         # 4.枪发射子弹   
#         self.gun.shoot()





# #主程序    是很关键的  一个对象的属性可以是另外一个类创建的对象   封装完成后直接调用方法


# #1.创建枪类

# ak47  = Gun("Ak47")
# # ak47.add_bullet(50)
# # ak47.shoot()


# #2.创建士兵
# xusanduo = Solder("许三多")
# xusanduo.gun = ak47
# xusanduo.fire()
# print(xusanduo.gun)
# #编程最重要的就是分析问题和解决问题    问题分析的不明白就没办法进行分析   


# #is运算符    is not   都是python的身份运算符号     比较两个对象的内存地址是不是一致      是不是同一个对象  

# #is和==区别 is对象的地址是不是相等    ==  数值是不是相等  
# #私有属性和私有方法

# #私有属性就是外部不能访问的属性   
# #私有方法就是外部不能访问的方法
# #定义私有属性和私有方法的时候  在属性名或者方法名前增加两个下划线    在外界不能被直接访问的  


# class Women:
#     def __init__(self,name):
#         self.name  = name 
#         self.__age = 18
#     def secret(self):
#         #在对象内部可以被访问对象的私有属性   对象内部可以访问 这就是私有属性  
#         print("[%s]年龄 %d" % (self.name,self.__age))


# xiaofang = Women("xiaofang")

# print(xiaofang._Women__age)
# #私有方法同样不允许在外界直接被访问    


# xiaofang.secret()    

# #伪私有属性和方法       python中并没有真正的私有的   
# #python解释器处理私有属性和私有方法     在名称前面加上__类名    =>_类名__名称    这是特殊的访问方法   不建议使用但是可以使用毕竟是私有属性


"""
#私有属性和私有方法的扩展  

子类对象能不能访问父类的属性和方法   





"""


class A():
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def __test(self):
        print("私有方法 %d %d "% (self.num1,self.num2))
    def test(self):
        #print("父类的公有方法%d" % self.__num2)
        self.__test()



class B(A):
    def demo(self):

        # #1.访问父类的私有属性
        # print("访问父类的私有属性%d" % self.__num2)

        #2.调用父类的私有方法    子类不能调用父类的私有方法   只能访问公有属性和方法
        # 3. 访问父类的公有方法和父类的公有的属性 是可以直接在子类中直接访问的
        print("子类方法%d" % self.num1)
        self.test()

       

   


#创建子类对象

b = B()
print(b)
#外部访问公有属性和方法

b.demo()


#在外界不能访问私有属性和私有方法   






