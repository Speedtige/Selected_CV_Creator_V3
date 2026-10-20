
import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

class Path():
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

# Directorios base
img0 = Path.resource_path("Avatares")
img1 = Path.resource_path("Avatares")
img2 = Path.resource_path("Avatares")
img3 = Path.resource_path("Avatares")
img4 = Path.resource_path("Avatares")

foto0 = f"{img0}/0.png"
foto1 = f"{img1}/2.png"
foto2 = f"{img2}/1.png"
foto3 = f"{img3}/1.png"
foto4 = f"{img4}/1.png"

print(f'{foto0}\n{foto1}\n{foto2}\n{foto3}\n{foto4}')


def draw_circle_image(c, img, x, y, size):
    try:
        c.saveState()
        c.circle(x, y, size/2)
        c.clipPath()
        c.drawImage(img, x-size/2, y-size/2, size, size, mask='auto')
        c.restoreState()
    except:
        c.drawImage(img, x-size/2, y-size/2, size, size)


class BaseCV:
    def __init__(self, palette):
        self.header = palette["header"]
        self.titles = palette["titles"]
        self.text = palette["text"]

    def generar(self, archivo, foto):
        c = canvas.Canvas(archivo, pagesize=A4)
        self.body(c, foto)
        c.save()


class CV1(BaseCV):
    def body(self, c, foto):
        c.setFillColorRGB(*self.header); c.rect(0, 760, 595, 80, fill=1)
        c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 26)
        c.drawString(40, 790, "Cristian M. Veliz Cano")
        draw_circle_image(c, foto, 530, 800, 70)

        c.setFillColorRGB(*self.titles); c.setFont("Helvetica-Bold", 16)
        c.drawString(40, 720, "Perfil Profesional")
        c.setFillColorRGB(*self.text); c.setFont("Helvetica", 12)
        c.drawString(40, 700, "Profesional en tecnología con experiencia en desarrollo...")


class CV2(BaseCV):
    def body(self, c, foto):
        c.setFillColorRGB(*self.header); c.rect(0, 0, 180, 842, fill=1)
        draw_circle_image(c, foto, 90, 760, 120)

        c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 18)
        c.drawString(20, 620, "Cristian Veliz")
        c.setFont("Helvetica", 12); 
        c.drawString(20, 600, "Desarrollador de Software")


class CV3(BaseCV):
    def body(self, c, foto):
        c.setFillColorRGB(*self.header); c.rect(0, 780, 595, 60, fill=1)
        draw_circle_image(c, foto, 40, 810, 60)
        c.setFont("Helvetica-Bold", 22); c.setFillColor(colors.white)
        c.drawString(120, 805, "Cristian Veliz Cano")

        c.setFillColorRGB(*self.titles); c.setFont("Helvetica-Bold", 14)
        c.drawString(40, 740, "Experiencia")


class CV4(BaseCV):
    def body(self, c, foto):
        draw_circle_image(c, foto, 300, 790, 120)
        c.setFillColorRGB(*self.titles); c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(300, 720, "Cristian Veliz")


class CV5(BaseCV):
    def body(self, c, foto):
        c.setFillColorRGB(*self.header); c.circle(80, 780, 70, fill=1)
        draw_circle_image(c, foto, 80, 780, 110)
        c.setFillColorRGB(*self.titles); c.setFont("Helvetica-Bold", 20)
        c.drawString(200, 800, "Cristian Veliz")


class CV6(BaseCV):
    def body(self, c, foto):
        c.setFillColorRGB(*self.header); c.rect(0, 780, 595, 40, fill=1)
        draw_circle_image(c, foto, 560, 795, 50)
        c.setFont("Helvetica-Bold", 20); c.setFillColor(colors.white)
        c.drawString(20, 790, "Cristian Veliz")


class CV7(BaseCV):
    def body(self, c, foto):
        c.setFillColorRGB(*self.header); c.rect(0, 0, 220, 842, fill=1)
        draw_circle_image(c, foto, 110, 760, 100)
        c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 18)
        c.drawString(20, 620, "Cristian Veliz")


class CV8(BaseCV):
    def body(self, c, foto):
        c.setFillColorRGB(*self.header)
        c.rect(0, 780, 595, 40, fill=1)
        draw_circle_image(c, foto, 40, 800, 70)

        c.setFont("Helvetica-Bold", 22); c.setFillColor(colors.white)
        c.drawString(130, 795, "Cristian Veliz")


class CV9(BaseCV):
    def body(self, c, foto):
        c.setFillColorRGB(*self.header); 
        c.rect(0, 780, 595, 50, fill=1)
        c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(300, 795, "Cristian Veliz")
        draw_circle_image(c, foto, 550, 800, 60)


class CV10(BaseCV):
    def body(self, c, foto):
        c.setFillColorRGB(*self.header); 
        c.rect(0, 0, 595, 180, fill=1)
        draw_circle_image(c, foto, 300, 120, 120)
        c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 26)
        c.drawCentredString(300, 30, "Cristian Veliz Cano")


if __name__ == "__main__":
    palettes = [
        {"header":(0.1,0.2,0.5),"titles":(0.2,0.3,0.6),"text":(0,0,0)},
        {"header":(0.2,0.5,0.2),"titles":(0.1,0.3,0.1),"text":(0,0,0)},
        {"header":(0.5,0.2,0.2),"titles":(0.4,0.1,0.1),"text":(0,0,0)},
        {"header":(0.6,0.4,0.1),"titles":(0.5,0.3,0.1),"text":(0,0,0)},
        {"header":(0.2,0.2,0.6),"titles":(0.1,0.1,0.4),"text":(0,0,0)},
        {"header":(0.6,0.1,0.4),"titles":(0.3,0.05,0.2),"text":(0,0,0)},
        {"header":(0.1,0.4,0.6),"titles":(0.05,0.2,0.4),"text":(0,0,0)},
        {"header":(0.3,0.3,0.3),"titles":(0.2,0.2,0.2),"text":(0,0,0)},
        {"header":(0.4,0.1,0.6),"titles":(0.2,0.05,0.4),"text":(0,0,0)},
        {"header":(0.1,0.6,0.6),"titles":(0.05,0.4,0.4),"text":(0,0,0)},
    ]

    CVs = [CV1, CV2, CV3, CV4, CV5, CV6, CV7, CV8, CV9, CV10]

    img0 = f"{img0}/0.png"  # Jaime
    img1 = f"{img1}/2.png"  # Mario
    img2 = f"{img2}/1.png"  # Cristina
    img3 = f"{img3}/1.png"  # Sofia
    img4 = f"{img4}/1.png"  # Carla

    fotos = [f"{foto0}",f"{foto1}",f"{foto2}",f"{foto3}",f"{foto4}",
             f"{foto0}",f"{foto1}",f"{foto2}",f"{foto3}",f"{foto4}"]

    for i,cv in enumerate(CVs):
        cv(palettes[i]).generar(f"CV_{i+1}.pdf", fotos[i])
