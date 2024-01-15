from tkinter import *

SHIELD_LOGO = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""


def start_popup(window):
    popup = Toplevel(window)
    popup.title("Welcome To The Anti Virus")
    # popup.geometry("300x100")
    avs = Label(popup, text="Anti Virus Starting", font=("TkDefaultFont", 16))
    avs.pack(pady=10)
    sl = Label(popup, text=SHIELD_LOGO)
    sl.pack(pady=10)
    ccte = Label(popup, text="Press Ctrl+C To Exit", font=("TkDefaultFont", 12))
    ccte.pack(pady=10)
    popup.after(2000, popup.destroy)
    popup.wait_window()


# def end_popup(window):  # does not work yet
#     print("ending")
#     popup = Toplevel(window)
#     popup.title("Anti Virus Ending")
#     ave = Label(popup, text="Anti Virus Ending...")
#     ave.pack(pady=10)
#     sl = Label(popup, text=SHIELD_LOGO)
#     sl.pack(pady=10)
#     # Close the popup after 2000 milliseconds (2 seconds)
#     popup.after(2000, popup.destroy)

def menu(pot_threats, on_remove):
    # def handle_remove(files, c_d):
    #     deleted = on_remove(files)
    #     for i in range(len(files)):
    #         if deleted[i]:
    #             c_d[0].grid_remove

    def on_check(checked_path, selected_paths):
        selected_paths.append(checked_path) if checked_path not in selected_paths \
            else selected_paths.remove(checked_path)

    def display_file(file):
        with open(file, "r") as f:
            try:
                content = f.read()
            except Exception as e:
                print(e)
                content = f"Cant read {file}.\nError: {e}"

        display_window = Tk()
        display_window.title(f"Displaying {file}")

        content_label = Label(display_window, text=content)
        content_label.grid(row=0, column=0)

        display_window.wait_window()

    window = Tk()
    window.config(pady=10, padx=10)
    window.title("Menu")

    av_label = Label(window, text="AntiVirus", font=("TkDefaultFont", 16))
    av_label.grid(row=0, column=0, columnspan=3)

    shield_label = Label(window, text=SHIELD_LOGO)
    shield_label.grid(row=1, column=0, columnspan=3)

    selected_files = []
    # checkbox_displaybtn = []

    for i in range(len(pot_threats)):
        checkbox = Checkbutton(window, text=pot_threats[i], wraplength=300,
                               command=lambda index=i: on_check(pot_threats[index], selected_files))
        checkbox.grid(row=i + 2, column=0, columnspan=2, pady=5, sticky=W)

        if not pot_threats[i].endswith(".exe"):
            display_button = Button(window, text="Display", command=lambda index=i: display_file(pot_threats[index]))
            display_button.grid(row=i + 2, column=2, pady=5)

        # checkbox_displaybtn.append([checkbox, display_button])

    remove_btn = Button(window, text="Remove Selected Files", font=("TkDefaultFont", 13), fg="red",
                        command=lambda: on_remove(selected_files))
    remove_btn.grid(row=len(pot_threats) + 2, column=0, pady=5, columnspan=3)

    window.wait_window()
