import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import csv

class ExcelGeneratorAppOTAA:
    def __init__(self, root):
        self.root = root
        self.root.title("Iotnet csv generator App - OTAA")

        self.data_rows = [
            ["CREATE_OTAA", "", "", "", "", "LoRaWAN AppKey", "", "", "", ""],
        ]

        self.default_device_profile_id = "5332d6ed-1670-4786-9490-9b2d397726b1"
        self.output_file_name = "iotnet-OTAA.csv"
        self.selected_city = ""
        self.inserted_dev_euis = []
        self.inserted_app_keys = []
        self.inserted_values = []
        self.description_entry = None

        self.create_gui()

    def create_gui(self):
        # Frame
        frame = ttk.Frame(self.root, padding="50")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Label
        label = ttk.Label(frame, text="Выберите город:")
        label.grid(row=0, column=0, pady=(0, 20))

        # City Combobox
        cities = ["Павлодар", "Алматы", "Астана", "Актобе", "Костанай", "Талдыкорган", "Атырау", "Кызылорда", "Шымкент", "Петропавлск", "Тараз", "Актау"]
        city_combobox = ttk.Combobox(frame, values=cities, state="readonly")
        city_combobox.grid(row=0, column=1, pady=(0, 20))
        city_combobox.bind("<<ComboboxSelected>>", self.on_city_selected)

        # Entry for DevEUI
        dev_eui_label = ttk.Label(frame, text="DevEUI:")
        dev_eui_label.grid(row=1, column=0, pady=(0, 20))
        dev_eui_entry = tk.Text(frame, height=4, width=30)
        dev_eui_entry.grid(row=1, column=1, pady=(0, 20))

        # Entry for AppKey
        app_key_label = ttk.Label(frame, text="AppKey:")
        app_key_label.grid(row=2, column=0, pady=(0, 20))
        app_key_entry = tk.Text(frame, height=4, width=30)
        app_key_entry.grid(row=2, column=1, pady=(0, 20))

        # Description Entry
        self.description_entry = ttk.Entry(frame)
        self.description_entry.grid(row=3, column=1, pady=(0, 20))
        description_label = ttk.Label(frame, text="Введите описание:")
        description_label.grid(row=3, column=0, pady=(0, 20))

        # Generate Button
        generate_button = ttk.Button(frame, text="Сгенерировать", command=lambda: self.generate_text_file(dev_eui_entry.get("1.0", "end-1c"), app_key_entry.get("1.0", "end-1c")))
        generate_button.grid(row=4, column=0, columnspan=2, pady=(0, 10))

    def on_city_selected(self, event):
        self.selected_city = event.widget.get()

        # Update the first column of data_rows based on the selected city
        if self.selected_city == "Павлодар":
            self.data_rows[0][6] = "b7148a60-9724-4a1b-a2e0-b9fb36c1b869"
            self.data_rows[0][7] = "7"
        elif self.selected_city == "Алматы":
            self.data_rows[0][6] = "c0849eea-a22c-42e4-bf55-52bc43a7a6b0"
            self.data_rows[0][7] = "8"
        elif self.selected_city == "Астана":
            self.data_rows[0][6] = "59a34a89-17ac-48a0-b782-71e1a796d448"
            self.data_rows[0][7] = "9"
        elif self.selected_city == "Актобе":
            self.data_rows[0][6] = "afb34e33-9d41-4d5f-a61e-16de1e582933"
            self.data_rows[0][7] = "10"
        elif self.selected_city == "Костанай":
            self.data_rows[0][6] = "c50adb90-4c7e-47a8-8a0b-6d5827ef7a51"
            self.data_rows[0][7] = "11"
        elif self.selected_city == "Талдыкорган":
            self.data_rows[0][6] = "4ec50cba-fcb0-48c7-b031-dc8c0a935400"
            self.data_rows[0][7] = "12"
        elif self.selected_city == "Атырау":
            self.data_rows[0][6] = "495d15dd-ff6a-441a-b6d5-4cca797ce057"
            self.data_rows[0][7] = "13"
        elif self.selected_city == "Кызылорда":
            self.data_rows[0][6] = "07ea325a-ea7d-4db8-8fe1-6daa9df94364"
            self.data_rows[0][7] = "14"
        elif self.selected_city == "Шымкент":
            self.data_rows[0][6] = "fef36f32-6990-4dca-8cf8-2443d7e66a21"
            self.data_rows[0][7] = "15"
        elif self.selected_city == "Петропавлск":
            self.data_rows[0][6] = "6c2f7775-f7c4-406f-a16c-b501646785cf"
            self.data_rows[0][7] = "16"
        elif self.selected_city == "Тараз":
            self.data_rows[0][6] = "59f2f23f-565d-4a9b-b29d-ba91402e7982"
            self.data_rows[0][7] = "17"
        elif self.selected_city == "Актау":
            self.data_rows[0][6] = "7938d0fd-731f-4425-beba-ec290c249307"
            self.data_rows[0][7] = "20"

    def add_variables(self, dev_euis, app_keys):
        dev_eui_list = dev_euis.split('\n')
        app_key_list = app_keys.split('\n')

        self.inserted_dev_euis.extend(dev_eui_list)
        self.inserted_app_keys.extend(app_key_list)

        # Set DeviceProfileID directly to "5332d6ed-1670-4786-9490-9b2d397726b1"
        device_profile_id = self.default_device_profile_id

        # Set ServiceProfileID based on the selected city
        if self.selected_city == "Павлодар":
            service_profile_id = "b7148a60-9724-4a1b-a2e0-b9fb36c1b869"
        elif self.selected_city == "Алматы":
            service_profile_id = "c0849eea-a22c-42e4-bf55-52bc43a7a6b0"
        elif self.selected_city == "Астана":
            service_profile_id = "59a34a89-17ac-48a0-b782-71e1a796d448"
        elif self.selected_city == "Актобе":
            service_profile_id = "afb34e33-9d41-4d5f-a61e-16de1e582933"
        elif self.selected_city == "Костанай":
            service_profile_id = "c50adb90-4c7e-47a8-8a0b-6d5827ef7a51"
        elif self.selected_city == "Талдыкорган":
            service_profile_id = "4ec50cba-fcb0-48c7-b031-dc8c0a935400"
        elif self.selected_city == "Атырау":
            service_profile_id = "495d15dd-ff6a-441a-b6d5-4cca797ce057"
        elif self.selected_city == "Кызылорда":
            service_profile_id = "07ea325a-ea7d-4db8-8fe1-6daa9df94364"
        elif self.selected_city == "Шымкент":
            service_profile_id = "fef36f32-6990-4dca-8cf8-2443d7e66a21"
        elif self.selected_city == "Петропавлск":
            service_profile_id = "6c2f7775-f7c4-406f-a16c-b501646785cf"
        elif self.selected_city == "Тараз":
            service_profile_id = "59f2f23f-565d-4a9b-b29d-ba91402e7982"
        elif self.selected_city == "Актау":
            service_profile_id = "7938d0fd-731f-4425-beba-ec290c249307"

        # AS Routing Profile ID based on the selected city
        if self.selected_city == "Павлодар":
            as_routing_profile_id = "7"
        elif self.selected_city == "Алматы":
            as_routing_profile_id = "8"
        elif self.selected_city == "Астана":
            as_routing_profile_id = "9"
        elif self.selected_city == "Актобе":
            as_routing_profile_id = "10"
        elif self.selected_city == "Костанай":
            as_routing_profile_id = "11"
        elif self.selected_city == "Талдыкорган":
            as_routing_profile_id = "12"
        elif self.selected_city == "Атырау":
            as_routing_profile_id = "13"
        elif self.selected_city == "Кызылорда":
            as_routing_profile_id = "14"
        elif self.selected_city == "Шымкент":
            as_routing_profile_id = "15"
        elif self.selected_city == "Петропавлск":
            as_routing_profile_id = "16" 
        elif self.selected_city == "Тараз":
            as_routing_profile_id = "17"
        elif self.selected_city == "Актау":
            as_routing_profile_id = "20"

        for dev_eui, app_key in zip(dev_eui_list, app_key_list):
            # Concatenate DevEUI with an underscore and append Description
            row_description = f"{dev_eui}_{self.description_entry.get()}"

            # Update the indices for "DeviceProfileID", "ServiceProfileID", "AS Routing Profile ID", and "LoRaWAN AppKey"
            self.inserted_values.append(["CREATE_OTAA", dev_eui, "", device_profile_id, "", app_key, service_profile_id, as_routing_profile_id, row_description, ""])

    def generate_text_file(self, dev_euis, app_keys):
        if not self.selected_city:
            tk.messagebox.showerror("Error", "Please choose a city.")
            return

        with open(self.output_file_name, 'w', encoding='utf-8') as file:
            header = ["CMD", "DevEUI", "DevAddr", "DeviceProfileID", "LoRaWAN JoinEUI/AppEUI", "LoRaWAN AppKey", "ServiceProfileID", "AS Routing Profile ID", "Description", "Admin info"]
            file.write(','.join(header) + '\n')

            for dev_eui, app_key in zip(dev_euis.split('\n'), app_keys.split('\n')):
                row_data = ["CREATE_OTAA", dev_eui, "", self.default_device_profile_id, "", app_key, self.data_rows[0][6], self.data_rows[0][7], f"{dev_eui}_{self.description_entry.get()}", ""]
                file.write(','.join(row_data) + '\n')

        print(f"Text file '{self.output_file_name}' generated successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelGeneratorAppOTAA(root)
    root.mainloop()

class ExcelGeneratorAppABP:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Generator App - ABP")

        self.default_device_profile_id = "66959415-a00c-4e30-b695-34d1429f8103"
        self.default_service_profile_id = "f1ea6c1a-61fa-4a0e-9b2f-77184a3f38ff"
        self.as_routing_profile_id = "18"
        self.output_file_name = "iotnet-ABP.csv"
        self.description_entry = None

        self.create_gui()

    def create_gui(self):
        # Frame for DevEUI, Device address, Network session key, and Application session key
        data_frame = ttk.Frame(self.root, padding="50")
        data_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Text widget for DevEUI
        dev_eui_label = ttk.Label(data_frame, text="DevEUI:")
        dev_eui_label.grid(row=0, column=0, pady=(0, 20))
        dev_eui_entry = tk.Text(data_frame, height=4, width=30)
        dev_eui_entry.grid(row=0, column=1, pady=(0, 20))

        # Text widget for Device address
        dev_addr_label = ttk.Label(data_frame, text="Device Address:")
        dev_addr_label.grid(row=1, column=0, pady=(0, 20))
        dev_addr_entry = tk.Text(data_frame, height=4, width=30)
        dev_addr_entry.grid(row=1, column=1, pady=(0, 20))

        # Text widget for Network session key
        nwk_s_key_label = ttk.Label(data_frame, text="Network Session Key:")
        nwk_s_key_label.grid(row=2, column=0, pady=(0, 20))
        nwk_s_key_entry = tk.Text(data_frame, height=4, width=30)
        nwk_s_key_entry.grid(row=2, column=1, pady=(0, 20))

        # Text widget for Application session key
        app_s_key_label = ttk.Label(data_frame, text="Application Session Key:")
        app_s_key_label.grid(row=3, column=0, pady=(0, 20))
        app_s_key_entry = tk.Text(data_frame, height=4, width=30)
        app_s_key_entry.grid(row=3, column=1, pady=(0, 20))

        # Entry for Description
        self.description_entry = ttk.Entry(data_frame)
        self.description_entry.grid(row=4, column=1, pady=(0, 20))
        description_label = ttk.Label(data_frame, text="Enter Description:")
        description_label.grid(row=4, column=0, pady=(0, 20))

        # Generate Button
        generate_button = ttk.Button(data_frame, text="Сгенерировать", command=lambda: self.generate_csv_file(
            dev_eui_entry.get("1.0", "end-1c"),
            dev_addr_entry.get("1.0", "end-1c"),
            nwk_s_key_entry.get("1.0", "end-1c"),
            app_s_key_entry.get("1.0", "end-1c")))
        generate_button.grid(row=5, column=0, columnspan=2, pady=(0, 10))

    def generate_csv_file(self, dev_eui, dev_addr, nwk_s_key, app_s_key):
        # Split the multiline input into a list
        dev_eui_list = dev_eui.split('\n')
        dev_addr_list = dev_addr.split('\n')
        nwk_s_key_list = nwk_s_key.split('\n')
        app_s_key_list = app_s_key.split('\n')

        # Open the file in write mode (will replace existing content)
        with open(self.output_file_name, 'w', encoding='utf-8') as file:
            # Write the header
            header = ["CMD", "DevEUI", "DevAddr", "Device Profile ID", "AppSKeys", "NwkSEncKey",
                      "FNwkSIntKey", "SNwkSIntKey", "FCntUp", "NFCntDown", "AFCntDown", "Service Profile ID",
                      "AS Routing Profile ID", "Name", "Admin LAT", "Admin LON", "Admin info"]
            file.write(','.join(header) + '\n')

            # Iterate over the input lists and create CSV rows
            for dev, addr, nwk_key, app_key in zip(dev_eui_list, dev_addr_list, nwk_s_key_list, app_s_key_list):
                # Create CSV data row
                csv_row = [
                    "CREATE_ABP",
                    dev,
                    addr,
                    self.default_device_profile_id,
                    app_key,  # AppSKeys
                    nwk_key,  # NwkSEncKey
                    "", "", "", "", "",  # FNwkSIntKey, SNwkSIntKey, FCntUp, NFCntDown, AFCntDown
                    self.default_service_profile_id,  # Service Profile ID
                    self.as_routing_profile_id,  # AS Routing Profile ID
                    f"{dev}_{self.description_entry.get()}",  # Device Name
                    "", "", "", "",  # Admin LAT, Admin LON, Admin info
                ]

                # Write to CSV file
                file.write(','.join(map(str, csv_row)) + '\n')

        print(f"CSV file '{self.output_file_name}' generated successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelGeneratorAppABP(root)
    root.mainloop()

class ExcelGeneratorAppDelete:
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
        generate_button = ttk.Button(frame, text="Сгенерировать", command=self.generate_csv)
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
        # simpledialog.messagebox.showinfo("CSV Generated", f"CSV file '{self.output_file_name}' generated successfully.")
        print(f"Text file '{self.output_file_name}' generated successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelGeneratorAppDelete(root)
    root.mainloop()