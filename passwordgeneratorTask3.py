import tkinter as tk
import secrets
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("550x300")
        self.root.configure(bg="#B5E5CF")

        self.create_widgets()

    def generate_password(self):
        try:
            length = int(self.entry_length.get())

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(characters) for _ in range(length))
            self.result_label.config(text="Generated Password: " + password)
            self.password = password  
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid length")

    def copy_password(self):
        try:
            pyperclip.copy(self.password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        except AttributeError:
            messagebox.showwarning("No Password Generated", "Please generate a password first.")

    def create_widgets(self):
        length_label = tk.Label(self.root, text="Enter Password Length:", bg="#B5E5CF", font=("Arial", 14))
        length_label.grid(row=0, column=0, padx=10, pady=10)

        self.entry_length = tk.Entry(self.root, font=("Arial", 14))
        self.entry_length.grid(row=0, column=1, padx=10, pady=10)

        generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password,
                                    bg='#D4AC0D', font=("Arial", 14))
        generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        copy_button = tk.Button(self.root, text="Copy Password", command=self.copy_password,
                                bg='#D4AC0D', font=("Arial", 14))
        copy_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(self.root, bg="#B5E5CF", font=("Arial", 16))
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
