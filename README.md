# 🎨 PDF Dark Mode Converter

A Python tool that converts any PDF from the default white background and black text to a dark theme with black background, white text, and blue links. Supports both single and bulk PDF processing.

---

## ✨ Features

- Converts PDF background to black
- Changes font color to white
- Highlights links in blue
- Single PDF mode — pick one file
- Bulk mode — pick a folder or multiple PDFs
- Saves output separately so original files stay untouched
- All colors configurable from one file

---

## 📁 Project Structure

    pdf_theme_changer/
    │
    ├── main.py
    ├── ui/
    │   └── selector.py
    ├── core/
    │   ├── pdf_processor.py
    │   ├── color_config.py
    │   └── file_handler.py
    ├── output/
    ├── requirements.txt
    ├── .gitignore
    ├── LICENSE
    └── README.md

---

## 🚀 Getting Started

### 1. Clone the Repository

    git clone https://github.com/SIVA-RAJA/pdf_theme_changer.git
    cd pdf_theme_changer

### 2. Create Virtual Environment

    python -m venv venv

    # Windows
    venv\Scripts\activate

    # Mac/Linux
    source venv/bin/activate

### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Run the Tool

    python main.py

---

## 🖥️ How to Use

When you run the program a dialog box will appear asking:

    YES → Single PDF Mode
    NO  → Bulk Mode

### Single Mode

- A file picker opens
- Select your PDF
- Converted PDF saved to /output folder

### Bulk Mode

- Choose between:
  - Folder — converts all PDFs inside it
  - Multiple files — hand pick PDFs
- All converted PDFs saved to /output folder

---

## 🎨 Customize Colors

All colors are in one place inside core/color_config.py

    COLORS = {
        "background": (0, 0, 0),        # Black
        "text":       (1, 1, 1),        # White
        "link":       (0.2, 0.4, 1.0),  # Blue
        "heading":    (0.8, 0.8, 0.0),  # Yellow
        "highlight":  (0.0, 0.8, 0.4),  # Green
    }

Colors use RGB format where values are between 0.0 and 1.0

---

## 📦 Dependencies

| Package  | Purpose                          |
|----------|----------------------------------|
| PyMuPDF  | PDF reading, editing, rendering  |
| tkinter  | File picker UI (built in Python) |

---

## 🤝 Contributing

1. Fork the project
2. Create your branch — git checkout -b feature/your-feature
3. Commit your changes — git commit -m 'Add your feature'
4. Push to the branch — git push origin feature/your-feature
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 👨‍💻 Author

SIVA RAJA S — https://github.com/SIVA-RAJA
