# core/file_handler.py
import os

def get_output_path(input_path: str, output_dir: str = "output") -> str:
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)
    return os.path.join(output_dir, f"{name}_dark{ext}")

def validate_pdf(path: str) -> bool:
    return path.endswith(".pdf") and os.path.exists(path)

def get_pdfs_from_folder(folder_path: str) -> list:
    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.endswith(".pdf")
    ]
