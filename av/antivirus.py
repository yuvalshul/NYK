import platform
import subprocess
import time
import ui
from utils import Scanner, Drive
from tkinter import Tk, messagebox


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
        ui.start_popup(self.window)
        i = 0
        while True:
            i += 1
            print(f"loop{i}")
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

    def lin_av(self):
        messagebox.showinfo(
            title="Linux not supported yet",
            message="Linux os is yet to be supported by this anti virus"
        )

    def handle(self, flash_drive):
        self.connected_drives.append(flash_drive)
        should_scan = messagebox.askyesno(
            title="New Flash Drive Detected",
            message=f"A new flash drive named '{flash_drive.name}' detected\n"
                    f"Do you want to scan it?"
        )
        if should_scan:
            self.scan(flash_drive)

    def scan(self, flash_drive):
        pot_threats = self.scanner.scan(flash_drive)
        if len(pot_threats) == 0:
            messagebox.showinfo(
                title="Scanning Complete",
                message=f"The scan of '{flash_drive.name}' is complete\n"
                        f"There is no potential threats"
            )
        else:
            self.handle_threats(flash_drive, pot_threats)

    def handle_threats(self, flash_drive, pot_threats):
        pot_threats_str = "\n".join(f"*{path}" for path in pot_threats)
        further_action = messagebox.askyesno(
            title="Scanning Complete",
            message=f"The scan of '{flash_drive.name}' is complete\n"
                    f"--------------------------------------------\n"
                    f"Found {len(pot_threats)} potential threats:\n"
                    f"{pot_threats_str}\n"
                    f"--------------------------------------------\n"
                    f"Do you want to take further action?"
        )
        if further_action:
            self.deal(pot_threats)

    def update_connected_devices(self, curr_connected_flash_drives):
        self.connected_drives = [flash_drive for flash_drive in self.connected_drives
                                 if flash_drive in curr_connected_flash_drives]

    def deal(self, pot_threats):
        ui.menu(pot_threats, on_remove=self.remove)

    def remove(self, files_to_remove):
        files_str = "\n".join(f"*{file}" for file in files_to_remove)
        remove = messagebox.askyesno(
            title="Just Making Sure",
            message=f"Are you sure wo want to delete the following files?\n{files_str}?"
        )
        if remove:
            results = []
            for file in files_to_remove:
                try:
                    self.scanner.remove(file)
                    results.append(True)
                except OSError:
                    results.append(False)
            # give the user info about which files we weren't able to remove due to os error
