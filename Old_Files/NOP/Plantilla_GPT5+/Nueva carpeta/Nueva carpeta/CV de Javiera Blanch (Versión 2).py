from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from PIL import Image, ImageOps
import os

PAGE_WIDTH, PAGE_HEIGHT = A4

def make_circle_image(input_path, output_path, size_px=400):
    im = Image.open(input_path).convert("RGBA")
    im = ImageOps.fit(im, (size_px, size_px), centering=(0.5, 0.5))
    mask = Image.new("L", (size_px, size_px), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size_px - 1, size_px - 1), fill=255)
    im.putalpha(mask)
    im.save(output_path, format="PNG")

class JavieraBlanchCV2:
    def __init__(self):
        self.page_w = PAGE_WIDTH
        self.page_h = PAGE_HEIGHT

    def generar(self, ruta_salida="cv_javiera_blanch2.pdf", foto_path=None):
        c = canvas.Canvas(ruta_salida, pagesize=A4)

        # Header
        header_h = 4.2 * cm
        c.setFillColorRGB(0.2, 0.2, 0.2)  # gris oscuro
        c.rect(0, self.page_h - header_h, self.page_w, header_h, stroke=0, fill=1)

        # Name and profession
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 28)
        x_name = 2 * cm
        y_name = self.page_h - 1.5 * cm
        c.drawString(x_name, y_name, "JAVIERA BLANCH")
        c.setFont("Helvetica", 12)
        c.drawString(x_name, y_name - 18, "Product Manager productos digitales")

        # Contact details
        c.setFillColorRGB(0.1, 0.1, 0.1)
        c.setFont("Helvetica", 10)
        contact_x = 2 * cm
        contact_y = self.page_h - header_h - 1 * cm
        c.drawString(contact_x, contact_y, "Plaza Real 5, Barcelona")
        c.drawString(contact_x, contact_y - 14, "+34 698 557 002")
        c.drawString(contact_x, contact_y - 28, "javierablanch@gmail.com")
        c.drawString(contact_x, contact_y - 42, "javierablanch.cyou")

        # Circular photo
        if foto_path and os.path.exists(foto_path):
            tmp_png = "_tmp_javiera_photo2.png"
            make_circle_image(foto_path, tmp_png, size_px=400)
            img_size_cm = 3.5 * cm
            img_w = img_h = img_size_cm
            img_x = self.page_w - img_w - 2 * cm
            img_y = self.page_h - header_h/2 - img_h/2
            c.drawImage(ImageReader(tmp_png), img_x, img_y, width=img_w, height=img_h, mask='auto')
            try:
                os.remove(tmp_png)
            except:
                pass
        else:
            img_size_cm = 3.5 * cm
            img_w = img_h = img_size_cm
            img_x = self.page_w - img_w - 2 * cm
            img_y = self.page_h - header_h/2 - img_h/2
            c.setFillColor(colors.lightgrey)
            c.circle(img_x + img_w/2, img_y + img_h/2, img_w/2, stroke=0, fill=1)

        # Executive summary
        section_x = 2 * cm
        y = self.page_h - header_h - 4 * cm
        c.setFont("Helvetica-Bold", 12)
        c.drawString(section_x, y, "Sobre mi")
        y -= 16
        c.setFont("Helvetica", 