import socket

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Địa chỉ và cổng của server
host = 'localhost'
port = 12345

try:
    # Kết nối đến server
    print("=" * 50)
    print(f"ĐANG KẾT NỐI ĐẾN SERVER {host}:{port}...")
    print("=" * 50)
    client_socket.connect((host, port))
    print("✓ Đã kết nối thành công!\n")
    
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
    print(f"✓ Tổng số message đã gửi: {message_count}")
    print("✓ Client đã đóng kết nối và thoát")
    print("=" * 50)
    
except ConnectionRefusedError:
    print("\n✗ Lỗi: Không thể kết nối đến server!")
    print("  Hãy đảm bảo server đã chạy trước.")
except Exception as e:
    print(f"\n✗ Lỗi: {e}")
finally:
    # Đóng kết nối
    client_socket.close()