import qrcode

# img = qrcode.make("Hello")
# img.save("mycode.png")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('POS URL')
qr.make(fit=True)

img = qr.make_image(fill_color="pink", back_color="green")
img.save("harshiv.png")