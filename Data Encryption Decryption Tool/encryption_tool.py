import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64
import time

# ==========================
# AES FUNCTIONS
# ==========================

def aes_encrypt(text):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)

    start = time.time()

    ciphertext, tag = cipher.encrypt_and_digest(text.encode())

    end = time.time()

    encrypted_data = base64.b64encode(
        cipher.nonce + tag + ciphertext
    ).decode()

    return encrypted_data, key.hex(), end - start


def aes_decrypt(encrypted_text, key_hex):
    data = base64.b64decode(encrypted_text)

    nonce = data[:16]
    tag = data[16:32]
    ciphertext = data[32:]

    key = bytes.fromhex(key_hex)

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    return plaintext.decode()

# ==========================
# RSA FUNCTIONS
# ==========================

rsa_key = RSA.generate(2048)
private_key = rsa_key
public_key = rsa_key.publickey()

def rsa_encrypt(text):

    cipher = PKCS1_OAEP.new(public_key)

    start = time.time()

    encrypted = cipher.encrypt(text.encode())

    end = time.time()

    return base64.b64encode(encrypted).decode(), end - start


def rsa_decrypt(encrypted_text):

    cipher = PKCS1_OAEP.new(private_key)

    encrypted_bytes = base64.b64decode(encrypted_text)

    decrypted = cipher.decrypt(encrypted_bytes)

    return decrypted.decode()

# ==========================
# GUI FUNCTIONS
# ==========================

def encrypt_message():

    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showerror("Error", "Enter text")
        return

    algo = algorithm.get()

    if algo == "AES":

        encrypted, key, enc_time = aes_encrypt(text)

        output_text.delete("1.0", tk.END)

        output_text.insert(
            tk.END,
            f"Encrypted Text:\n{encrypted}\n\nAES Key:\n{key}\n\nTime: {enc_time:.8f} sec"
        )

    else:

        encrypted, enc_time = rsa_encrypt(text)

        output_text.delete("1.0", tk.END)

        output_text.insert(
            tk.END,
            f"Encrypted Text:\n{encrypted}\n\nTime: {enc_time:.8f} sec"
        )


def decrypt_message():

    text = input_text.get("1.0", tk.END).strip()

    algo = algorithm.get()

    try:

        if algo == "AES":

            key = key_entry.get()

            decrypted = aes_decrypt(text, key)

        else:

            decrypted = rsa_decrypt(text)

        output_text.delete("1.0", tk.END)

        output_text.insert(
            tk.END,
            f"Decrypted Text:\n{decrypted}"
        )

    except Exception as e:

        messagebox.showerror("Error", str(e))


def load_file():

    path = filedialog.askopenfilename()

    if path:

        with open(path, "r", encoding="utf-8") as file:

            content = file.read()

            input_text.delete("1.0", tk.END)

            input_text.insert(tk.END, content)


def save_output():

    path = filedialog.asksaveasfilename(
        defaultextension=".txt"
    )

    if path:

        with open(path, "w", encoding="utf-8") as file:

            file.write(
                output_text.get("1.0", tk.END)
            )

        messagebox.showinfo(
            "Saved",
            "File saved successfully"
        )


# ==========================
# GUI
# ==========================

root = tk.Tk()

root.title("Data Encryption and Decryption Tool")

root.geometry("900x650")

algorithm = tk.StringVar(value="AES")

title = tk.Label(
    root,
    text="Data Encryption and Decryption Tool",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Radiobutton(
    frame,
    text="AES",
    variable=algorithm,
    value="AES"
).pack(side=tk.LEFT, padx=20)

tk.Radiobutton(
    frame,
    text="RSA",
    variable=algorithm,
    value="RSA"
).pack(side=tk.LEFT, padx=20)

tk.Label(
    root,
    text="Input Text"
).pack()

input_text = tk.Text(root, height=10, width=100)

input_text.pack()

tk.Label(
    root,
    text="AES Key (Only for AES Decryption)"
).pack()

key_entry = tk.Entry(root, width=80)

key_entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Encrypt",
    command=encrypt_message
).pack(side=tk.LEFT, padx=10)

tk.Button(
    button_frame,
    text="Decrypt",
    command=decrypt_message
).pack(side=tk.LEFT, padx=10)

tk.Button(
    button_frame,
    text="Load File",
    command=load_file
).pack(side=tk.LEFT, padx=10)

tk.Button(
    button_frame,
    text="Save Output",
    command=save_output
).pack(side=tk.LEFT, padx=10)

tk.Label(
    root,
    text="Output"
).pack()

output_text = tk.Text(root, height=15, width=100)

output_text.pack()

root.mainloop()
