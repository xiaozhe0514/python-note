# # # 1. 打开 - 文件名 需要注意大小写   

# # file  = open("D:\\Project\\vscode\\python-note\\README")

# # # 2. 读取
# # text = file.read()
# # print(text)

# # # 3. 关闭    
# # file.close()



# # 1. 打开文件
# #open默认是只读进行打开的  
# file  = open("D:\\Project\\vscode\\python-note\\README","a")
# # w 会覆盖原来的文件 注意  还有追加的方式进行写的操作    
# #    r w a 读写的方式进行读写文件   

# #提示频繁的移动文件指针  会影响文件的读写效率   开发中更多的时候会以只读 只写的方式进行操作文件  










# # 2. 写入文件

# file.write("132 hello\n")





# # 3. 关闭文件
# file.close()



# #

# file  = open("D:\\Project\\vscode\\python-note\\README")


# while True:
#     text = file.readline()
#     if not text:
#         break
#     print(text,end=" ")

# file.close()
file_read  = open("D:\\Project\\vscode\\python-note\\README")
file_write = open("D:\\Project\\vscode\\python-note\\README2","w")
# 1. 打开文件
while True:
    #读取一行的内容进行操作  
    text = file_read.readline()
    if not text:
        break

    file_write.write(text)



# 2. 读写操作




# 3. 关闭文件

file_read.close()
file_write.close()
