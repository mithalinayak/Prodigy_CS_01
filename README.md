# Ceasar Cipher GUI Application

This repository contains a simple Ceasar Cipher GUI application built using Python's Tkinter library. The application allows users to encrypt and decrypt text using the Ceasar Cipher method.

## Features

- **Encrypt Text**: Encrypt any input text with a specified key.
- **Decrypt Text**: Decrypt any encrypted text with a specified key.
- **User-Friendly Interface**: Easy-to-use graphical interface with intuitive design.

## Getting Started

Follow the instructions below to set up and run the application on your local machine.

### Prerequisites

- Python 3.x

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/ceasar-cipher-gui.git
    cd ceasar-cipher-gui
    ```

2. **Run the application**:

    ```bash
    python ceasar_cipher.py
    ```

## Usage

1. **Input Text**: Enter the text you want to encrypt or decrypt in the text area.
2. **Specify Key**: Enter a key value between 1 and 25 in the key entry box.
3. **Encrypt/Decrypt**: Click the "Encrypt" button to encrypt the text or the "Decrypt" button to decrypt the text.

## Code Explanation

### CeasarCipher Class

The `CeasarCipher` class extends `tk.Frame` and contains the main logic and GUI components of the application.

- **Initialization**:
    - `self.colour1`, `self.colour2`, and `self.colour3` define the color scheme.
    - `self.letters` contains the alphabet used for the cipher.
    - `self.num_letters` holds the length of the alphabet.

- **render_widgets**:
    - Sets up the GUI components including labels, text widget, buttons, and entry fields.

- **encrypt_text**:
    - Encrypts the input text using the provided key.

- **decrypt_text**:
    - Decrypts the input text using the provided key.

- **get_key**:
    - Retrieves and validates the key entered by the user.

### Main Execution

- The main part of the script initializes the Tkinter root window, sets the window title, adjusts the window size based on the operating system, and starts the Tkinter main loop.

## Acknowledgements

- The Tkinter library documentation and tutorials.
