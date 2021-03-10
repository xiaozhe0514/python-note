# a, b = 0, 1
# while a < 100:
#     print(a, end='')
#     a, b = b, a + b

#  #计算面积
#  #    
# r = 25
# area = 3.1415626 * r * r
# print(area)
# print("{:.2f}".format(area))

#画五角星 
# from turtle import *

# color('red', 'red')
# begin_fill()
# for i in range(5):
#     fd(200)
#     rt(144)
#     end_fill()
# done()

# #绘制七彩的园 
# import turtle 
# colors = ["red","orange","yellow","green","blue","indigo","purple"]
# for i in range(7):
#     c = colors
#     turtle.color(c,c)
#     tutle.begin_fill()
#     tutle.rt(360/7)
#     tutle.circle(50)
#     tutle.end_fill()
# tutle.done()
# coding=utf-8
# coding=utf-8
# import turtle
# import time
 
# turtle.pensize(5)
# turtle.pencolor("yellow")
# turtle.fillcolor("red")
 
# turtle.begin_fill()
# for _ in range(5):
#   turtle.forward(200)
#   turtle.right(144)
# turtle.end_fill()
# time.sleep(2)
 
# turtle.penup()
# turtle.goto(-150,-120)
# turtle.color("violet")
# turtle.write("Done", font=('Arial', 40, 'normal'))
 
# turtle.mainloop()



# radius = 25 
# area = 3.1415 * radius * radius
# print(area)
# print("{:.2f}".format(area))
# name = input("输入姓名:")
# print("%s同学,学好python,前途无量"%name)
#最美的切园
# import turtle
# for i in range(4):
#     turtle.pensize(2)
#     turtle.circle(10)
#     turtle.circle(40)
#     turtle.circle(80)
#     turtle.circle(160)




# s = 0 
# for i  in range(2):
#     print(i)
#     s += i
# print(s)


# print("{}是{}的首都".format( \
#     "北京", \
#         "中国"\
#     ))


# s = "你是谁？"
# #print(s[1:2])  #可以理解为2-1
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])

# print(s[:])

# print(s)
# #画园的操作
# import turtle
# turtle.fd(-200)
# turtle.right(90)
# turtle.circle(200)




# num = eval(input("请输入一个数字："))
# if 0 <= num <= 100:
#     print("输入的整数在0到100之间（含）")


# n = 10
# while n < 100:
#     print(n, end="")
#     n = n + 3

# print(end="")



# b = eval("1.234")
# print(b)
# a = eval("1.2+3.4")
# print(a)

# s = input("请输入一段文本")
# i = len(s) - 1
# while i >= 0:
#     print(s[i])
#     i = i - 1
    
# a = 10
# print(type(a))
# print(a)




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

# f = open("wenzhe.txt","w",encoding="utf-8")
# f.write("我爱自动化运维.\n")
# f.write("我爱网络行业..\n")
# f.write("hello world\n")
# f.close()
# f = open("wenzhe.txt", "a", encoding="utf-8")
# f.write("测试a方式写入，如果文件存在，在文件内容后最后追加写入，如果文件不存在则创建")
# f.close()


# f = open("wenzhe.txt", "rt", encoding="utf-8")
# # 以文本方式读，f.read()返回字符串对象
# data = f.read()
# print(type(data))
# print(data)
# f.close()
# f = open("wenzhe.txt", "rb")
# # 以文本方式读，f.read()返回字节对象
# data = f.read()
# print(type(data))
# print(data)
# print('将读取的字符对象解码：')
# print(data.decode('utf-8'))
# f.close()


# f = open("wenzhe.txt", "rb")
# # 以文本方式读，f.read()返回字节对象
# data = f.read()
# print(type(data))
# print(data)
# print('将读取的字符对象解码：')
# print(data.decode('utf-8'))
# f.close()

# print(f'以文本方式将Unicode字符串"{str}"写入wenzhe.txt')

# with open("wenzhe.txt", "w", encoding="gbk") as f:
#     f.write(str)

# print("以文本方式读取 wenzhe.txt 的内容")
# with open("wenzhe.txt", "r", encoding="gbk") as f:
#     print(f.read())



# #文件定位
# f = open("wenzhe.txt", "wb+")
# f.write(b"abcdefghi")
# f.seek(5)  # 移动到文件的第六个字节
# print(f.read(1))
# f.seek(-3, 2)  # 移动到文件的倒数第三字节
# print(f.read(1))





# import time

# with open('a.txt', 'rb') as f:
#     f.seek(0, 2)  # 将光标移动至文件末尾
#     while True:  # 实时显示文件新增加的内容
#         line = f.read()
#         if line:
#             print(line.decode('utf-8'), end='')
#         else:
#             time.sleep(0.2)  # 读取完毕后短暂的睡眠



print("213")