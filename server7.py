import socket

# Hàm mã hóa/giải mã Caesar Cipher
def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result

# Tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = 'localhost'
port = 12345
SHIFT = 1

server_socket.bind((host, port))
server_socket.listen(1)

print("=" * 50)
print(f"SERVER MÃ HÓA CAESAR CIPHER (SHIFT={SHIFT})")
print(f"Đang chạy tại {host}:{port}")
print("=" * 50)
print("Đang chờ kết nối từ client...\n")

client_socket, client_address = server_socket.accept()
print(f"Đã kết nối với client: {client_address}\n")

message_count = 0
while True:
    try:
        encrypted_data = client_socket.recv(1024).decode('utf-8')
        
        if not encrypted_data:
            print("Client đã ngắt kết nối")
            break
        
        decrypted_data = caesar_cipher(encrypted_data, SHIFT, decrypt=True)
        
        print(f"[Nhận được - MÃ HÓA]: {encrypted_data}")
        print(f"[Giải mã thành]: {decrypted_data}")
        
        if decrypted_data.strip() == "0":
            print("\n" + "=" * 50)
            print("Client đã gửi lệnh thoát (0)")
            print("=" * 50)
            
            response = "Server: Đã nhận lệnh thoát. Tạm biệt!"
            encrypted_response = caesar_cipher(response, SHIFT, decrypt=False)
            
            print(f"[Gửi - GỐC]: {response}")
            print(f"[Gửi - MÃ HÓA]: {encrypted_response}")
            
            client_socket.send(encrypted_response.encode('utf-8'))
            break
        
        message_count += 1
        response = f"#{message_count}: '{decrypted_data}'"
        encrypted_response = caesar_cipher(response, SHIFT, decrypt=False)
        
        print(f"[Phản hồi - GỐC]: {response}")
        print(f"[Phản hồi - MÃ HÓA]: {encrypted_response}")
        print()
        
        client_socket.send(encrypted_response.encode('utf-8'))
        
    except Exception as e:
        print(f"Lỗi: {e}")
        break

client_socket.close()
server_socket.close()
print(f"\nTổng số message đã nhận: {message_count}")
print("Server đã đóng kết nối và thoát")
print("=" * 50)