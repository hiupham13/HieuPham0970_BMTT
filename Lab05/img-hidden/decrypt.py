import sys
from PIL import Image

import os
from PIL import Image

def decode_image(encoded_image_path):
    if not os.path.exists(encoded_image_path):
        raise FileNotFoundError(f"File not found: {encoded_image_path}")
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ''
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]

    message = ''
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if char == '\0':
            break
        message += char
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image>")
        return
    encode_image_path = sys.argv[1]
    secret_message = decode_image(encode_image_path)
    print("Decoded message:", secret_message)

if __name__ == "__main__":
    main()