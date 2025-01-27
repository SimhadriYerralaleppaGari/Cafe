import qrcode

# Replace with the hosted URL for your services page
url = "http://localhost:8000/src/index.html"  # Update with the actual hosted link when deployed

# Generate QR code
qr = qrcode.make(url)

# Save the QR code image
qr.save("assets/qr-code.png")

print("QR Code generated and saved in assets/qr-code.png")
