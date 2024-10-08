import tkinter as tk
import sys

class CeasarCipher(tk.Frame):

    def __init__(self, root):
        self.colour1 = '#072b63'
        self.colour2 = '#bfe2ff'
        self.colour3 = '#89b9e1'

        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.num_letters = len(self.letters)

        super().__init__(root, bg=self.colour1)

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.render_widgets()

    def render_widgets(self):
        self.title = tk.Label(
            self.main_frame,
            bg=self.colour1,
            fg=self.colour2,
            font=('Arial', 22, 'bold'),
            text='Ceasar Cipher'
        )
        self.title.grid(column=0, row=0, sticky=tk.EW, pady=35)

        self.text_widget = tk.Text(
            self.main_frame,
            bg=self.colour2,
            fg=self.colour1,
            selectbackground=self.colour1,
            selectforeground=self.colour2,
            font=('Arial', 17),
            height=5,
            padx=10,
            pady=10,
            highlightthickness=0,
            border=0
        )
        self.text_widget.grid(column=0, row=1, padx=100)

        self.key_label = tk.Label(
            self.main_frame,
            bg=self.colour1,
            fg=self.colour2,
            font=('Arial', 13),
            text=f'Key: (1-{self.num_letters - 1})',
            justify=tk.CENTER
        )
        self.key_label.grid(column=0, row=2, pady=(38, 10))

        self.buttons_container = tk.Frame(self.main_frame, bg=self.colour1)
        self.buttons_container.columnconfigure(0, weight=1)
        self.buttons_container.columnconfigure(1, weight=1)
        self.buttons_container.columnconfigure(2, weight=1)
        self.buttons_container.grid(column=0, row=3, sticky=tk.NSEW, padx=100)

        self.button_encrypt = tk.Button(
            self.buttons_container,
            bg=self.colour2,
            fg=self.colour1,
            activebackground=self.colour3,
            activeforeground=self.colour1,
            font=('Arial', 15),
            text='Encrypt',
            width=6,
            height=1,
            border=0,
            command=self.encrypt_text
        )
        self.button_encrypt.grid(column=0, row=0, ipadx=5, ipady=5)

        self.button_decrypt = tk.Button(
            self.buttons_container,
            bg=self.colour2,
            fg=self.colour1,
            activebackground=self.colour3,
            activeforeground=self.colour1,
            font=('Arial', 15),
            text='Decrypt',
            width=6,
            height=1,
            border=0,
            command=self.decrypt_text
        )
        self.button_decrypt.grid(column=2, row=0, ipadx=5, ipady=5)

        self.key_entry = tk.Entry(
            self.buttons_container,
            bg=self.colour2,
            fg=self.colour1,
            selectbackground=self.colour1,
            selectforeground=self.colour2,
            font=('Arial', 15),
            width=6,
            highlightthickness=0,
            border=0,
            justify=tk.CENTER
        )
        self.key_entry.grid(column=1, row=0, ipady=9)

    def encrypt_text(self):
        text = self.text_widget.get("1.0", tk.END).strip().lower()
        key = self.get_key()
        if text and key is not None:
            encrypted_text = ''.join([self.letters[(self.letters.index(c) + key) % self.num_letters] if c in self.letters else c for c in text])
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, encrypted_text)

    def decrypt_text(self):
        text = self.text_widget.get("1.0", tk.END).strip().lower()
        key = self.get_key()
        if text and key is not None:
            decrypted_text = ''.join([self.letters[(self.letters.index(c) - key) % self.num_letters] if c in self.letters else c for c in text])
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, decrypted_text)

    def get_key(self):
        try:
            key = int(self.key_entry.get().strip())
            if 1 <= key <= self.num_letters - 1:
                return key
        except ValueError:
            pass
        return None

operating_system = sys.platform
root = tk.Tk()
ceasar_cipher_app = CeasarCipher(root)
root.title("Ceasar Cipher")

if 'win' in operating_system:
    root.geometry('800x450')
elif 'linux' in operating_system:
    root.geometry('800x470')
elif 'darwin' in operating_system:
    root.geometry('800x470')

root.resizable(width=False, height=False)
root.mainloop()
