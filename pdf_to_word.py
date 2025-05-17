import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter
import os

def select_folder():
    folder_selected = filedialog.askdirectory(title="Select PDF Folder")
    if folder_selected:
        input_folder.set(folder_selected)

def convert_bulk_pdfs():
    pdf_folder = input_folder.get()
    output_folder = os.path.join(pdf_folder, "converted_docs")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            docx_path = os.path.join(output_folder, filename.replace(".pdf", ".docx"))

            cv = Converter(pdf_path)
            cv.convert(docx_path, start=0, end=None)
            cv.close()
            status_label.config(text=f"Converted: {filename}")

root = tk.Tk()
root.title("PDF to Word Converter")

input_folder = tk.StringVar()

frame = tk.Frame(root)
frame.pack(pady=20)

btn_select = tk.Button(frame, text="Select PDF Folder", command=select_folder)
btn_select.pack()

btn_convert = tk.Button(frame, text="Convert PDFs", command=convert_bulk_pdfs)
btn_convert.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()