# try:
#     num = int(input("请输入数字:"))
# except:
#     print("请输入正确的数字")
#     pass

# print(int(input("请输入数字:")))


# try:
# # 1. 提示用户输入整数
#     num = int(input("输入一个整数"))

# # 2. 使用数字8 处理用户输入的整数并且输出
#     result = 8 /num

#     print(result)
# except ZeroDivisionError:
#     print("除0错误")
# except ValueError:
#     print("重新输入数字 仅仅能输入数字")
# except Exception as result:
#     print("未知错误%s" % result)
# else:
#     print("尝试成功")
#     pass

# finally:
#     print("无论是否出现错误都会执行的代码")
# print("-" * 50 )

# def demo1():
#     return int(input("请输入一个整数"))


# def demo2():
#     return demo1

# #利用异常的传递性 在主程序中捕获异常

# try:
#     print(demo1())
# except ValueError:
#     print("请输入正确的整数")
# except Exception as result:
#     print("未知捕获%s" % result)

def input_password():
    # 1.提示用户输入密码
    pwd  = input("请出入密码：")
    # 2. 判断密码长度 >= 8 符合规则  返回用户输入的密码 
    if len(pwd) >= 8:
        return pwd


    # 3. 如果小于8  主动抛出异常信息  *args 多值元组信息  使用异常对象字符串进行判断
    print("主动抛出异常")
    #创建异常或额捕获异常  
    ex  =  Exception("密码长度不够使用")
    raise  ex




# 提示用户输入密码
try:

    print(input_password())
except Exception as result:
    print(result)
















