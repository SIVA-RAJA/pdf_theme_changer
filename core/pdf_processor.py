# core/pdf_processor.py
import fitz
from PIL import Image, ImageEnhance
import numpy as np
import io
from core.file_handler import get_output_path

def is_image_heavy_page(page):
    """Detect if page is mostly images (like a book cover)"""
    images = page.get_images(full=True)
    text = page.get_text().strip()
    return len(images) > 0 and len(text) < 50

def apply_dark_mode(img: Image.Image) -> Image.Image:
    """Smart dark mode — black bg, pure white text"""
    img_array = np.array(img.convert("RGB"), dtype=np.float32)

    # Normalize to 0-1
    img_norm = img_array / 255.0

    # Invert
    img_inverted = 1.0 - img_norm

    # Boost contrast to push text to pure white
    # Anything above 0.6 brightness → push to pure white
    # Anything below 0.3 brightness → push to pure black
    r, g, b = img_inverted[:,:,0], img_inverted[:,:,1], img_inverted[:,:,2]
    brightness = 0.299*r + 0.587*g + 0.114*b

    # Create mask for text pixels (bright after inversion = was dark text)
    text_mask = brightness > 0.55

    # Force text pixels to pure white
    img_inverted[text_mask] = [1.0, 1.0, 1.0]

    # Force background pixels to pure black
    bg_mask = brightness < 0.25
    img_inverted[bg_mask] = [0.0, 0.0, 0.0]

    result = (img_inverted * 255).astype(np.uint8)
    return Image.fromarray(result)

def apply_cover_dark(img: Image.Image) -> Image.Image:
    """For cover pages — just darken, don't invert colors"""
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(0.5)  # 50% darker

def process_pdf(input_path: str, output_dir: str = "output"):
    doc = fitz.open(input_path)
    new_doc = fitz.open()

    for page_num, page in enumerate(doc.pages()):
        mat = fitz.Matrix(2, 2)
        pix = page.get_pixmap(matrix=mat)

        img_data = pix.tobytes("png")
        img = Image.open(io.BytesIO(img_data)).convert("RGB")

        # Check if cover/image-heavy page
        if is_image_heavy_page(page):
            print(f"🖼️  Page {page_num + 1} detected as image/cover — darkening only")
            processed_img = apply_cover_dark(img)
        else:
            processed_img = apply_dark_mode(img)

        # Save processed image
        img_bytes = io.BytesIO()
        processed_img.save(img_bytes, format="PNG")
        img_bytes.seek(0)

        # Add to new PDF
        new_page = new_doc.new_page(
            width=page.rect.width,
            height=page.rect.height
        )
        new_page.insert_image(
            new_page.rect,
            stream=img_bytes.read()
        )

        print(f"✅ Page {page_num + 1} done")

    output_path = get_output_path(input_path, output_dir)
    new_doc.save(output_path)
    new_doc.close()
    doc.close()

    print(f"\n✅ Saved: {output_path}")
    return output_path
