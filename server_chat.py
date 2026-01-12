import socket

# Tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Địa chỉ và cổng
host = 'localhost'
port = 12345

# Bind socket đến địa chỉ
server_socket.bind((host, port))

# Lắng nghe kết nối (tối đa 1 client)
server_socket.listen(1)

print(f"Server đang chạy tại {host}:{port}")
print("Đang chờ kết nối từ client...")

# Chấp nhận kết nối
client_socket, client_address = server_socket.accept()
print(f"Đã kết nối với client: {client_address}")

# Nhận dữ liệu từ client
data = client_socket.recv(1024).decode('utf-8')
print(f"Message từ client: {data}")

# Gửi phản hồi cho client
response = f"Server đã nhận message: '{data}'"
client_socket.send(response.encode('utf-8'))
print("Đã gửi phản hồi cho client")

# Đóng kết nối
client_socket.close()
server_socket.close()
print("Server đã đóng kết nối và thoát")