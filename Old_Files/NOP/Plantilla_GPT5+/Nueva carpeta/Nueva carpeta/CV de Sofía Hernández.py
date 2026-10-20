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

class SofiaHernandezCV:
    def __init__(self):
        self.page_w = PAGE_WIDTH
        self.page_h = PAGE_HEIGHT

    def generar(self, ruta_salida="cv_sofia_hernandez.pdf", foto_path=None):
        c = canvas.Canvas(ruta_salida, pagesize=A4)

        # Header
        header_h = 4.2 * cm
        c.setFillColorRGB(0.8, 0.2, 0.2)  # rojo
        c.rect(0, self.page_h - header_h, self.page_w, header_h, stroke=0, fill=1)

        # Circular photo
        if foto_path and os.path.exists(foto_path):
            tmp_png = "_tmp_sofia_photo.png"
            make_circle_image(foto_path, tmp_png, size_px=400)
            img_size_cm = 3.5 * cm
            img_w = img_h = img_size_cm
            img_x = 2 * cm
            img_y = self.page_h - header_h/2 - img_h/2
            c.drawImage(ImageReader(tmp_png), img_x, img_y, width=img_w, height=img_h, mask='auto')
            try:
                os.remove(tmp_png)
            except:
                pass
        else:
            img_size_cm = 3.5 * cm
            img_w = img_h = img_size_cm
            img_x = 2 * cm
            img_y = self.page_h - header_h/2 - img_h/2
            c.setFillColor(colors.lightgrey)
            c.circle(img_x + img_w/2, img_y + img_h/2, img_w/2, stroke=0, fill=1)

        # Name and profession
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 28)
        x_name = 6 * cm
        y_name = self.page_h - 1.5 * cm
        c.drawString(x_name, y_name, "Sofía Hernández")
        c.setFont("Helvetica", 12)
        c.drawString(x_name, y_name - 18, "Puesto de trabajo")

        # Contact details
        c.setFillColorRGB(0.1, 0.1, 0.1)
        c.setFont("Helvetica", 10)
        contact_x = 2 * cm
        contact_y = self.page_h - header_h - 1 * cm
        c.drawString(contact_x, contact_y, "correo@electronico.com")
        c.drawString(contact_x, contact_y - 14, "www.paginaweb.com")
        c.drawString(contact_x, contact_y - 28, "678 910 123")

        # Separator line
        c.setStrokeColorRGB(0.85, 0.85, 0.85)
        line_y = contact_y - 42
        c.setLineWidth(0.8)
        c.line(1.5 * cm, line_y, self.page_w - 1.5 * cm, line_y)

        # Skills
        section_x = 2 * cm
        y = line_y - 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(section_x, y, "Habilidades")
        y -= 16
        c.setFont("Helvetica", 10)
        c.drawString(section_x, y, "Donec sed volutpat velit. Morbi vel ultrices nisi. Maecenas volutpat.")

        # Work experience
        y -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(section_x, y, "Empleos")
        y -= 16
        c.setFont("Helvetica-Bold", 10)
        for i in range(4):
            c.drawString(section_x, y, f"Nombre de la empresa {i+1}")
            y -= 12
            c.setFont("Helvetica-Oblique", 9)
            c.drawString(section_x, y, "Puesto de trabajo")
            y -= 12
            c.setFont("Helvetica", 9)
            c.drawString(section_x, y, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam sagittis dolor ante, sit amet commodo elit posuere vitae. Donec id viverra nibh.")
            y -= 18
            c.setFont("Helvetica-Bold", 10)

        # Education
        y -= 6
        c.setFont("Helvetica-Bold", 12)
        c.drawString(section_x, y, "Estudios")
        y -= 16
        c.setFont("Helvetica-Bold", 10)
        for i in range(2):
            c.drawString(section_x, y, f"Titulación {i+1}")
            y -= 12
            c.setFont("Helvetica", 9)
            c.drawString(section_x, y, "Nombre de la escuela, universidad")
            y -= 12
            c.drawString(section_x, y, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
            y -= 16

        c.showPage()
        c.save()

# Llamar a la clase para generar el PDF
if __name__ == "__main__":
    img_path = "ruta/a/la/imagen.jpg"  # Reemplaza con la ruta correcta de la imagen
    s = SofiaHernandezCV()
    s.generar("cv_sofia_hernandez.pdf", foto_path=img_path)
    print("Se generó cv_sofia_hernandez.pdf")