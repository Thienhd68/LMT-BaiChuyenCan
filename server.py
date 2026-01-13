import socket

# Nhập IP và Port từ bàn phím
print("=" * 50)
print("CẤU HÌNH SERVER")
print("=" * 50)

host = input("Nhập địa chỉ IP của Server (Enter = localhost): ").strip()
if not host:
    host = 'localhost'

port_input = input("Nhập Port (Enter = 12345): ").strip()
if not port_input:
    port = 12345
else:
    try:
        port = int(port_input)
        if port < 1024 or port > 65535:
            print("Port nên nằm trong khoảng 1024-65535. Sử dụng 12345 mặc định.")
            port = 12345
    except ValueError:
        print("Port không hợp lệ. Sử dụng 12345 mặc định.")
        port = 12345

# Tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Cho phép sử dụng lại địa chỉ
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    # Bind socket đến địa chỉ
    server_socket.bind((host, port))
    
    # Lắng nghe kết nối
    server_socket.listen(1)
    
    print("\n" + "=" * 50)
    print(f"SERVER ĐANG CHẠY TẠI {host}:{port}")
    print("=" * 50)
    print("Đang chờ kết nối từ client...\n")
    
    # Chấp nhận kết nối
    client_socket, client_address = server_socket.accept()
    print(f"Đã kết nối với client: {client_address}\n")
    
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
    print(f"\nTổng số message đã nhận: {message_count}")
    print("Client đã đóng kết nối")
    
except OSError as e:
    print(f"\nLỗi khi khởi động server: {e}")
    print("  Kiểm tra lại IP/Port hoặc port có thể đang được sử dụng.")
except Exception as e:
    print(f"\nLỗi: {e}")
finally:
    server_socket.close()
    print("Server đã đóng kết nối và thoát")
    print("=" * 50)