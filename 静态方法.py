# class Dog(object):
    
#     @staticmethod
#     def run():
#         print("小狗喜欢跑......")



# #调用静态方法   通过类名点的方式进行静态方法的调用  
# # # 不需要创建对象就能直接调用静态方法   
# # 不访问实例属性和类属性时候   
# # 不需要传递第一个参数 在定义的时候增加@staticmethod

# Dog.run()


class Game(object):
    #历史最高分
    top_score = 0

    #定义实例属性
    def __init__(self,player_name):
        self.player_name = player_name
    
    @staticmethod
    def show_help():
        print("帮助信息：让人们进入大门")
    
    @classmethod
    def show_top_score(cls):
        print("历史记录%d"% cls.top_score)
        
    def start_game(self):
        print("%s开始游戏了....." % self.player_name)



#1.查看游戏帮助信息  
Game.show_help()

# 2. 查看历史最高分数  
Game.show_top_score()

# 3. 创建游戏对象
game = Game("小明")
game.start_game()


"""



"""








