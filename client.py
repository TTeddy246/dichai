import socket

# Khởi tạo client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))  # Sử dụng địa chỉ IP và cổng của server

while True:
    user_input = input("Nhập văn bản tiếng Việt (hoặc 'quit' để thoát): ")
    if user_input.lower() == "quit":
        break

    client.send(user_input.encode("utf-8"))
    response = client.recv(1024).decode("utf-8")
    print(f"Kết quả dịch sang tiếng Anh: {response}")

client.close()
