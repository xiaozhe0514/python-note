import urllib.request

# url = 'http://www.baidu.com'
# #http://www.baidu.com:80
# #带有的参数   
# index.html?name=goudan&password=123#lala



# response = urllib.request.urlopen(url=url)
# print(response.read().decode())    #字符串之间的转化   
image_url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fs7.sinaimg.cn%2Fbmiddle%2F60ee77c5t6ea3a2c6dd46%26690&refer=http%3A%2F%2Fs7.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1615865242&t=5d4760eccc86c506d871c22d9ad053c2'

urllib.request.urlretrieve(image_url,'chun.jpg')
