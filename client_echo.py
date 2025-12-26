import socket

def create_client(host='localhost', port=5000):
    # 1. Tạo socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Kết nối đến server
    client_socket.connect((host, port))
    print(f"Đã kết nối đến {host}:{port}")

    # 3. Gửi dữ liệu
    message = "Hello World"
    client_socket.send(message.encode('utf-8'))
    print(f"Client gửi: {message}")

    # 4. Nhận phản hồi
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Client nhận: {response}")

    # 5. Đóng kết nối
    client_socket.close()

if __name__ == "__main__":
    create_client()
