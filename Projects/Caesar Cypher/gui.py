import tkinter as tk
from tkinter import messagebox
import art

# Caesar Cipher function
def caesar(original_text, shift_amount, encode_or_decode):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    output_text = ""
    smb = ""
    pr = ""
    for char in original_text:
        if char in alphabet:
            pr += char
        else:
            smb += char

    for letter in pr:
        if encode_or_decode == "decode":
            shift_amount *= -1
        shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
        output_text += alphabet[shifted_position]
    return output_text + smb

# GUI Application
class CaesarCipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher")
        self.root.geometry("400x400")

        # Logo
        self.logo_label = tk.Label(root, text=art.logo, font=("Courier", 8))
        self.logo_label.pack(pady=10)

        # Message Input
        self.message_label = tk.Label(root, text="Enter your message:")
        self.message_label.pack()
        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.pack(pady=5)

        # Shift Input
        self.shift_label = tk.Label(root, text="Enter shift number:")
        self.shift_label.pack()
        self.shift_spinbox = tk.Spinbox(root, from_=1, to=25, width=5)
        self.shift_spinbox.pack(pady=5)

        # Encode/Decode Selection
        self.operation_var = tk.StringVar(value="encode")
        self.encode_radio = tk.Radiobutton(root, text="Encode", variable=self.operation_var, value="encode")
        self.encode_radio.pack()
        self.decode_radio = tk.Radiobutton(root, text="Decode", variable=self.operation_var, value="decode")
        self.decode_radio.pack()

        # Process Button
        self.process_button = tk.Button(root, text="Process", command=self.process_text)
        self.process_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="", wraplength=350, justify="left")
        self.result_label.pack(pady=10)

        # Clear Button
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_fields)
        self.clear_button.pack()

    def process_text(self):
        try:
            text = self.message_entry.get().lower()
            shift = int(self.shift_spinbox.get())
            operation = self.operation_var.get()
            result = caesar(text, shift, operation)
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid shift number.")

    def clear_fields(self):
        self.message_entry.delete(0, tk.END)
        self.shift_spinbox.delete(0, tk.END)
        self.shift_spinbox.insert(0, "1")
        self.result_label.config(text="")
        self.operation_var.set("encode")

def run_gui():
    root = tk.Tk()
    app = CaesarCipherGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()