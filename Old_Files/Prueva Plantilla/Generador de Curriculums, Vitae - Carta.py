

# cv_templates_reportlab.py
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from PIL import Image, ImageOps
import math

##=========================================================================================================
##=========================================================================================================

class Path():
    
    def resource_path(relative_path):
        """Get absolute path to resource, works for dev and for pyinstaller"""
        try:
            #PyInstaller Create a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

img0 = Path.resource_path("Avatares")  # Jaime
img1 = Path.resource_path("Avatares")  # Mario
img2 = Path.resource_path("Avatares")  # Cristina
img3 = Path.resource_path("Avatares")  # Sofia
img4 = Path.resource_path("Avatares")  # Carla

PAGE_WIDTH, PAGE_HEIGHT = A4

def make_circle_image(input_path, output_path, size_px=400):
    """
    Crea una imagen circular (png con transparencia) a partir de input_path.
    Guarda en output_path.
    """
    im = Image.open(input_path).convert("RGBA")
    # Resize to square
    im = ImageOps.fit(im, (size_px, size_px), centering=(0.5, 0.5))
    mask = Image.new("L", (size_px, size_px), 0)
    draw = Image.new("RGBA", (size_px, size_px), (0, 0, 0, 0))
    # Create circular mask
    mask_draw = Image.new("L", (size_px, size_px), 0)
    from PIL import ImageDraw
    d = ImageDraw.Draw(mask_draw)
    d.ellipse((0, 0, size_px - 1, size_px - 1), fill=255)
    # Apply mask
    im.putalpha(mask_draw)
    im.save(output_path, format="PNG")

