import base64

def manin():
    input_string = input("Nhap thong tin can ma hoa: ")
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')

    with open("data.txt", "w") as file:
        file.write(encoded_string)
    print("Da ma hoa va luu vao file data.txt")

if __name__ == "__main__":
    manin()