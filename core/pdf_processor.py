# core/pdf_processor.py
import fitz  # PyMuPDF
from core.color_config import COLORS
from core.file_handler import get_output_path

def process_pdf(input_path: str, output_dir: str = "output"):
    doc = fitz.open(input_path)

    for page in doc:
        # ── Black Background ──────────────────────────
        page.draw_rect(
            page.rect,
            color=None,
            fill=COLORS["background"],
            overlay=False  # Draw behind everything
        )

        # ── Change Text Color ─────────────────────────
        for block in page.get_text("dict")["blocks"]:
            if block["type"] == 0:  # Text block
                for line in block["lines"]:
                    for span in line["spans"]:
                        bbox = fitz.Rect(span["bbox"])
                        fontsize = span["size"]
                        text = span["text"]

                        # Cover old text with black rectangle
                        page.draw_rect(bbox, fill=COLORS["background"], color=None)

                        # Rewrite text in white
                        page.insert_text(
                            (bbox.x0, bbox.y1),
                            text,
                            fontsize=fontsize,
                            color=COLORS["text"]
                        )

        # ── Change Link Colors ────────────────────────
        for link in page.get_links():
            if link.get("uri"):
                r = fitz.Rect(link["from"])
                page.draw_rect(r, color=COLORS["link"], width=0.5)

    output_path = get_output_path(input_path, output_dir)
    doc.save(output_path)
    doc.close()

    print(f"✅ Saved: {output_path}")
    return output_path
