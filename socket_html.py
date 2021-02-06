import multiprocessing
import socket
import re

# 设置静态目录
HTML_SOURCE_DIR = './temp'


def handle_request(client_socket):
    """处理客户端请求"""
    request_data = client_socket.recv(1024)
    print("客户端请求:\n", request_data)
    # 处理请求数据
    request_lines = request_data.splitlines()
    for line in request_lines:
        print(line)
    # 获得url指定文件
    request_start = request_lines[0]
    file_name = re.search(r"\w+ +(/[^ ]*) ", str(request_start)).group(1)
    if (file_name == '') or (file_name == '/'):
        file_name = '/order.html'
    # 打开文件读取资源
    try:
        with open(HTML_SOURCE_DIR + file_name, "rb") as stream:
            file_content = stream.read()
    # 构造响应报文
    except OSError:
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_header = "Server: My Server\r\n"
        response_body = "The file is not found!"
    else:
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_header = "Server: My Server\r\n"
        response_body = file_content.decode('utf-8')

    response = response_start_line + response_header + "\r\n" + response_body
    print("响应数据:\n", response)
    client_socket.send(response.encode('utf-8'))    # python2不必要转
    client_socket.close()       # 结束客户端通信


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 7980))
    server.listen(128)
    print("服务器已开启!")
    while True:
        client_socket, client_address = server.accept()
        print("%s用户已连接！", client_address[0])
        handle_client_process = multiprocessing.Process(target=handle_request, args=(client_socket,))
        handle_client_process.start()

        client_socket.close()
