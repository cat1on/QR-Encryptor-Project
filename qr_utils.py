import qrcode
import tkinter as tk
from tkinter import filedialog
import datetime
from PIL import Image

def create_qr(data: str) -> Image.Image:
    
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def save_qr(img: Image.Image, root: tk.Tk) -> None:

    filename = datetime.datetime.now().strftime("qr_%Y-%m-%d_%H-%M-%S.png")
    
    file_path = filedialog.asksaveasfilename(
        parent=root,
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        initialfile=filename,
        title="Сохранить QR-код"
    )

    if file_path:
        img.save(file_path)
        print(f"\nQR-код сохранён: {file_path}")
    else:
        print("\nСохранение отменено")