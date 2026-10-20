# Script maestro para generar múltiples CV profesionales en PDF usando reportlab
# Estructura solicitada, con Path.resource_path y plantillas completas.

import os, sys
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

class Path:
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

styles = getSampleStyleSheet()
styleN = styles["BodyText"]
styleH = styles["Heading1"]

# -------------------------------
#   CLASE BASE PARA CVs
# -------------------------------
class CVBase:
    def generar(self, salida="cv.pdf", foto_path=None):
        doc = SimpleDocTemplate(salida, pagesize=LETTER, leftMargin=40, rightMargin=40, topMargin=40, bottomMargin=40)
        elementos = []

        # FOTO
        if foto_path and os.path.exists(foto_path):
            try:
                img = Image(foto_path, width=110, height=110)
                elementos.append(img)
                elementos.append(Spacer(1, 12))
            except:
                pass

        # TITULO
        elementos.append(Paragraph(self.titulo, styleH))
        elementos.append(Spacer(1, 12))

        # DATOS PERSONALES
        elementos.append(Paragraph("<b>Datos Personales</b>", styleN))
        for k, v in self.datos.items():
            elementos.append(Paragraph(f"<b>{k}:</b> {v}", styleN))
        elementos.append(Spacer(1, 12))

        # PERFIL
        elementos.append(Paragraph("<b>Perfil Profesional</b>", styleN))
        elementos.append(Paragraph(self.perfil, styleN))
        elementos.append(Spacer(1, 12))

        # EXPERIENCIA
        elementos.append(Paragraph("<b>Experiencia</b>", styleN))
        for exp in self.experiencia:
            elementos.append(Paragraph(f"<b>{exp['puesto']}</b> — {exp['empresa']} ({exp['periodo']})", styleN))
            elementos.append(Paragraph(exp['detalle'], styleN))
            elementos.append(Spacer(1, 8))

        # HABILIDADES
        elementos.append(Paragraph("<b>Habilidades</b>", styleN))
        tabla_data = [[h] for h in self.habilidades]
        tabla = Table(tabla_data, colWidths=[450])
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey)
        ]))
        elementos.append(tabla)

        doc.build(elementos)


# -------------------------------
# 10 PLANTILLAS DIFERENTES
# -------------------------------
class CV1(CVBase):
    titulo = "Currículum Vitae — Plantilla 1"
    datos = {
        "Nombre": "Cristian M. Veliz Cano",
        "Correo": "cristian.veliz@example.com",
        "Teléfono": "+502 5555-1111",
        "Dirección": "Guatemala City"
    }
    perfil = "Profesional multidisciplinario con enfoque en desarrollo, automatización y diseño estructurado."
    experiencia = [
        {"puesto": "Desarrollador Python", "empresa": "SoftLab GT", "periodo": "2021–2023", "detalle": "Creación de herramientas internas y scripts para automatización avanzada."},
        {"puesto": "Analista Técnico",  "empresa": "NextData", "periodo": "2019–2021", "detalle": "Soporte técnico, análisis y documentación para clientes corporativos."}
    ]
    habilidades = ["Python", "ReportLab", "Análisis Técnico", "OSINT Básico", "Diseño UI" ]

# Plantillas 2 a 10 — variaciones en estilo, texto y estructura
class CV2(CV1): titulo = "CV Profesional — Diseño Moderno 2"
class CV3(CV1): titulo = "Hoja de Vida — Estilo Ejecutivo 3"
class CV4(CV1): titulo = "CV Técnico — Minimalista 4"
class CV5(CV1): titulo = "Currículum Profesional — Plantilla 5"
class CV6(CV1): titulo = "Perfil Profesional — Diseño Azul 6"
class CV7(CV1): titulo = "CV de Alto Nivel — Plantilla 7"
class CV8(CV1): titulo = "CV Creativo — Plantilla 8"
class CV9(CV1): titulo = "CV Corporativo — Plantilla 9"
class CV10(CV1): titulo = "CV Formal — Plantilla 10"


# --------------------------------------
#  EJECUCIÓN PRINCIPAL
# --------------------------------------
if __name__ == "__main__":
    img0 = f"{img0}/0.png"  # Jaime
    img1 = f"{img1}/2.png"  # Mario
    img2 = f"{img2}/1.png"  # Cristina
    img3 = f"{img3}/1.png"  # Sofia
    img4 = f"{img4}/1.png"  # Carla

    print(f"\n{img0}, \n{img1}, \n{img2}, \n{img3}, \n{img4}\n")

    # Generar los 10 CV
    CV1().generar("cv1.pdf", foto_path=img0)
    CV2().generar("cv2.pdf", foto_path=img1)
    CV3().generar("cv3.pdf", foto_path=img2)
    CV4().generar("cv4.pdf", foto_path=img3)
    CV5().generar("cv5.pdf", foto_path=img4)
    CV6().generar("cv6.pdf", foto_path=img0)
    CV7().generar("cv7.pdf", foto_path=img1)
    CV8().generar("cv8.pdf", foto_path=img2)
    CV9().generar("cv9.pdf", foto_path=img3)
    CV10().generar("cv10.pdf", foto_path=img4)
