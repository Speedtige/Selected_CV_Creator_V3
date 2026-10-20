from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

class CVModernoTarjetas:

    def generar(self, archivo, foto_path=None):
        c = canvas.Canvas(archivo, pagesize=A4)
        w, h = A4

        # Encabezado claro
        c.setFillColor(HexColor("#EFEFEF"))
        c.rect(0, h-120, w, 120, stroke=0, fill=1)

        # Nombre
        c.setFillColor(HexColor("#333333"))
        c.setFont("Helvetica-Bold", 26)
        c.drawString(40, h-70, "CRISTIAN VELIZ CANO")

        c.setFont("Helvetica", 14)
        c.drawString(40, h-95, "ANALISTA Y DESARROLLADOR")

        # Tarjetas
        y = h-180
        card_w = (w-120)/3
        titulos = ["Experiencia", "Educación", "Habilidades"]
        textos = [
            "• Python\n• PyQt5\n• ReportLab",
            "Ingeniería en Sistemas\nUniversidad de Guatemala",
            "• Trabajo en equipo\n• Diseño Offline"
        ]

        for i in range(3):
            x = 40 + i*(card_w+20)
            c.setFillColor(HexColor("#FFFFFF"))
            c.rect(x, y-140, card_w, 140, stroke=0, fill=1)

            c.setFillColor(HexColor("#0A558E"))
            c.setFont("Helvetica-Bold", 14)
            c.drawString(x+10, y-25, titulos[i])

            c.setFillColor(HexColor("#000000"))
            c.setFont("Helvetica", 10)

            yy = y-45
            for linea in textos[i].split("\n"):
                c.drawString(x+10, yy, linea)
                yy -= 15

        c.save()
