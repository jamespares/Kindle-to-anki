import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

class KindleToAnkiGUI:
    def __init__(self, master):
        self.master = master
        master.title("Kindle to Anki Converter")
        master.geometry("400x200")

        self.input_file = tk.StringVar()
        self.output_file = tk.StringVar()
        self.deck_name = tk.StringVar()

        # Input file selection
        tk.Label(master, text="Input File:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(master, textvariable=self.input_file, width=30).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(master, text="Browse", command=self.browse_input).grid(row=0, column=2, padx=5, pady=5)

        # Output file selection
        tk.Label(master, text="Output File:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(master, textvariable=self.output_file, width=30).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(master, text="Browse", command=self.browse_output).grid(row=1, column=2, padx=5, pady=5)

        # Deck name input
        tk.Label(master, text="Deck Name:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(master, textvariable=self.deck_name, width=30).grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        # Convert button
        tk.Button(master, text="Convert", command=self.convert).grid(row=3, column=1, pady=20)

    def browse_input(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        self.input_file.set(filename)

    def browse_output(self):
        filename = filedialog.asksaveasfilename(defaultextension=".apkg", filetypes=[("Anki Deck", "*.apkg")])
        self.output_file.set(filename)

    def convert(self):
        input_file = self.input_file.get()
        output_file = self.output_file.get()
        deck_name = self.deck_name.get()

        if not input_file or not output_file or not deck_name:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        try:
            result = subprocess.run(["python", "kindle_to_anki.py", input_file, output_file, deck_name], 
                                    capture_output=True, text=True, check=True)
            messagebox.showinfo("Success", "Conversion completed successfully!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Conversion failed: {e.stderr}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = KindleToAnkiGUI(root)
    root.mainloop()
