# class Dog(object):

#     def __init__(self,name):
#         self.name = name 
#     def game(self):
#         print("%s蹦蹦的玩耍......"% self.name)


# class xiaotianquan(Dog):
#     def ganme(self):
#         print("%s飞到天上玩耍"% self.name)




# class Person(object):
#     def __init__(self,name):
#        self.name =name 
#     def game_with_dog(self,dog):
#         print("%s和%s快乐的玩耍" %(self.name,dog.name) )
#         dog.game()







# #1. 创建一个狗对象
# # wangcai = Dog("旺财")
# wangcai = xiaotianquan("飞天旺财")



# # 2. 创建小明对象
# xiaoming = Person("小明")



# # 3. 让小明和狗玩的方法   


# xiaoming.game_with_dog(wangcai)






class Tool(object):
    # 使用赋值语句定义类属性 记录所有工具对象的数量
    count = 0
    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量%d" % cls.count)
        pass



    def __init__(self,name):
        self.name = name 
        Tool.count +=1
    





#1.创建工具类对象     封装到类方法中

tool1 = Tool("水桶")
Tool.show_tool_count()





# # 1. 创建工具对象     实现计数的功能   

# tool1 = Tool("斧头")
# tool2 = Tool("榔头")
# tool3 = Tool("水桶")
# print(Tool.count)
# tool3.count = 99

# print("工具对象总数%d"% tool3.count)
# print("==========>%d" % Tool.count)











