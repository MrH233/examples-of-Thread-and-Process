import socket
import threading


def recv(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(f"\n对方回复:{recv_data[0].decode('utf-8')}")


def send(udp_socket, dest_ip, dest_port):
    while True:
        send_data = input("请输入要发送的数据:")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def main():
    """完成UDP聊天器的整体控制(扔包式网络通信)"""
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定本地信息
    udp_socket.bind(("192.168.31.147", 7890))
    # 3.获取对方信息
    dest_ip = input("请输入对方ip：")
    dest_port = int(input("请输入对方port："))
    # 4.创建线程
    t_recv = threading.Thread(target=recv, args=(udp_socket,))
    t_send = threading.Thread(target=send, args=(udp_socket, dest_ip, dest_port))

    t_recv.start()
    t_send.start()


if __name__ == '__main__':
    main()
