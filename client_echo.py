import socket

def create_client(host='localhost', port=5000):
    # 1. Tạo socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # 2. Gửi dữ liệu
    message = input("Nhập tin nhắn gửi đến server: ")
    client_socket.send(message.encode('utf-8'))

    # 3. Nhận phản hồi
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Client nhận: {response}")

    # 4. Đóng kết nối
    client_socket.close()

if __name__ == "__main__":
    create_client()