class JaimePerezCV:
    """
    Plantilla tipo 'Jaime Pérez' - encabezado oscuro con foto circular a la derecha.
    """
    def __init__(self):
        self.page_w = PAGE_WIDTH
        self.page_h = PAGE_HEIGHT

    def generar(self, ruta_salida="cv_jaime.pdf", foto_path=None):
        c = canvas.Canvas(ruta_salida, pagesize=A4)
        # Header
        header_h = 4.2 * cm
        c.setFillColorRGB(0.2, 0.2, 0.22)  # gris oscuro
        c.rect(0, self.page_h - header_h, self.page_w, header_h, stroke=0, fill=1)

        # Name and profession (left side of header)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 28)
        x_name = 2 * cm
        y_name = self.page_h - 1.5 * cm
        c.drawString(x_name, y_name, "Jaime Pérez")
        c.setFont("Helvetica", 12)
        c.drawString(x_name, y_name - 18, "Electricista")

        # Circular photo (right side overlapping header)
        if foto_path and os.path.exists(foto_path):
            tmp_png = "_tmp_jaime_photo.png"
            make_circle_image(foto_path, tmp_png, size_px=400)
            img_size_cm = 3.5 * cm
            img_w = img_h = img_size_cm
            img_x = self.page_w - img_w - 2*cm
            img_y = self.page_h - header_h/2 - img_h/2
            c.drawImage(ImageReader(tmp_png), img_x, img_y, width=img_w, height=img_h, mask='auto')
            try:
                os.remove(tmp_png)
            except:
                pass
        else:
            # Draw placeholder circle
            img_size_cm = 3.5 * cm
            img_w = img_h = img_size_cm
            img_x = self.page_w - img_w - 2*cm
            img_y = self.page_h - header_h/2 - img_h/2
            c.setFillColor(colors.lightgrey)
            c.circle(img_x + img_w/2, img_y + img_h/2, img_w/2, stroke=0, fill=1)

        # Contact icons + details under header (left)
        c.setFillColorRGB(0.1, 0.1, 0.1)
        c.setFont("Helvetica", 10)
        contact_x = 2 * cm
        contact_y = self.page_h - header_h - 1*cm
        c.drawString(contact_x, contact_y, "correo@electronico.com")
        c.drawString(contact_x, contact_y - 14, "678 910 123")

        # Separator line
        c.setStrokeColorRGB(0.85, 0.85, 0.85)
        line_y = contact_y - 28
        c.setLineWidth(0.8)
        c.line(1.5*cm, line_y, self.page_w - 1.5*cm, line_y)

        # Sections: Objetivo Profesional
        section_x = 2 * cm
        y = line_y - 20
        c.setFont("Helvetica-Bold", 14)
        c.drawString(section_x, y, "Objetivo Profesional")
        y -= 16
        c.setFont("Helvetica", 10)
        texto_objetivo = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                          "Sed tincidunt facilisis ante, at lacinia orci pellentesque a.")
        # wrap text manually a little
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.platypus import Paragraph
        from reportlab.lib.enums import TA_JUSTIFY
        style = ParagraphStyle('normal', fontName='Helvetica', fontSize=10, leading=12, alignment=TA_JUSTIFY)
        p = Paragraph(texto_objetivo, style)
        # Use a small frame to draw paragraph
        p.wrapOn(c, self.page_w - 4*cm, 5*cm)
        p.drawOn(c, section_x, y - 40)
        y -= 60

        # Experiencia (three dummy entries)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(section_x, y, "Experiencia")
        y -= 16
        c.setFont("Helvetica-Bold", 10)
        for i in range(3):
            c.drawString(section_x, y, "Nombre de la empresa (2018-2018)")
            y -= 12
            c.setFont("Helvetica-Oblique", 9)
            c.drawString(section_x, y, "Título del puesto")
            y -= 12
            c.setFont("Helvetica", 9)
            c.drawString(section_x, y, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
            y -= 18
            c.setFont("Helvetica-Bold", 10)

        # Formación
        y -= 6
        c.setFont("Helvetica-Bold", 12)
        c.drawString(section_x, y, "Formación")
        y -= 14
        c.setFont("Helvetica", 9)
        for i in range(2):
            c.drawString(section_x, y, f"Formación {i+1} (2016-2018)")
            y -= 12
            c.drawString(section_x, y, "Descripción breve de la formación.")
            y -= 16

        # Habilidades: three columns
        y -= 6
        c.setFont("Helvetica-Bold", 12)
        c.drawString(section_x, y, "Habilidades")
        y -= 16
        col_w = (self.page_w - 4*cm) / 3.0
        for i, skill in enumerate(["Habilidad 1", "Habilidad 2", "Habilidad 3"]):
            sx = section_x + i*col_w
            c.setFont("Helvetica-Bold", 10)
            c.drawString(sx, y, skill)
            c.setFont("Helvetica", 9)
            c.drawString(sx, y-12, "Lorem ipsum dolor sit elit.")

        c.showPage()
        c.save()


class MarioLopezCV:
    """
    Plantilla tipo 'Mario López' - barra lateral azul a la izquierda y contenido a la derecha.
    """
    def __init__(self):
        self.page_w = PAGE_WIDTH
        self.page_h = PAGE_HEIGHT

    def generar(self, ruta_salida="cv_mario.pdf", foto_path=None):
        c = canvas.Canvas(ruta_salida, pagesize=A4)
        # Sidebar dimensions
        sidebar_w = self.page_w * 0.32
        c.setFillColorRGB(0.82, 0.9, 0.97)  # azul claro
        c.rect(0, 0, sidebar_w, self.page_h, stroke=0, fill=1)

        # Photo in sidebar
        if foto_path and os.path.exists(foto_path):
            tmp_png = "_tmp_mario_photo.png"
            make_circle_image(foto_path, tmp_png, size_px=400)
            img_size = 4 * cm
            img_x = sidebar_w/2 - img_size/2
            img_y = self.page_h - 4.5*cm
            c.drawImage(ImageReader(tmp_png), img_x, img_y, width=img_size, height=img_size, mask='auto')
            try:
                os.remove(tmp_png)
            except:
                pass
        else:
            # placeholder
            img_size = 4 * cm
            img_x = sidebar_w/2 - img_size/2
            img_y = self.page_h - 4.5*cm
            c.setFillColor(colors.lightgrey)
            c.circle(img_x + img_size/2, img_y + img_size/2, img_size/2, stroke=0, fill=1)

        # Name and profession in sidebar
        c.setFillColorRGB(0.05, 0.1, 0.15)
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(sidebar_w/2, self.page_h - 6.6*cm, "Mario López")
        c.setFont("Helvetica", 10)
        c.drawCentredString(sidebar_w/2, self.page_h - 7.4*cm, "Profesión")

        # Contact & web
        c.setFont("Helvetica", 9)
        contact_y = self.page_h - 9*cm
        c.drawCentredString(sidebar_w/2, contact_y, "correo@electronico.com")
        c.drawCentredString(sidebar_w/2, contact_y - 12, "666 777 888")
        c.drawCentredString(sidebar_w/2, contact_y - 26, "www.webpersonal.com")

        # Left sidebar small sections (Idioma, Software)
        small_y = contact_y - 50
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(sidebar_w/4, small_y, "Idioma")
        c.drawCentredString(sidebar_w*3/4, small_y, "Idioma")
        c.setFont("Helvetica", 9)
        c.drawCentredString(sidebar_w/4, small_y - 12, "Nativo")
        c.drawCentredString(sidebar_w*3/4, small_y - 12, "Nativo")

        # Main content (right column)
        margin_x = sidebar_w + 1.5*cm
        x = margin_x
        y = self.page_h - 2.5*cm
        c.setFont("Helvetica-Bold", 16)
        c.drawString(x, y, "Experiencia")
        y -= 18
        c.setFont("Helvetica-Bold", 11)
        for i in range(4):
            c.drawString(x, y, "Nombre de la empresa (2018-2018)")
            y -= 13
            c.setFont("Helvetica-Oblique", 9)
            c.drawString(x, y, "Título del puesto")
            y -= 12
            c.setFont("Helvetica", 9)
            c.drawString(x, y, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
            y -= 18
            c.setFont("Helvetica-Bold", 11)

        # Formación
        y -= 6
        c.setFont("Helvetica-Bold", 14)
        c.drawString(x, y, "Formación")
        y -= 16
        c.setFont("Helvetica", 10)
        for i in range(3):
            c.drawString(x, y, f"Formación {i+1} (2016-2018)")
            y -= 14
            c.drawString(x, y, "Descripción breve.")
            y -= 16

        c.showPage()
        c.save()


class CristinaRodriguezCV:
    """
    Plantilla tipo 'Cristina Rodríguez' - minimalista, centrada, con separadores.
    """
    def __init__(self):
        self.page_w = PAGE_WIDTH
        self.page_h = PAGE_HEIGHT

    def generar(self, ruta_salida="cv_cristina.pdf", foto_path=None):
        c = canvas.Canvas(ruta_salida, pagesize=A4)
        # Top header: name centered on a light strip
        header_h = 3.2 * cm
        c.setFillColorRGB(0.95, 0.95, 0.95)
        c.rect(0, self.page_h - header_h, self.page_w, header_h, stroke=0, fill=1)

        c.setFillColorRGB(0.07, 0.07, 0.07)
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(self.page_w/2, self.page_h - header_h/2 + 8, "CRISTINA RODRÍGUEZ")
        c.setFont("Helvetica", 10)
        c.drawCentredString(self.page_w/2, self.page_h - header_h/2 - 10, "TITULO DEL PUESTO")

        y = self.page_h - header_h - 24

        # Objetivo
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(self.page_w/2, y, "OBJETIVO PROFESIONAL")
        y -= 18
        # thin centered separator
        c.setStrokeColorRGB(0.8, 0.8, 0.8)
        c.setLineWidth(1)
        c.line(self.page_w*0.2, y+6, self.page_w*0.8, y+6)
        # text
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.platypus import Paragraph
        from reportlab.lib.enums import TA_JUSTIFY
        style = ParagraphStyle('normal', fontName='Helvetica', fontSize=10, leading=12, alignment=TA_JUSTIFY)
        texto_obj = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tincidunt facilisis ante, "
                     "at lacinia orci pellentesque a.")
        p = Paragraph(texto_obj, style)
        p.wrapOn(c, self.page_w*0.6, 4*cm)
        p.drawOn(c, self.page_w*0.2, y-48)
        y -= 90

        # Experiencia (centered blocks)
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(self.page_w/2, y, "EXPERIENCIA")
        y -= 18
        for i in range(3):
            c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(self.page_w/2, y, "NOMBRE DE LA EMPRESA (2018-2018)")
            y -= 12
            c.setFont("Helvetica-Oblique", 9)
            c.drawCentredString(self.page_w/2, y, "Titulo del puesto")
            y -= 12
            c.setFont("Helvetica", 9)
            c.drawCentredString(self.page_w/2, y, "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
            y -= 20

            # small separator
            c.setStrokeColorRGB(0.85, 0.85, 0.85)
            c.setLineWidth(0.8)
            c.line(self.page_w*0.35, y+6, self.page_w*0.65, y+6)
            y -= 8

        # Formación
        y -= 8
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(self.page_w/2, y, "FORMACIÓN")
        y -= 18
        for i in range(2):
            c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(self.page_w/2, y, f"Formación {i+1} (2018-2018)")
            y -= 12
            c.setFont("Helvetica", 9)
            c.drawCentredString(self.page_w/2, y, "Descripción corta sobre la formación.")
            y -= 18

        # Habilidades (three across)
        y -= 4
        c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(self.page_w/2, y, "HABILIDADES")
        y -= 18
        col_xs = [self.page_w*0.25, self.page_w*0.5, self.page_w*0.75]
        for i, skill in enumerate(["Habilidad 1", "Habilidad 2", "Habilidad 3"]):
            c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(col_xs[i], y, skill)
            c.setFont("Helvetica", 9)
            c.drawCentredString(col_xs[i], y-12, "Lorem ipsum dolor sit elit.")

        c.showPage()
        c.save()

if __name__ == "__main__":
    # Ruta de ejemplo para las imágenes que subiste a la sesión

    img0 = f"{img0}/0.png"  # Jaime
    img1 = f"{img1}/2.png"  # Mario
    img2 = f"{img2}/1.png"  # Cristina
    img3 = f"{img3}/1.png"  # Sofia
    img4 = f"{img4}/1.png"  # Carla

    print(f"\
        \n{img0}, \
        \n{img1}, \
        \n{img2}, \
        \n{img3}, \
        \n{img4} \
        ")

    # Generar los 3 CVs con datos falsos
    j = JaimePerezCV()
    j.generar("cv_jaime_perez.pdf", foto_path=img0)

    m = MarioLopezCV()
    m.generar("cv_mario_lopez.pdf", foto_path=img1)

    cr = CristinaRodriguezCV()
    cr.generar("cv_cristina_rodriguez.pdf", foto_path=img2)

    print("Se generaron: cv_jaime_perez.pdf, cv_mario_lopez.pdf, cv_cristina_rodriguez.pdf")
