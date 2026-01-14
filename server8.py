import socket

# Mật khẩu xác thực
PASSWORD = "pass1234"

# Tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = 'localhost'
port = 12345

server_socket.bind((host, port))
server_socket.listen(1)

print("=" * 50)
print(f"SERVER XÁC THỰC - ĐANG CHẠY TẠI {host}:{port}")
print(f"Mật khẩu server: {PASSWORD}")
print("=" * 50)
print("Đang chờ kết nối từ client...\n")

client_socket, client_address = server_socket.accept()
print(f"Đã kết nối với client: {client_address}")
print("Đang chờ xác thực...\n")

try:
    # Nhận mật khẩu từ client
    password_input = client_socket.recv(1024).decode('utf-8').strip()
    
    print(f"[Xác thực] Client gửi mật khẩu: {password_input}")
    
    # Kiểm tra mật khẩu
    if password_input == PASSWORD:
        print("[Xác thực] Mật khẩu đúng!")
        
        client_socket.send("AUTH_SUCCESS".encode('utf-8'))
        print("[Xác thực] Đã gửi xác nhận thành công cho client\n")
        print("=" * 50)
        print("BẮT ĐẦU PHIÊN CHAT")
        print("=" * 50 + "\n")
        
        # Bắt đầu chat
        message_count = 0
        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                
                if not data:
                    print("Client đã ngắt kết nối")
                    break
                
                if data.strip() == "0":
                    print("\n" + "=" * 50)
                    print("Client đã gửi lệnh thoát (0)")
                    print("=" * 50)
                    response = "Server: Da nhan lenh thoat. Tam biet!"
                    client_socket.send(response.encode('utf-8'))
                    break
                
                message_count += 1
                print(f"[Message #{message_count}] Client: {data}")
                
                response = f"Server da nhan message #{message_count}: '{data}'"
                client_socket.send(response.encode('utf-8'))
                print(f"[Phan hoi #{message_count}] Server: Da gui xac nhan\n")
                
            except Exception as e:
                print(f"Loi: {e}")
                break
        
        print(f"\nTong so message da nhan: {message_count}")
        
    else:
        print(f"[Xác thực] Mật khẩu sai!")
        print(f"[Xác thực] Client nhập: '{password_input}' (Mong đợi: '{PASSWORD}')")
        
        client_socket.send("AUTH_FAILED".encode('utf-8'))
        print("[Xác thực] Đã gửi thông báo thất bại và ngắt kết nối\n")

except Exception as e:
    print(f"Loi: {e}")
finally:
    client_socket.close()
    server_socket.close()
    print("Server đã đóng kết nối và thoát")
    print("=" * 50)