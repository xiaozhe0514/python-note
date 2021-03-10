# str = "我是中国人"
# print(f'Unicode字符串为"{str}"')
# byte0 = str.encode("utf-8")
# print(f'Unicode字符串"{str}"以utf-8编码得到字节串[{byte0}]')
# str0 = byte0.decode("utf-8")
# print(f'将utf-8字节串[{byte0}]解码得到Unicode字符串"{str0}"')

# byte1 = str.encode("gbk")
# print(f'Unicode字符串"{str}"以gbk编码得到字节串[{byte1}]')
# str1 = byte1.decode("gbk")
# print(f'将gbk字节串[{byte1}]解码得到Unicode字符串"{str1}"')
# f = open("maxin.txt","w",encoding="utf-8")
# f.write("我爱自动化运维.\n")
# f.write("我爱网络行业..\n")
# f.write("hello world\n")
# f.close()



# #以字节形式读文件
# f = open("wb.txt", "rb")
# # 以文本方式读，f.read()返回字节对象
# data = f.read()
# print(type(data))
# print(data)
# print('将读取的字符对象解码：')
# print(data.decode('utf-8'))
# f.close()
# print(f'以文本方式将Unicode字符串"{str}"写入a.txt')

# with open("a.txt", "w", encoding="gbk") as f:
#     f.write(str)

# print("以文本方式读取 a.txt 的内容")
# with open("a.txt", "r", encoding="gbk") as f:
#     print(f.read())


# #获取cpu的个数
# import psutil
# import socket

# print(psutil.cpu_count())

# #统计cpu的用户系统 时间和空闲时间
# print(psutil.cpu_times())
# print(psutil.cpu_times(percpu=True))
# #获取cpu的占用率
# for x in range(10):
#     s = psutil.cpu_percent(interval=1)
#     print("当前cpu占比：", s)
# #查看物理内存信息
# print(psutil.virtual_memory())

# #查看交换内存
# # print(psutil.swap_memory())










# # #实例演示
# # mem = psutil.virtual_memory()
# # print(mem.total)
# # print(mem.used)
# # print(mem.free)
# # print(type(mem.free))
# # if mem.used / mem.total > 0.8:
# #     print("内存占用过高")
# # else:
# #     print("内存占比正常")

# # #查看磁盘分区分析
# # print(psutil.disk_partitions())
# # #磁盘占用的io数
# # print(psutil.disk_io_counters(perdisk=True))

# # s = psutil.disk_io_counters(perdisk=True)
# # s['PhysicalDrive0']
# # s['PhysicalDrive0'].read_count

# # print(s)

# # #监控网络信息
# # import socket
# # hostname = socket.gethostname()
# # print(hostname)

# # print(socket.gethostbyname(hostname))
# # #获取网络的字节数
# # print(psutil.net_io_counters())


# # #获取网络接口信息
# # print(psutil.net_if_addrs())

# # #获当前网络链接信息
# # print(psutil.net_connections())


# #使用python编写系统运行报告
# print("CPU的个数：", psutil.cpu_count())
# print("CPU的物理总数是", psutil.cpu_count(logical=False))
# print("CPU的空闲时间是：", psutil.cpu_times())
# print("CPU的占用率是", psutil.cpu_percent())

# for x in range(10):
#     s = psutil.cpu_percent(interval=1)

#     print("当前cpu占比为：", s)

# print("物理内存是:", psutil.virtual_memory())
# print("交换内存是", psutil.swap_memory())
# print("查看磁盘分区", psutil.disk_io_counters())
# print("查看磁盘利用率：", psutil.disk_usage("c:\\"))
# print("查看磁盘io总数：", psutil.disk_io_counters)
# print(psutil.disk_io_counters().read_count)
# print("查看每个磁盘io数", psutil.disk_io_counters(perdisk=True))


# #获取本机的IP地址
# hostname = socket.gethostname()
# print("您的主机名是", hostname)
# print("您的主机IP是", socket.gethostbyname(hostname))
# print("网络读写字节个数", psutil.net_io_counters())
# print("网络接口信息", psutil.net_if_addrs())
# print("网络接口状态", psutil.net_if_stats())




# # from watchdog.observers import Observer
# # from watchdog.events import *
# # import time

# # class FileEventHandler(FileSystemEventHandler):
# #     def __init__(self)
# #     FileEventHandler.__init__(self)
# #该命令只能在linux上执行和使用

# # import subprocess
# # a = subprocess.run("ls -al /dev/null", shell=True)
# # print(a)

# # import subprocess
# # print(subprocess.run(['ipconfig']))




# # #打印到控制台
# # import logging
# # logging.debug('ddebug message')
# # logging.info('info message')
# # logging.critical('critical message')
# # import platform 
# # print(platform.uname())


# # num = 2
# # name = "tom"

# # print(name)

# # print(num)


# # name2 ={1,2}
# # print (type(name2))


# # url = "www.baidu.com"
# # while url:
# #     url = url[:-1]
# #     print(url)
# # else:
# #     print("over")




# # str4 = "hello"
# # print(str4)



# # s = 6
# # str5 = hex(s)
# # str6 = bin(s)
# # print(str5)
# # print(str6)


# print((1 - 0.01) ** 365)
# print((1 + 0.01) ** 365)
# import math
# num10 = 4
# num12 = 13
# print(math.sqrt(num10))

