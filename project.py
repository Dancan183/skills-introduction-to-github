import qrcode

data = "I Love You Lilo!"

qr = qrcode.make(data)

qr.save("qrcode.png")

print("qr code created successfully")