from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

class CVSidebarAzul:

    def _foto(self, c, img, x, y, size):
        c.setFillColor(HexColor("#FFFFFF"))
        c.circle(x+size/2, y+size/2, size/2, stroke=0, fill=1)
        if img:
            c.drawImage(img, x, y, size, size, mask="auto")

    def generar(self, archivo, foto_path=None):
        c = canvas.Canvas(archivo, pagesize=A4)
        w, h = A4

        # Barra lateral
        c.setFillColor(HexColor("#0E3B85"))
        c.rect(0, 0, 180, h, stroke=0, fill=1)

        # Foto
        self._foto(c, foto_path, 40, h-200, 100)

        # Nombre
        c.setFillColor(HexColor("#FFFFFF"))
        c.setFont("Helvetica-Bold", 20)
        c.drawString(20, h-230, "CRISTIAN VELIZ")

        # Contacto
        c.setFont("Helvetica", 10)
        c.drawString(20, h-260, "Tel: (502) 5555-1212")
        c.drawString(20, h-280, "Email: cristian@example.com")

        # Contenido principal
        c.setFillColor(HexColor("#000000"))
        x = 200
        y = h-80

        c.setFont("Helvetica-Bold", 18)
        c.drawString(x, y, "PERFIL")
        y -= 25

        c.setFont("Helvetica", 12)
        texto = (
            "Ingeniero en software con experiencia en aplicaciones Offline,\n"
            "interfaces PyQt5 y generación de documentos programáticos."
        )
        for linea in texto.split("\n"):
            c.drawString(x, y, linea)
            y -= 18

        c.save()
