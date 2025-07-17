from PIL import Image

def image_to_pdf(image_path, pdf_path):
    try:
        img = Image.open(image_path)
        print(f"✅ Successfully loaded: {image_path}")

        # Convert to RGB if needed
        if img.mode != 'RGB':
            print("🔄 Converting image mode to RGB")
            img = img.convert('RGB')

        # Save as PDF
        img.save(pdf_path, "PDF", resolution=100.0)
        print(f"✅ PDF saved successfully: {pdf_path}")

    except FileNotFoundError:
        print(f"❌ File not found: {image_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

# 👇 Replace with the correct full path to your image and desired output path
image_to_pdf("d:/simple project chalenjes/cconvertimage topdf/sample.jpeg",
             "d:/simple project chalenjes/cconvertimage topdf/output.pdf")
