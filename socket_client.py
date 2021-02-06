import socket

# 1.创建socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.连接服务器
client.connect(("192.168.31.147", 7980))

# 3.接收数据
msg = client.recvfrom(1024)   # 阻塞方法
print("服务端回复：%s" % msg[0].decode('utf-8'))

# 4.向服务端回复
client.send("你好!".encode('utf-8'))

# 关闭
client.close()