# # print(math.sqrt(num12))

# # str = ["hello"]
# # print(str)

# price  = 8.5 
# wight = 7.5 
# total = price * wight
# total = total - 5

# # print(total)

# # fullname = 'xiaoming'
# # age = 16
# # sex = "男"


# # shengao = "1.65"
# # wigth = '25kg'
# first_name = "张"
# last_name = "三"
# print(first_name + last_name)
# print((first_name + last_name) * 3)
# input("密码：")








# has_ticket = False
# knifie_length = 30

# if has_ticket:
#     print("通过开始检测")
#     if knifie_length > 20:
#         print("太长了")
#     else:
#         print("错误")
        
# else:
#     print("结束")

# int01 = int(input("请输入您要出的拳头   石头:1   剪刀:2  布:3"))

# int02 = range(1,3)
# #解决的思路    使用数字和文字进行绑定   然后判断数字和电脑随机数生成的数字
# #情况之间进行判断 配合逻辑进行判断

# computer = int02
# print(int02)

# if int01 == int02:
#     print("平局")


# i= 1
# while i <= 3:
#     print("你好")
#     i=i+1
# #使用单步执行进行变量的判断
# print("循环结束后，i=%d"%i) 
# print("偶数求和")
# 编写循环   求出偶数  最后在加起来


# def main():
#     i = 1
#     while i <= 10:
#         print("hello01")
#         print("hello02")
#         i += 1


# def test():
#     """测试使用的"""
#     i = 1
#     while i <= 3:
#         print("hello01")
#         print("hello02")
#         i += 1



# test()





# def sum_2_sum(num1, num2):
#     """主要就是整数加法和减法"""
    
#     result = num1 + num2
#     print("最终的结果为：%d+%d=%d" % (num1, num2, result))

# def sum_3_sum(a,b):
#     return sum_2_sum(a, b)


# a = int(input("第一个数据："))
# b = int(input("第二个数据："))
# sum_3_sum(a,b)


# 函数调用的演示过程
# def test01():
#     print("*"*50)

# def test02():
#     print("-" * 50)
#     test01()
#     print("-" * 50)

# test02()




# print(3 + 1)

# print(chr(20056))

# 标识符   保留字     规矩

# 保留字就是写代码不能使用默认的

# import keyword
# print(keyword.kwlist)
# 变量命名的规则就是表示符号
# 不能使用保留字和系统默认的字符



# 自动打字的代码：
# import pyautogui
# import time
# r = open('2.txt','r')
# time.sleep(5)
# for i in r.read():
#     pyautogui.press(i)
#     time.sleep(0.8)


# 参考笔记
# https://www.cnblogs.com/caicairui/p/7520037.html


# 关于python学习中遇到的can only concatenate str （not “int”）to str 这种错误经过学习得到了以下结论:

# 1、字面上理解即只能用字符串与字符串拼接，笔者自己便是将int的数字与字符串拼接时得到这种报错
# 2、解决方式:根据需要转换数据类型
# 如:字符串转换为int int_data=int(str_data)
# nt 转换为字符串 str_data=str(int_data)


# candidate
# 1、首先要倒入库OS、SYS

# 2、路径的写法path+'\\文件名.格式'

# 如此，实现相对路径读取文件


# 读取相对路径




# 局部变量和全局变量



# #递归调用自己  
# def sum_numbers(num):
#     #1.出口
#     if num ==1:
#         return 1
    

#     #2.数字的累加 num+（1.........num+1）
#     temp = sum_numbers(num-1)
#     #核心代码就是两个数字的累加  
#     return num + temp
    

# result = sum_numbers(100)

# print(result)






# class Cat:
#     def eat(self):
#         print("%s爱吃鱼" % self.name)
    
# #     def drink(self):
# #         print("%s喝水" % self.name )
# #         #self 就是对象的应用   第一个参数方法内部就是slef的引用   
# #         # 方法的时候使用self点进行引用


# # tom = Cat()
# # tom.name = "tom"
# # tom.eat()
# # tom.drink()



# class  Cat:
#     def __init__(self,new_name):
#         self.name = new_name
#         print("%s来了" % self.name)
#     def __del__(self):
#         print("%s我去了" % self.name)
#     def __str__(self):
#         # 必须返回一个字符串  使用return返回
#         return "我是小猫[%s]" % self.name




# class Person:
#     def __init__(self,name,weight):
#        # self.属性 = 形参
#         self.name = name
#         self.weight = weight
#     def  __str__(self):
#         return "我的名字叫%s 体重是%.2f公斤" % (self.name,self.weight)
#     def run(self):
#         print("%s爱跑步,跑步锻炼身体" % self.name)
#         self.weight -= 0.5 



#     def eat(self):
#          print("%s是吃货，吃完在减肥" % self.name)
#          self.weight += 1




# xiaoming = Person("xiaoming",75.0)
# xiaoming.run()
# xiaoming.eat()
# print(xiaoming)

# print("="* 50 )

# #小美爱跑步  

# xiaomei = Person("小美", 45)
# xiaomei.eat()
# xiaomei.run()
# print(xiaomei)

# print(xiaoming)



    





# #tom是一个全局变量
# tom  = Cat("tom")
# print(tom)































