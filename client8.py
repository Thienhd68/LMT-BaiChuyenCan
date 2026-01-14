import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 12345

try:
    print("=" * 50)
    print(f"CLIENT XÁC THỰC - KẾT NỐI ĐẾN {host}:{port}")
    print("=" * 50)
    client_socket.connect((host, port))
    print("Đã kết nối thành công!\n")
    
    # Xác thực
    print("=" * 50)
    print("XÁC THỰC")
    print("=" * 50)
    password = input("Nhập mật khẩu: ")
    
    client_socket.send(password.encode('utf-8'))
    print(f"Đã gửi mật khẩu đến server...")
    
    auth_result = client_socket.recv(1024).decode('utf-8')
    
    if auth_result == "AUTH_SUCCESS":
        print("\n" + "=" * 50)
        print("XÁC THỰC THÀNH CÔNG!")
        print("=" * 50)
        print("\nHƯỚNG DẪN:")
        print("- Nhập message để gửi đến server")
        print("- Nhập '0' để thoát chương trình")
        print("=" * 50 + "\n")
        
        message_count = 0
        
        while True:
            message = input("Bạn: ")
            
            client_socket.send(message.encode('utf-8'))
            message_count += 1
            
            if message.strip() == "0":
                response = client_socket.recv(1024).decode('utf-8')
                print(f"\n{response}\n")
                break
            
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Server: {response}\n")
        
        print("=" * 50)
        print(f"Tổng số message đã gửi: {message_count}")
        print("Client đã đóng kết nối và thoát")
        print("=" * 50)
        
    elif auth_result == "AUTH_FAILED":
        print("\n" + "=" * 50)
        print("XÁC THỰC THẤT BẠI!")
        print("Mật khẩu không đúng. Kết nối bị ngắt.")
        print("=" * 50)
    else:
        print("\nLỗi: Phản hồi không xác định từ server")
    
except ConnectionRefusedError:
    print("\nLỗi: Không thể kết nối đến server!")
    print("  Hãy đảm bảo server đã chạy trước.")
except Exception as e:
    print(f"\nLỗi: {e}")
finally:
    client_socket.close()