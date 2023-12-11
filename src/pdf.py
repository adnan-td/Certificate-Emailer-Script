import img2pdf


def save_image_as_pdf(image_path="output.png", output_path="pdf/output.pdf"):
  with open(output_path, "wb") as f:
    f.write(img2pdf.convert(image_path))
