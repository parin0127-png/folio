import qrcode

def qr_generator(data: str, filename: str = "qr.png"):
    """generate a qr code image from any text, url, or data input"""
    try:
        img = qrcode.make(data)
        img.save(filename)
    except Exception as e:
        return f"> QR generator failed: {str(e)}"


