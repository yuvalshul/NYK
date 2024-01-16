import virustotalhandler
import webbrowser
from tkinter import Label, Button, Toplevel, Tk, Checkbutton, W, ttk

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
    def handle_remove(selected_f, grid_rows):
        print(selected_f)
        results = on_remove(selected_f)
        if results:
            row_to_name = [row[0] for row in grid_rows]
            remove_me = []
            for j in range(len(results)):
                if results[j]:
                    remove_me.append(selected_f[j])
                    row_index = row_to_name.index(selected_f[j])
                    grid_row = grid_rows[row_index]
                    for element in grid_row[1::]:
                        element.grid_remove()
            for f in remove_me:
                selected_f.remove(f)

    def handle_vt(file_path):
        output = virustotalhandler.start(file_path)
        vt_window = Tk()
        vt_window.config(pady=10, padx=10)
        vt_window.title("VirusTotal Scan")
        if not output:
            err_label = Label(vt_window, text="There was an error trying to scan this file")
            err_label.pack()
        elif output['positives'] == 0:
            safe_label = Label(vt_window, text="According to VirusTotal the file is SAFE", fg="green")
            safe_label.pack()
        else:
            unsafe_label = Label(vt_window,
                                 text=f"VirusTotal reported {output['positives']} "
                                      f"engines found that this file might be malicious",
                                 fg="red")
            unsafe_label.pack()
            url_label = ttk.Label(vt_window, text="For full VirusTotal analysis", cursor="hand2", foreground="blue")
            url_label.pack()
            url_label.bind("<Button-1>", lambda event: webbrowser.open(output['permalink']))

        vt_window.wait_window()

    def handle_check(checked_path, selected_paths):
        selected_paths.append(checked_path) if checked_path not in selected_paths \
            else selected_paths.remove(checked_path)

    def display_file(file):
        try:
            with open(file, "r") as f:
                content = f.read()
        except Exception as e:
            content = f"Cant read {file}.\nError: {e}"

        display_window = Tk()
        display_window.config(padx=10, pady=10)
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
    rows = []

    for i in range(len(pot_threats)):
        checkbox = Checkbutton(window, text=pot_threats[i], wraplength=300,
                               command=lambda index=i: handle_check(pot_threats[index], selected_files))
        checkbox.grid(row=i + 2, column=0, pady=5, sticky=W)

        vt_btn = Button(window, text="VirusTotal", command=lambda index=i: handle_vt(pot_threats[index]))
        vt_btn.grid(row=i + 2, column=2, pady=5, padx=2)

        if not pot_threats[i].endswith(".exe"):
            display_button = Button(window, text="Display", command=lambda index=i: display_file(pot_threats[index]))
            display_button.grid(row=i + 2, column=1, pady=5, padx=2)
            rows.append((pot_threats[i], checkbox, display_button, vt_btn))
        else:
            rows.append((pot_threats[i], checkbox, vt_btn))

    remove_btn = Button(window, text="Remove Selected Files", font=("TkDefaultFont", 13), fg="red",
                        command=lambda: handle_remove(selected_files, rows))
    remove_btn.grid(row=len(pot_threats) + 2, column=0, pady=5, columnspan=3)

    cont_btn = Button(window, text="End Scan", font=("TkDefaultFont", 13), fg="green",
                      command=lambda: window.destroy())
    cont_btn.grid(row=len(pot_threats) + 3, column=0, pady=5, columnspan=3)

    window.wait_window()
