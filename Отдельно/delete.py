import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import csv

class ExcelGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Iotnet csv delete generator App")

        self.data_rows = [
            ["CMD", "DevEUI"],
        ]

        self.output_file_name = "iotnet-delete.csv"
        self.inserted_dev_euis = []

        self.create_gui()

    def create_gui(self):
        # Frame
        frame = ttk.Frame(self.root, padding="50")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Entry for DevEUI
        dev_eui_label = ttk.Label(frame, text="DevEUI:")
        dev_eui_label.grid(row=1, column=0, pady=(0, 20))
        self.dev_eui_entry = tk.Text(frame, height=4, width=30)
        self.dev_eui_entry.grid(row=1, column=1, pady=(0, 20))

        # Button to generate CSV
        generate_button = ttk.Button(frame, text="Generate CSV", command=self.generate_csv)
        generate_button.grid(row=2, column=0, columnspan=2, pady=(20, 0))

    def generate_csv(self):
        # Get the DevEUIs from the entry
        dev_euis = self.dev_eui_entry.get("1.0", tk.END).strip().split("\n")

        # Add DELETE and DevEUIs to data_rows
        for dev_eui in dev_euis:
            self.data_rows.append(["DELETE", dev_eui])

        # Write data to CSV file
        with open(self.output_file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.data_rows)

        # Notify user
        simpledialog.messagebox.showinfo("CSV Generated", f"CSV file '{self.output_file_name}' generated successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelGeneratorApp(root)
    root.mainloop()
