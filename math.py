#自动生成两三位数乘一位数
import  random

i = 1
while i <= 30:
    a = random.randint(2,9)
    b = random.randint(3,8)
    c = random.randint(1,9)
    # print(a*b,"×",b,"=")
    print("(",b,"+",c,")","x",b,"=")
    i += 1










