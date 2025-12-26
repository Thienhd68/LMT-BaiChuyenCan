import socket

def create_server(host='localhost', port=5000):
    # 1. Tạo socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Bind địa chỉ
    server_socket.bind((host, port))

    # 3. Lắng nghe kết nối
    server_socket.listen(1)
    print(f"Server đang lắng nghe tại {host}:{port}")

    # 4. Chấp nhận kết nối
    client_socket, client_address = server_socket.accept()
    print(f"Kết nối từ {client_address}")

    # 5. Nhận dữ liệu
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Server nhận được: {data}")

    # 6. Gửi lại nguyên văn
    response = f"Server đã nhận: {data}"
    client_socket.send(response.encode('utf-8'))

    # 7. Đóng kết nối
    client_socket.close()
    server_socket.close()
    print("Server đã đóng kết nối")

if __name__ == "__main__":
    create_server()
