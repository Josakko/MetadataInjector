from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os


root = Tk()

window_width = 350
window_hight = 400

monitor_width = root.winfo_screenwidth()
monitor_hight = root.winfo_screenheight()

x = (monitor_width / 2) - (window_width / 2)
y = (monitor_hight / 2) - (window_hight / 2)

root.geometry(f'{window_width}x{window_hight}+{int(x)}+{int(y)}')

root.title("Metadata Injector")
root.iconbitmap("JK.ico")
root.config(bg="#dbdbdb")


font = ("Arial", 14)
ready = False

def input():
    global inputfile, ready
    inputfile = filedialog.askopenfilename(defaultextension="mp4", filetypes=[("Video Files", "*.mp4*"), ("WebM Files", "*.webm")])
    input_lbl.configure(text=inputfile)
    if inputfile and ready:
        execute_btn.config(state="normal")
    else:
        ready = True
    
def output():
    global outputfile, ready
    outputfile = filedialog.asksaveasfilename(defaultextension="mp4", filetypes=[("Video Files", "*.mp4"), ("WebM Files", "*.webm")])
    output_lbl.configure(text=inputfile)
    if outputfile and ready:
        execute_btn.config(state="normal")
    else:
        ready = True

def inject():
    print()
    cmd = f'ffmpeg -i {inputfile} -metadata duration="$(ffprobe -i {inputfile} -show_entries format=duration -v quiet -of csv="p=0")" {outputfile}' #cmd = f'ffmpeg -i {inputfile} -metadata duration="$(ffprobe -i {inputfile} -show_entries format=duration -v quiet -of csv="p=0")" -codec copy {outputfile}'
    root.title("Processing - Metadata Injector")
    status_lbl.configure(text="Processing...")
    messagebox.showwarning("Warning", "This process could take several minutes, please do not close this window until processing the video is completed!")
    try:
        os.system(cmd)
    except Exception as e:
        root.title("Failed - Metadata Injector")
        status_lbl.configure(text="Failed, please try again!")
        messagebox.showerror("Error", "Something went wrong, please try again!")
    root.title("Success - Metadata Injector")
    status_lbl.configure(text="Successfully completed!")
    messagebox.showinfo("Info", "Process successfully completed!")

separator_lbl = Label(root, text="", bg="#dbdbdb")
separator_lbl.pack()

input_lbl = Label(root, text="", font=font, bg="#dbdbdb")
input_lbl.pack(pady=5)

input_btn = Button(root, text="Select Input file", width=20, font=font, command=input)
input_btn.pack()

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill=X, pady=15)

output_lbl = Label(root, text="", font=font, bg="#dbdbdb")
output_lbl.pack(pady=5)

output_btn = Button(root, text="Select Output File", width=20, font=font, command=output)
output_btn.pack()

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill=X, pady=15)

status_lbl = Label(root, text="", font=font, bg="#dbdbdb")
status_lbl.pack(pady=5)

execute_btn = Button(root, text="Inject Metadata", width=20, font=font, command=inject, state="disabled")
execute_btn.pack()


root.mainloop()
