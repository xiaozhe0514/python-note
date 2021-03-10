import paramiko

# 建立一个sshclient对象
ssh = paramiko.SSHClient()
# 将信任的主机自动加入到host_allow列表，须放在connect方法前面
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 调用connect方法连接服务器
ssh.connect(hostname="222.194.118.17", port=22, username="root", password="root")
# 执行命令
stdin, stdout, stderr = ssh.exec_command("echo `date` && df -hl")
# 结果放到stdout中，如果有错误将放到stderr中
print(stdout.read().decode('utf-8'))
# 
returncode = stdout.channel.recv_exit_status()
print("returncode:",returncode)
# 关闭连接
ssh.close()





import paramiko
# 指定本地的RSA私钥文件,如果建立密钥对时设置的有密码，提供password参数即可，如无则不提供
pkey = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
#建立连接
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='222.194.118.17',
            port=22,
            username='root',
            pkey=pkey)
# 执行命令
stdin, stdout, stderr = ssh.exec_command('echo `date` && df -hl')
# 输出
print(stdout.read().decode('utf-8'))
# 关闭连接
ssh.close()




import paramiko
#获取Transport实例
tran = paramiko.Transport("222.194.118.17",22)
#连接SSH服务端
tran.connect(username = "root", password = "root")
#获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)
#设置上传的本地/远程文件路径
localpath="123.txt" ##本地文件路径
remotepath="/opt/123.txt" ##上传对象保存的文件路径
#执行上传动作
sftp.put(localpath,remotepath)
tran.close()



import paramiko
#获取Transport实例
tran = paramiko.Transport("222.194.118.17",22)
#连接SSH服务端
tran.connect(username = "root", password = "root")
#获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)
#设置上传的本地/远程文件路径
localpath="456.txt" ##本地文件路径
remotepath="/opt/456.txt" ##下载对象保存的文件路径
#执行下载动作
sftp.get(remotepath,localpath)
tran.close()





import paramiko
# 指定本地的RSA私钥文件,如果建立密钥对时设置的有密码，提供password参数即可，如无则不提供
pkey = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
#建立连接
tran = paramiko.Transport(('222.194.118.17',22))
tran.connect(username='root',pkey=pkey)
#获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)
#设置上传的本地/远程文件路径
localpath="123.txt" ##本地文件路径
remotepath="/opt/789.txt" ##上传对象保存的文件路径
#执行上传动作
sftp.put(localpath,remotepath)
# 关闭连接
tran.close()





import paramiko
# 指定本地的RSA私钥文件,如果建立密钥对时设置的有密码，提供password参数即可，如无
#则不提供
pkey = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
#建立连接
tran = paramiko.Transport(('222.194.118.17',22))
tran.connect(username='root',pkey=pkey)
#获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)
#设置上传的本地/远程文件路径
localpath="012.txt" ##本地文件路径
remotepath="/opt/789.txt" ##下载对象保存的文件路径
#执行下载动作
sftp.get(remotepath,localpath)
# 关闭连接
tran.close()


