import tkinter as Runner
from tkinter import filedialog, Text
import os

root = Runner.Tk()
apps = []

if os.path.isfile("favapps.txt"):
    with open("favapps.txt", 'r') as f:
        savedApps = f.read()
        savedApps = savedApps.split(",")
        apps = [x for x in savedApps if x.strip()]

def addApps():
    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/", title= "Pick your fav Apps", filetypes=(("applications", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = Runner.Label(frame, text=app, bg="white")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = Runner.Canvas(root, height=500, width=500, bg="#FFAA55")
canvas.pack()

frame = Runner.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = Runner.Button(root, text="Open File", padx=10,
                     pady=5, fg="white", bg="#FFAA55", command=addApps)
openFile.pack()

runApp = Runner.Button(root, text="Run Apps", padx=10,
                       pady=5, fg="white", bg="#FFAA55", command=runApps)
runApp.pack()

for app in apps:
    label = Runner.Label(frame, text=app)
    label.pack()

root.mainloop()

with open("favapps.txt", 'w') as f:
    for app in apps:
        f.write(app + ',' )