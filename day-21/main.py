"""
Day 21 - QRCode Generator
"""

import qrcode


def generate(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR Code has saved to {filename}")


if __name__ == "__main__":
    data = input("Enter a text/url: ")
    generate(data)
