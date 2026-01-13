import socket

# Nhập IP và Port từ bàn phím
print("=" * 50)
print("CẤU HÌNH CLIENT")
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
            print("⚠ Port nên nằm trong khoảng 1024-65535. Sử dụng 12345 mặc định.")
            port = 12345
    except ValueError:
        print("⚠ Port không hợp lệ. Sử dụng 12345 mặc định.")
        port = 12345

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Kết nối đến server
    print("\n" + "=" * 50)
    print(f"ĐANG KẾT NỐI ĐẾN SERVER {host}:{port}...")
    print("=" * 50)
    client_socket.connect((host, port))
    print("Đã kết nối thành công!\n")
    
    print("HƯỚNG DẪN:")
    print("- Nhập message để gửi đến server")
    print("- Nhập '0' để thoát chương trình")
    print("=" * 50 + "\n")
    
    message_count = 0
    
    # Vòng lặp gửi message
    while True:
        # Nhập message từ người dùng
        message = input("Bạn: ")
        
        # Gửi message đến server
        client_socket.send(message.encode('utf-8'))
        message_count += 1
        
        # Kiểm tra lệnh thoát
        if message.strip() == "0":
            # Nhận phản hồi cuối cùng từ server
            response = client_socket.recv(1024).decode('utf-8')
            print(f"\n{response}\n")
            break
        
        # Nhận phản hồi từ server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server: {response}\n")
    
    print("=" * 50)
    print(f"Tổng số message đã gửi: {message_count}")
    print("Client đã đóng kết nối và thoát")
    print("=" * 50)
    
except ConnectionRefusedError:
    print("\nLỗi: Không thể kết nối đến server!")
    print(f"  Kiểm tra lại địa chỉ {host}:{port}")
    print("  Hãy đảm bảo server đã chạy trước.")
except socket.gaierror:
    print("\nLỗi: Địa chỉ IP không hợp lệ!")
    print(f"  Không thể phân giải địa chỉ: {host}")
except Exception as e:
    print(f"\nLỗi: {e}")
finally:
    # Đóng kết nối
    client_socket.close()