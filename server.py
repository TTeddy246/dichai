import socket
import requests


# Hàm dịch văn bản từ tiếng Việt sang tiếng Anh bằng Google Translate API
def translate_vietnamese_to_english(text):
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=vi&tl=en&dt=t&q=" + text
    response = requests.get(url)
    translation = response.json()
    translated_text = translation[0][0][0]
    return translated_text


# Khởi tạo server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))  # Sử dụng địa chỉ IP và cổng của bạn
server.listen(5)

print("Đang lắng nghe kết nối từ client...")
client_socket, client_address = server.accept()

while True:
    data = client_socket.recv(1024).decode("utf-8")
    if not data:
        break

    translated_text = translate_vietnamese_to_english(data)
    client_socket.send(translated_text.encode("utf-8"))

client_socket.close()
server.close()
