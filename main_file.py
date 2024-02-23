import tkinter as tk
from tkinter import ttk
from excel_generator_classes import ExcelGeneratorAppOTAA, ExcelGeneratorAppABP, ExcelGeneratorAppDelete

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Application")

        # Set the size of the main window
        self.root.geometry("400x300")

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the x and y coordinates to center the main window
        x_coordinate = (screen_width - 400) // 2
        y_coordinate = (screen_height - 300) // 2

        # Set the main window position
        self.root.geometry(f"400x300+{x_coordinate}+{y_coordinate}")

        # Button for launching ExcelGeneratorAppOTAA
        button_otaa = ttk.Button(self.root, text="OTAA Generator", command=self.launch_otaa_generator)
        button_otaa.pack(pady=20, ipadx=20, ipady=10)

        # Button for launching ExcelGeneratorAppABP
        button_abp = ttk.Button(self.root, text="ABP Generator", command=self.launch_abp_generator)
        button_abp.pack(pady=20, ipadx=20, ipady=10)

        # Button for launching ExcelGeneratorAppDelete
        button_delete = ttk.Button(self.root, text="Delete Generator", command=self.launch_delete_generator)
        button_delete.pack(pady=20, ipadx=20, ipady=10)

    def launch_otaa_generator(self):
        root_otaa = tk.Toplevel(self.root)
        app_otaa = ExcelGeneratorAppOTAA(root_otaa)

    def launch_abp_generator(self):
        root_abp = tk.Toplevel(self.root)
        app_abp = ExcelGeneratorAppABP(root_abp)

    def launch_delete_generator(self):
        root_delete = tk.Toplevel(self.root)
        app_delete = ExcelGeneratorAppDelete(root_delete)

if __name__ == "__main__":
    root_main = tk.Tk()
    main_app = MainApplication(root_main)
    root_main.mainloop()