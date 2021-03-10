# import random

# rand1 = random.randint(1,10)
# rand2 = random.randint(1,10)
# print(random.__file__)
# # # print(rand2)
# # print("结果%d" % (rand1*rand2))




#主要就是针对文件进行测试   编写主函数的操作 


# def main():
#     if __name__ == "__main__":
#         print("123")




# main()

#使用单例模型进行数据的判断和使用 外界创建的内存地址都是相同的
#使用初始化动作和数据的模型执行的操作  初始化动作和创建对象只占用一块内存地址

class MusicPlayer(object):
    # def __init__(self):
    #     print("播放器初始化")
    #记录第一个被创建对象的引用

    instance = None
    init_flag = False

    # 2. 改造new方法  
    def __new__(cls, *args,**kwargs):
        # 1. 判断类属性是都是空对象
        if cls.instance is None:
            
            # 2. 调用父类对象的方法  为第一个对象分配空间  
            cls.instance = super().__new__(cls) 
        # 3. 返回类属性保存的对象引用   
        return cls.instance
    def __init__(self):
        # 1. 判断是否执行过初始化工作  
        if MusicPlayer.init_flag:
            return 
        
        # 2. 没有执行过  执行初始化动作    
        print("初始化播放器")
        # 3. 修改类属性的标记   
        MusicPlayer.init_flag = True







       




player1 =MusicPlayer()
print(player1)

player2 =MusicPlayer()
print(player2)








