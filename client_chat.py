import socket

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Địa chỉ và cổng của server
host = 'localhost'
port = 12345

# Kết nối đến server
print(f"Đang kết nối đến server {host}:{port}...")
client_socket.connect((host, port))
print("Đã kết nối thành công!")

# Nhập message từ người dùng
message = input("Nhập message gửi đến server: ")

# Gửi message đến server
client_socket.send(message.encode('utf-8'))
print(f"Đã gửi message: {message}")

# Nhận phản hồi từ server
response = client_socket.recv(1024).decode('utf-8')
print(f"Phản hồi từ server: {response}")

# Đóng kết nối
client_socket.close()
print("Client đã đóng kết nối và thoát")