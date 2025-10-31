import qrcode

# Chave PIX de teste
pix_key = "00020126360014BR.GOV.BCB.PIX0114+5511999999995204000053039865406100.005802BR5913Teste PIX6009Sao Paulo62070503***6304"

img = qrcode.make(pix_key)
img.save("pix_qr.png")
print("QR Code PIX gerado em pix_qr.png")
