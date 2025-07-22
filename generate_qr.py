import qrcode

url = "https://clanmokback.github.io/myportfolio/"

qr = qrcode.make(url)

qr.save("portfolio_qr.png")
