import hashlib
import tkinter as tk

class EncryptionGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("H3XCrypt")

        # Create input fields
        self.input_label = tk.Label(self.root, text="Enter text to encrypt:")
        self.input_label.grid(row=0, column=0, padx=5, pady=5)
        self.input_entry = tk.Entry(self.root, width=50)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create algorithm selector
        self.algorithm_label = tk.Label(self.root, text="Select encryption algorithm:")
        self.algorithm_label.grid(row=1, column=0, padx=5, pady=5)
        self.algorithm_var = tk.StringVar(value="MD5")
        self.algorithm_dropdown = tk.OptionMenu(self.root, self.algorithm_var, "MD5", "SHA-256")
        self.algorithm_dropdown.grid(row=1, column=1, padx=5, pady=5)

        # Create button to encrypt text
        self.encrypt_button = tk.Button(self.root, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.grid(row=2, column=1, padx=5, pady=5)

        # Create output field
        self.output_label = tk.Label(self.root, text="Encrypted text:")
        self.output_label.grid(row=3, column=0, padx=5, pady=5)
        self.output_entry = tk.Entry(self.root, width=50, state="readonly")
        self.output_entry.grid(row=3, column=1, padx=5, pady=5)

    def encrypt_text(self):
        # Get input text and selected algorithm
        input_text = self.input_entry.get()
        algorithm = self.algorithm_var.get()

        # Encrypt input text using selected algorithm
        if algorithm == "MD5":
            hash_object = hashlib.md5(input_text.encode())
        elif algorithm == "SHA-256":
            hash_object = hashlib.sha256(input_text.encode())
        else:
            raise ValueError("Invalid encryption algorithm")

        # Update output field with encrypted text
        self.output_entry.configure(state="normal")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, hash_object.hexdigest())
        self.output_entry.configure(state="readonly")

    def run(self):
        self.root.mainloop()

# Create and run the GUI
gui = EncryptionGUI()
gui.run()
