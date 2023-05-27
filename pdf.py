import img2pdf


def save_image_as_pdf(image_path="output.png", output_path="output.pdf"):
    with open(output_path, "wb") as f:
        f.write(img2pdf.convert(image_path))


# Usage example
if __name__ == "__main__":
    image_path = "output.png"
    pdf_output_path = "output.pdf"
    save_image_as_pdf(image_path, pdf_output_path)
