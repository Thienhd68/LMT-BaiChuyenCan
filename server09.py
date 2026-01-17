import socket
import time

# Hàm chuyển đổi số thành chữ
def number_to_word(num):
    """Chuyển số từ 0-10 thành chữ tiếng Việt"""
    words = {
        0: "không",
        1: "một",
        2: "hai",
        3: "ba",
        4: "bốn",
        5: "năm",
        6: "sáu",
        7: "bảy",
        8: "tám",
        9: "chín",
        10: "mười"
    }
    return words.get(num, None)

# Tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Địa chỉ và cổng
host = 'localhost'
port = 12345

# Bind socket đến địa chỉ
server_socket.bind((host, port))

# Lắng nghe kết nối
server_socket.listen(1)

print(f"SERVER CHUYỂN ĐỔI SỐ THÀNH CHỮ (CÓ DELAY)")
print(f"Đang chạy tại {host}:{port}")
print("Đang chờ kết nối từ client...\n")

# Chấp nhận kết nối
client_socket, client_address = server_socket.accept()
print(f"Đã kết nối với client: {client_address}\n")

# Vòng lặp xử lý request
request_count = 0

while True:
    try:
        # Nhận dữ liệu từ client
        data = client_socket.recv(1024).decode('utf-8').strip()
        
        if not data:
            print("Client đã ngắt kết nối")
            break
        
        # Kiểm tra lệnh thoát
        if data.lower() == "quit":
            print("Client đã gửi lệnh QUIT")
            response = "Server: Đã nhận lệnh thoát. Tạm biệt!"
            client_socket.send(response.encode('utf-8'))
            break
        
        request_count += 1
        print(f"[Request #{request_count}] Client gửi: '{data}'")
        
        # Thử chuyển đổi thành số
        try:
            number = int(data)
            
            # Kiểm tra phạm vi 0-10
            if 0 <= number <= 10:
                # DELAY THEO SỐ GIÂY TƯƠNG ỨNG
                print(f"[Processing] Đang xử lý... (delay {number} giây)")
                time.sleep(number)  # Delay theo giá trị số nhập vào
                
                word = number_to_word(number)
                response = f"Số {number} đọc là: {word}"
                print(f"[Response #{request_count}] Server: {response}")
            else:
                response = f"Lỗi: Số {number} nằm ngoài phạm vi (0-10)"
                print(f"[Response #{request_count}] Server: {response}")
        
        except ValueError:
            response = f"Lỗi: '{data}' không phải là số hợp lệ"
            print(f"[Response #{request_count}] Server: {response}")
        
        # Gửi phản hồi cho client
        client_socket.send(response.encode('utf-8'))
        print()
        
    except Exception as e:
        print(f"Lỗi: {e}")
        break

# Đóng kết nối
client_socket.close()
server_socket.close()
print(f"\nTổng số request đã xử lý: {request_count}")
print("Server đã đóng kết nối và thoát")