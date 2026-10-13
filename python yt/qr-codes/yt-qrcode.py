import qrcode
qr=qrcode.make("https://www.youtube.com/@AnsariAbdulla-o3g")
qr.save("my-qrcode.png")
print("QrCode generated successfully.")