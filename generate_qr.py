import qrcode

# URL for your portfolio
url = "https://clanmokback.github.io/myportfolio/"

# Generate QR code
qr = qrcode.make(url)

# Save as image
qr.save("portfolio_qr.png")
