# ui/selector.py
import tkinter as tk
from tkinter import filedialog, messagebox
from core.file_handler import get_pdfs_from_folder, validate_pdf

def ask_mode() -> str:
    root = tk.Tk()
    root.withdraw()

    choice = messagebox.askquestion(
        "Select Mode",
        "Click YES for SINGLE PDF\nClick NO for BULK (folder or multiple PDFs)",
        icon="question"
    )
    root.destroy()
    return "single" if choice == "yes" else "bulk"


def select_single_pdf() -> list:
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(
        title="Select a PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )
    root.destroy()
    return [path] if validate_pdf(path) else []


def select_bulk_pdfs() -> list:
    root = tk.Tk()
    root.withdraw()

    choice = messagebox.askquestion(
        "Bulk Mode",
        "YES = Select a Folder\nNO = Select Multiple PDFs",
        icon="question"
    )

    if choice == "yes":
        folder = filedialog.askdirectory(title="Select Folder with PDFs")
        root.destroy()
        return get_pdfs_from_folder(folder) if folder else []
    else:
        files = filedialog.askopenfilenames(
            title="Select Multiple PDFs",
            filetypes=[("PDF Files", "*.pdf")]
        )
        root.destroy()
        return list(files)
