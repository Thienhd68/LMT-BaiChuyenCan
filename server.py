import socket

# Tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Địa chỉ và cổng
host = 'localhost'
port = 12345

# Bind socket đến địa chỉ
server_socket.bind((host, port))

# Lắng nghe kết nối
server_socket.listen(1)

print("=" * 50)
print(f"SERVER ĐANG CHẠY TẠI {host}:{port}")
print("=" * 50)
print("Đang chờ kết nối từ client...\n")

# Chấp nhận kết nối
client_socket, client_address = server_socket.accept()
print(f"✓ Đã kết nối với client: {client_address}\n")

# Vòng lặp nhận message
message_count = 0
while True:
    try:
        # Nhận dữ liệu từ client
        data = client_socket.recv(1024).decode('utf-8')
        
        if not data:
            print("Client đã ngắt kết nối")
            break
        
        # Kiểm tra nếu client gửi "0" để thoát
        if data.strip() == "0":
            print("\n" + "=" * 50)
            print("Client đã gửi lệnh thoát (0)")
            print("=" * 50)
            # Gửi xác nhận thoát
            response = "Server: Đã nhận lệnh thoát. Tạm biệt!"
            client_socket.send(response.encode('utf-8'))
            break
        
        message_count += 1
        print(f"[Message #{message_count}] Client: {data}")
        
        # Gửi phản hồi cho client
        response = f"Server đã nhận message #{message_count}: '{data}'"
        client_socket.send(response.encode('utf-8'))
        print(f"[Phản hồi #{message_count}] Server: Đã gửi xác nhận\n")
        
    except Exception as e:
        print(f"Lỗi: {e}")
        break

# Đóng kết nối
client_socket.close()
server_socket.close()
print(f"\n✓ Tổng số message đã nhận: {message_count}")
print("✓ Server đã đóng kết nối và thoát")
print("=" * 50)