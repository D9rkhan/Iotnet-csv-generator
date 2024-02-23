import tkinter as tk
from tkinter import ttk

class ExcelGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Generator App")

        self.default_device_profile_id = "66959415-a00c-4e30-b695-34d1429f8103"
        self.default_service_profile_id = "f1ea6c1a-61fa-4a0e-9b2f-77184a3f38ff"
        self.as_routing_profile_id = "18"
        self.output_file_name = "iotnet.csv"
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
        generate_button = ttk.Button(data_frame, text="Generate", command=lambda: self.generate_csv_file(
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
    app = ExcelGeneratorApp(root)
    root.mainloop()
