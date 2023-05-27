from PIL import Image, ImageDraw, ImageFont


def add_text_to_image(text, image_path="gdsc.png", x=1050, y=970, font_size=80, font_color=(0, 0, 0), padding=100):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", font_size)
    text_width, text_height = draw.textsize(text, font=font)
    text_x = x - text_width // 2
    text_y = y - text_height // 2
    padded_image = Image.new(
        "RGB", (image.width + 2*padding, image.height + 2*padding), (255, 255, 255))
    padded_image.paste(image, (padding, padding))
    draw = ImageDraw.Draw(padded_image)
    draw.text((text_x + padding, text_y + padding),
              text, font=font, fill=font_color)
    padded_image.save("output.png")


# Usage example
if __name__ == "__main__":
    print("Adding text to image")
    image_path = "gdsc.png"
    text = "Prathamesh Kurve"
    x = 1050
    y = 970
    add_text_to_image(text, image_path, x, y, 80, padding=100)
