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

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 12345
SHIFT = 1

try:
    print("=" * 50)
    print(f"CLIENT MÃ HÓA CAESAR CIPHER (SHIFT={SHIFT})")
    print(f"Đang kết nối đến server {host}:{port}...")
    print("=" * 50)
    client_socket.connect((host, port))
    print("Đã kết nối thành công!\n")
    
    print("HƯỚNG DẪN:")
    print("- Nhập message để gửi đến server")
    print("- Message sẽ được MÃ HÓA trước khi gửi")
    print("- Nhập '0' để thoát chương trình")
    print("=" * 50 + "\n")
    
    message_count = 0
    
    while True:
        message = input("Bạn: ")
        encrypted_message = caesar_cipher(message, SHIFT, decrypt=False)
        
        print(f"  → [Gốc]: {message}")
        print(f"  → [Mã hóa]: {encrypted_message}")
        
        client_socket.send(encrypted_message.encode('utf-8'))
        message_count += 1
        
        if message.strip() == "0":
            encrypted_response = client_socket.recv(1024).decode('utf-8')
            decrypted_response = caesar_cipher(encrypted_response, SHIFT, decrypt=True)
            
            print(f"  ← [Nhận - Mã hóa]: {encrypted_response}")
            print(f"  ← [Giải mã]: {decrypted_response}\n")
            break
        
        encrypted_response = client_socket.recv(1024).decode('utf-8')
        decrypted_response = caesar_cipher(encrypted_response, SHIFT, decrypt=True)
        
        print(f"  ← [Nhận - Mã hóa]: {encrypted_response}")
        print(f"  ← [Giải mã]: {decrypted_response}\n")
    
    print("=" * 50)
    print(f"Tổng số message đã gửi: {message_count}")
    print("Client đã đóng kết nối và thoát")
    print("=" * 50)
    
except ConnectionRefusedError:
    print("\nLỗi: Không thể kết nối đến server!")
    print("  Hãy đảm bảo server đã chạy trước.")
except Exception as e:
    print(f"\nLỗi: {e}")
finally:
    client_socket.close()