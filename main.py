# main.py
from ui.selector import ask_mode, select_single_pdf, select_bulk_pdfs
from core.pdf_processor import process_pdf

def main():
    print("🎨 PDF Theme Changer — Dark Mode")
    print("─" * 35)

    mode = ask_mode()

    if mode == "single":
        print("📄 Single PDF Mode")
        pdfs = select_single_pdf()
    else:
        print("📦 Bulk Mode")
        pdfs = select_bulk_pdfs()

    if not pdfs:
        print("❌ No PDFs selected. Exiting.")
        return

    print(f"\n🔄 Processing {len(pdfs)} PDF(s)...\n")

    for pdf in pdfs:
        try:
            process_pdf(pdf)
        except Exception as e:
            print(f"⚠️  Error processing {pdf}: {e}")

    print("\n✅ All done! Check the 'output' folder.")

if __name__ == "__main__":
    main()
