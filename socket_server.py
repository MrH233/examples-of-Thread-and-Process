import socket
import threading

# 1.创建server 套接字
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.绑定本地端口
server.bind(('192.168.31.147', 7980))

# 3.监听
server.listen()

# 4.等待接收客户端的连接
print("服务器已启动，等待连接……")
client, address = server.accept()
print("%s 已连接！" % str(address))

# 5.向客户端发送消息
client.send("Connect successfully!".encode('utf-8'))

# 6.等待客户端发来消息
msg = client.recvfrom(1024)
print("客户端回复：%s" % msg[0].decode('utf-8'))

client.send("连接关闭！".encode('utf-8'))
client.close()
server.close()
