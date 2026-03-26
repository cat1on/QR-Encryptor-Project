import os
import sys
import tkinter as tk
from tkinter import messagebox
from encoder import encrypt_text
from qr_utils import create_qr, save_qr
from PIL import ImageTk
from strings import Strings


is_hidden = True

def resourse_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def encrypt_action():
    
    passphrase = entry_passphrase.get()
    plaintext = text_input.get("1.0", tk.END).strip()

    if passphrase == "":
        messagebox.showwarning(Strings.ERROR_KEY_PHRASE)
        return
    
    if plaintext == "":
        messagebox.showwarning(Strings.ERROR_ENCRYPT_TEXT)
        return

    encrypted_payload = encrypt_text(passphrase, plaintext)
    img = create_qr(encrypted_payload)
    img = img.resize((250,250))
    root.qr_img = img
    photo = ImageTk.PhotoImage(img)
    qr_label.config(image=photo)
    qr_label.image = photo


    result_output.config(state="normal")
    result_output.delete("1.0", tk.END)
    result_output.insert(tk.END, encrypted_payload)
    result_output.config(state="disabled")

    button_saveqr.pack(pady=20)

def save_qr_action():
    result_output.config(state="normal")
    encrypted_payload = result_output.get("1.0", tk.END).strip()
    result_output.config(state="disabled")

    if not hasattr(root, "qr_img"):
        messagebox.showwarning(Strings.ERROR_FIRST_ENCRYPT)
        return
    
    save_qr(root.qr_img, root)
    show_status(Strings.SAVED_QRCODE)

def copy_json_action():
    result_output.config(state="normal")
    encrypted_payload = result_output.get("1.0", tk.END).strip()
    result_output.config(state="disabled")

    if encrypted_payload == "":
        messagebox.showwarning(Strings.ERROR_FIRST_ENCRYPT)
        return
    
    root.clipboard_clear()
    root.clipboard_append(encrypted_payload)
    show_status_copy(Strings.COPY)

def toggle_passphrase():
    global is_hidden

    if is_hidden:
        entry_passphrase.config(show="")
        button_toggle.config(text=Strings.HIDE)
        is_hidden = False
    else:
        entry_passphrase.config(show="*")
        button_toggle.config(text=Strings.SHOW)
        is_hidden = True

def show_status(message: str):
    status_label.config(text=message)
    root.after(2000, lambda: status_label.config(text=""))

def show_status_copy(message: str):
    status_copy.config(text=message)
    root.after(2000, lambda: status_copy.config(text=""))

root = tk.Tk()
root.title(Strings.TITLE_TEXT)
root.geometry("800x650")
root.resizable(False,False)
icon_path = resourse_path("icon.ico")
root.iconbitmap(icon_path)

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

left_frame = tk.Frame(main_frame)
left_frame.pack(side="left", padx=20, pady=10)

right_frame = tk.Frame(main_frame)
right_frame.pack(side="left", padx=20, pady=10)

label_passphrase = tk.Label(left_frame, text=Strings.PASSPHRASE_LABEL_TEXT)
label_passphrase.pack(pady=(20,5))

frame_passphrase = tk.Frame(left_frame)
frame_passphrase.pack()

entry_passphrase = tk.Entry(frame_passphrase, width=35, show="*")
entry_passphrase.pack(side="left")

button_toggle = tk.Button(frame_passphrase, text=Strings.SHOW, command=toggle_passphrase)
button_toggle.pack(side="left", padx=5)

label_text = tk.Label(left_frame, text=Strings.TEXT_FOR_ENCRYPT)
label_text.pack(pady=(20,5))

text_input = tk.Text(left_frame, width=40, height=8)
text_input.pack()

button_encrypt = tk.Button(left_frame, text=Strings.ENCRYPT, command=encrypt_action)
button_encrypt.pack(pady=20)

label_result = tk.Label(left_frame, text=Strings.ENCRYPT_JSON)
label_result.pack(pady=(10,5))

result_output = tk.Text(left_frame, width=50, height=8)
result_output.pack()

status_copy = tk.Label(left_frame, text="")
status_copy.pack()
button_copy = tk.Button(left_frame, text=Strings.COPY_JSON, command=copy_json_action)
button_copy.pack(pady=20)

qr_label = tk.Label(right_frame)
qr_label.pack()

button_saveqr = tk.Button(right_frame, text=Strings.SAVE_QRCODE, command=save_qr_action)

status_label = tk.Label(right_frame, text="")
status_label.pack()

root.mainloop()