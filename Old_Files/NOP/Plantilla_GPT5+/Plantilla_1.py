
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader

import os, sys

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

class CVMinimalElegante:

    def _foto_redonda(self, c, img, x, y, size):
        try:
            c.saveState()
            c.setFillColor(HexColor("#DDDDDD"))
            c.circle(x + size/2, y + size/2, size/2, stroke=0, fill=1)
            if img:
                c.drawImage(img, x, y, size, size, mask="auto")
        except:
            pass
        finally:
            c.restoreState()

    def generar(self, archivo, foto_path=None):
        c = canvas.Canvas(archivo, pagesize=A4)
        w, h = A4

        # Encabezado
        c.setFillColor(HexColor("#1A1A1A"))
        c.rect(0, h-120, w, 120, stroke=0, fill=1)

        # Nombre
        c.setFillColor(HexColor("#FFFFFF"))
        c.setFont("Helvetica-Bold", 28)
        c.drawString(40, h-70, "CRISTIAN M. VELIZ CANO")

        # Puesto
        c.setFont("Helvetica", 14)
        c.drawString(40, h-95, "DESARROLLADOR DE SOFTWARE")

        # Foto
        self._foto_redonda(c, foto_path, w-150, h-150, 100)

        # Línea divisoria
        c.setStrokeColor(HexColor("#CCCCCC"))
        c.setLineWidth(1)
        c.line(40, h-160, w-40, h-160)

        y = h-190
        c.setFillColor(HexColor("#000000"))
        c.setFont("Helvetica-Bold", 16)
        c.drawString(40, y, "PERFIL PROFESIONAL")

        c.setFont("Helvetica", 12)
        texto = (
            "Desarrollador con experiencia en Python, PyQt5 y generación de documentos.\n"
            "Apasionado por proyectos humanitarios y software offline accesible."
        )
        y -= 25
        for linea in texto.split("\n"):
            c.drawString(40, y, linea)
            y -= 18

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
    j = CVMinimalElegante()
    j.generar("cv_jaime_perez.pdf", foto_path=img0)