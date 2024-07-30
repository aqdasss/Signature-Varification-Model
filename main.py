import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import cv2
import os
from signature import match

# Match Threshold
THRESHOLD = 85

def browsefunc(ent):
    filename = askopenfilename(filetypes=(
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg")
    ))
    if filename:
        ent.delete(0, tk.END)
        ent.insert(tk.END, filename)

def checkSimilarity(window, path1, path2):
    result = match(path1, path2)
    if result <= THRESHOLD:
        messagebox.showerror("Failure: Signatures Do Not Match", f"Signatures are {result}% similar!!")
    else:
        messagebox.showinfo("Success: Signatures Match", f"Signatures are {result}% similar!!")
    return True

root = tk.Tk()
root.title("Signature Matching")
root.geometry("500x700")

# Label for comparing signatures
uname_label = tk.Label(root, text="Compare Two Signatures:", font=10)
uname_label.place(x=90, y=50)

# Label and entry for signature 1
img1_message = tk.Label(root, text="Signature 1", font=10)
img1_message.place(x=10, y=128)
image1_path_entry = tk.Entry(root, font=10)
image1_path_entry.place(x=150, y=128)
img1_browse_button = tk.Button(root, text="Browse", font=10, command=lambda: browsefunc(image1_path_entry))
img1_browse_button.place(x=400, y=120)

# Label and entry for signature 2
img2_message = tk.Label(root, text="Signature 2", font=10)
img2_message.place(x=10, y=180)
image2_path_entry = tk.Entry(root, font=10)
image2_path_entry.place(x=150, y=180)
img2_browse_button = tk.Button(root, text="Browse", font=10, command=lambda: browsefunc(image2_path_entry))
img2_browse_button.place(x=400, y=172)

# Compare button
compare_button = tk.Button(root, text="Compare", font=10, command=lambda: checkSimilarity(root, image1_path_entry.get(), image2_path_entry.get()))
compare_button.place(x=200, y=240)

# Result label
result_label = tk.Label(root, text="", font=10)
result_label.place(x=200, y=380)

root.mainloop()
