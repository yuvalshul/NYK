import platform, subprocess, time
from utils import Scanner, Drive
from tkinter import Tk, messagebox, Button, Label


class AntiVirus:
    def __init__(self):
        self.scanner = Scanner()
        self.os = platform.system()
        self.window = Tk()
        self.window.withdraw()
        self.connected_drives = []

    def start(self):
        if self.os == "Windows":
            self.win_av()
        elif self.os == "Linux":
            self.lin_av()
        else:
            messagebox.showinfo(
                title="OS Not Supported",
                message=f"{self.os} is not supported in this anti virus"
            )

    def win_av(self):
        print("Anti Virus Starting...\nPress Ctrl+C To Exit")
        while True:
            try:
                out = subprocess.check_output(args='wmic logicaldisk get DriveType, caption, VolumeSerialNumber',
                                              shell=True)
                shell_lines = out.decode('utf-8').strip().split('\r\r\n')[1::]
                drives = [Drive(shell_line) for shell_line in shell_lines]
                flash_drives = [drive for drive in drives if drive.is_flash_drive()]
                self.update_connected_devices(flash_drives)
                [self.handle(flash_drive) for flash_drive in flash_drives if flash_drive not in self.connected_drives]
                time.sleep(1)
            except KeyboardInterrupt:
                break
        print("Anti Virus Ending...")

    def lin_av(self):
        messagebox.showinfo(
            title="Linux not supported yet",
            message="Linux os is yet to be supported by this anti virus"
        )

    def handle(self, flash_drive):
        self.connected_drives.append(flash_drive)
        should_scan = messagebox.askyesno(
            title="New Flash Drive Detected",
            message=f"A new flash drive named '{flash_drive.name}' detected\nDo you want to scan it?"
        )
        if should_scan:
            self.scan(flash_drive)

    def scan(self, flash_drive):
        pot_threats = self.scanner.scan(flash_drive)
        if len(pot_threats) == 0:
            messagebox.showinfo(
                title="Scanning Complete",
                message=f"The scan of '{flash_drive.name}' is complete\nThere is no potential threats"
            )
        else:
            messagebox.showinfo(
                title="Scanning Complete",
                message=f"The scan of '{flash_drive.name}' is complete\n"
                        f"Found {len(pot_threats)} potential threats"
            )
            self.handle_threats(flash_drive, pot_threats)

    def handle_threats(self, flash_drive, pot_threats):
        for dir_name, dir_path in pot_threats:
            further_action = messagebox.askyesno(
                title="Potential Threat Detected",
                message=f"The flash drive '{flash_drive.name}' has a file called {dir_name} that may be harmful\n"
                        f"Do you want to take further action?"
            )
            if further_action:
                self.deal(dir_path)

    def update_connected_devices(self, curr_connected_flash_drives):
        self.connected_drives = [flash_drive for flash_drive in self.connected_drives
                                 if flash_drive in curr_connected_flash_drives]

    def deal(self, dir_path):
        # delete file, print file
        # show gui
        self.display_menu()
        print(f"Dealing with bad file at {dir_path}")
        with open(dir_path, "r") as file:
            try:
                print(file.read())
            except Exception:
                print("cant read file")


    def display_menu(self):
        pass
        # self.window.withdraw()
        # self.window.title("AntiVirus")
        # self.window.minsize(height=300, width=500)
        # label = Label(self.window, text="AntiVirus")
        # button1 = Button(self.window, text="Scan", command=lambda: print(1))
        # button2 = Button(self.window, text="Update", command=lambda: print(2))
        # button3 = Button(self.window, text="Quarantine", command=lambda: print(3))
        # button4 = Button(self.window, text="Settings", command=lambda: print(4))
        #
        # label.grid(row=0, column=0, columnspan=2)
        # button1.grid(row=1, column=0, padx=10, pady=10)
        # button2.grid(row=1, column=1, padx=10, pady=10)
        # button3.grid(row=2, column=0, padx=10, pady=10)
        # button4.grid(row=2, column=1, padx=10, pady=10)
