import socket

# Tạo socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Địa chỉ và cổng của server
host = 'localhost'
port = 12345

try:
    # Kết nối đến server
    print(f"CLIENT - CHUYỂN ĐỔI SỐ THÀNH CHỮ")
    print(f"Đang kết nối đến server {host}:{port}...")
    client_socket.connect((host, port))
    print("✓ Đã kết nối thành công!\n")
    
    print("HƯỚNG DẪN:")
    print("- Nhập một số tự nhiên từ 0 đến 10")
    print("- Server sẽ chuyển đổi số thành chữ")
    print("- Nhập 'Quit' để thoát chương trình")
    
    request_count = 0
    
    # Vòng lặp gửi số
    while True:
        # Nhập số từ người dùng
        user_input = input("Nhập số (0-10) hoặc 'Quit': ").strip()
        
        # Gửi dữ liệu đến server
        client_socket.send(user_input.encode('utf-8'))
        request_count += 1
        
        # Kiểm tra lệnh thoát
        if user_input.lower() == "quit":
            # Nhận phản hồi cuối cùng từ server
            response = client_socket.recv(1024).decode('utf-8')
            print(f"\n{response}\n")
            break
        
        # Nhận phản hồi từ server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"→ Server: {response}\n")
    
    print(f"✓ Tổng số request đã gửi: {request_count}")
    print("✓ Client đã đóng kết nối và thoát")
    
except ConnectionRefusedError:
    print("\n✗ Lỗi: Không thể kết nối đến server!")
    print("  Hãy đảm bảo server đã chạy trước.")
except Exception as e:
    print(f"\n✗ Lỗi: {e}")
finally:
    # Đóng kết nối
    client_socket.close()