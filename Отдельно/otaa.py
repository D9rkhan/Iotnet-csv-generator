import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

class ExcelGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Iotnet csv generator App")

        self.data_rows = [
            ["CREATE_OTAA", "", "", "", "", "LoRaWAN AppKey", "", "", "", ""],
        ]

        self.default_device_profile_id = "5332d6ed-1670-4786-9490-9b2d397726b1"
        self.output_file_name = "iotnet.csv"
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
        cities = ["Павлодар", "Алматы", "Астана", "Актобе", "Костанай", "Талдыкорган", "Атырау", "Кызылорда", "Шымкент", "Петропавлск", "Тараз"]
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
    app = ExcelGeneratorApp(root)
    root.mainloop()
