# import flask
# import requests
# import gunicorn
# import socket  
# import threading

# from main import app
# from pydantic import BaseModel




# def send_alarm_server(send_data):
#     server_address = ('127.0.0.1', 9091)      ###地址   端口
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.connect(server_address)
#         sock.sendall(send_data.encode('utf-8'))    ###字节类型
#         rec_data = sock.recv(255)                  ###限制字节数

#         if rec_data:
#             print(rec_data.decode('utf-8'))

#     except Exception as e:                          ###监听异常
#         print(f"Error: {e}")                        ###打印异常信息
#     finally:
#         sock.close()                                ###关闭套接字
# def fd_hangue(fd):
#     busso=fd.recv(255)
#     if busso:
#         meace = busso.decode('utf-8')
#         print("/r\n"+ meace)
#         fd.close()

import socket
import threading
from fastapi import FastAPI

app = FastAPI()

HALO_S_PORT = 9090

def send_alarm_server(send_data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sclient:
            sclient.connect(('127.0.0.1', 9091))
            sclient.sendall(send_data.encode('utf-8'))
            rec_data = sclient.recv(255)
            if rec_data:
                print(rec_data.decode('utf-8'))
    except Exception as e:
        print(f"Error sending alarm server: {e}")

def handle_request(client_socket, client_address):
    print(f"\nConnection from {client_address}")

    # 接收数据
    buffer = client_socket.recv(8192)
    if buffer:
        request_line = buffer.decode('utf-8')
        print(f"Request: {request_line}")

        send_alarm_server(request_line)

        # 解析请求
        first_line = request_line.splitlines()[0]
        method, path, _ = first_line.split(' ')

        print(f"Method: {method}, Path: {path}")

        # 处理 GET 和 HEAD 请求
        if method.upper() not in ['GET', 'HEAD']:
            print("Not GET or HEAD method.")
            client_socket.close()
            return

        # TODO: 解析请求路径并处理
        # 仅做示例，假设使用 '/api/word=' 进行后续处理
        if path.startswith('/api/word='):
            search_word = path[len('/api/word='):]

            # 假设这里是调用外部函数进行词汇处理
            ex_words = f"Explanations for {search_word}"  # 示例返回值
            
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                "Connection: close\r\n\r\n"
                + ex_words
            )
            client_socket.sendall(response.encode('utf-8'))
        else:
            print("Cannot parse request URL.")
    
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', HALO_S_PORT))
    server_socket.listen(5)
    print(f"Server listening on port {HALO_S_PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=handle_request, args=(client_socket, client_address)).start()

if __name__ == "__main__":           
    threading.Thread(target=start_server).start()






