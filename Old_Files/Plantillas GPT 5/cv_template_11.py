import os, sys, textwrap
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.pdfgen import canvas
from reportlab.lib import colors

class Path:
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

img_base = Path.resource_path("Avatares")
foto0 = f"{img_base}/0.png"
foto1 = f"{img_base}/1.png"
foto2 = f"{img_base}/2.png"
foto3 = f"{img_base}/3.png"
foto4 = f"{img_base}/4.png"

PERSONA = {
    "Estudiante": "________________________________________",
    "Nombres": "Cristian Manolo",
    "Apellidos": "Veliz Cano",
    "Identificación": "XXXX XXXXX XXXX",
    "Nit": "XXXXXXXX",
    "Correo Electrónico": "XXXXXXXXXX@gmail.com",
    "Fecha de Nacimiento": "XX/XX/XXXX",
    "Profesión": "Técnico en Computación",
    "Pretensión Salarial": "Q 2500.00",
    "Sexo": "Masculino",
    "Estado Civil": "Soltero",
    "Años de Experiencia": "Entre 3 y 5 años",
    "Teléfonos": "XXXX-XXXX",
    "Dirección": "XXXXXXXX Zona X, XX CL XXXXX XXXX 0X-0",
    "Formación Académica": "Estudiando",
    "Experiencia Profesional": [
        "Academia Comercial Modelo — Mecanógrafo Supervisor",
        "Taller Mecánico Automotriz Pelón — Mecánico Automotriz",
        "Empresa Torsa — Dependiente de Mostrador",
        "SELO, Servicios Eléctricos Oqueli — Ayudante de Electricista",
        "Librería y Papelería Pro papel — Encargado de Fotocopiadoras",
        "Agua Pura Antártida — Rutero Piloto",
        "Empresa Imagen y Publicidad — Serigrafo",
        "Eco Maderas Zona 10 Guatemala — Ayudante de Carpintería",
        "Comercial El Buen Precio — Encargado de Bodega",
        "Zapatería G&T Goody Toledo — Encargado General",
        "Rapi Entregas Los Altos — Co-dueno en Asociación, Gerente",
        "Municipalidad de San Lorenzo, Such. — Encargado Área de Informática"
    ],
    "Información Adicional": "Mecanógrafo",
    "Habilidades": [
        "Manejo de Carro y Moto",
        "Carpintería básica",
        "Electricidad básica",
        "Administración básica",
        "Atención al Cliente",
        "Reparación de Hardware y Software",
        "Dibujo técnico",
        "Seguir órdenes directas"
    ],
    "Intereses": "Que Tanto La Empresa como el Jefe o Dueño queden siempre en alto; seguir estudiando; realizar bien mis tareas; garantizar mi trabajo; ser mejor persona.",
    "Referencias Laborales": [
        "Lic. Henry Estuardo Ayala Dardon — Alcalde de San Lorenzo Suchitepéquez — Cel. XXXX-XXXX",
        "P.C. Narciso Morales García — Encargado RRHH Municipalidad San Lorenzo — Cel. XXXX-XXXX",
        "Ing. Jorge Eduardo Kestler — Ingeniero Supervisor Obras Municipales — Cel. XXXX-XXXX"
    ],
    "Referencias Personales": [
        "Martin López Mendoza — Profesor — Cel. XXXX-XXXX",
        "Lic. LAE. Ángel Estuardo López Mejía — Cel. XXXX-XXXX",
        "Ing. Julio Cesar Montufar Flores — Cel. XXXX-XXXX"
    ]
}

def safe_draw_image(c, img_path, x, y, size):
    try:
        c.setFillColor(colors.white)
        c.circle(x + size/2, y + size/2, size/2 + 2, stroke=0, fill=1)
        if img_path and os.path.exists(img_path):
            c.drawImage(img_path, x, y, width=size, height=size, mask='auto')
        else:
            c.setFillColor(colors.lightgrey)
            c.rect(x, y, size, size, fill=1, stroke=0)
    except Exception:
        c.setFillColor(colors.lightgrey)
        c.rect(x, y, size, size, fill=1, stroke=0)

def draw_wrapped_text(c, x, y, text, max_width_chars=50, leading=10, font='Helvetica', size=9):
    c.setFont(font, size)
    lines = textwrap.wrap(text, width=max_width_chars)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y

class BaseTemplate:
    def __init__(self, palette, page_size=A4):
        self.palette = palette
        self.page_size = page_size

    def generar_pdf(self, filename, foto_path):
        c = canvas.Canvas(filename, pagesize=self.page_size)
        self.build(c, foto_path)
        c.showPage()
        c.save()

class Template9(BaseTemplate):
    def build(self, c, foto):
        w, h = self.page_size
        c.setFillColorRGB(*self.palette['header'])
        c.rect(0, h-80, w, 80, fill=1)
        c.setFillColor(colors.white)
        c.setFont('Helvetica-Bold', 24)
        c.drawString(40, h-60, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])
        safe_draw_image(c, foto, w-110, h-70, 70)
        x = 40
        y = h-120
        c.setFillColor(colors.black)
        c.setFont('Helvetica-Bold', 14)
        c.drawString(x, y, 'Datos Personales')
        y -= 12
        for key in ['Identificación', 'Nit', 'Fecha de Nacimiento', 'Sexo', 'Estado Civil', 'Dirección', 'Pretensión Salarial']:
            c.setFont('Helvetica', 9)
            c.drawString(x, y, f'{key}: {PERSONA.get(key, "-")}')
            y -= 11
        rx = 300
        ry = h-120
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Experiencia')
        ry -= 12
        for it in PERSONA['Experiencia Profesional']:
            ry = draw_wrapped_text(c, rx, ry, '- ' + it, max_width_chars=50, leading=10, size=9)
            ry -= 4
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Habilidades')
        ry -= 12
        for skill in PERSONA['Habilidades']:
            ry = draw_wrapped_text(c, rx, ry, '- ' + skill, max_width_chars=50, leading=10, size=9)
            ry -= 4
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Intereses')
        ry -= 12
        ry = draw_wrapped_text(c, rx, ry, PERSONA['Intereses'], max_width_chars=50, leading=10, size=9)
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Referencias Laborales')
        ry -= 12
        for ref in PERSONA['Referencias Laborales']:
            ry = draw_wrapped_text(c, rx, ry, '- ' + ref, max_width_chars=50, leading=10, size=9)
            ry -= 4
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Referencias Personales')
        ry -= 12
        for ref in PERSONA['Referencias Personales']:
            ry = draw_wrapped_text(c, rx, ry, '- ' + ref, max_width_chars=50, leading=10, size=9)
            ry -= 4

if __name__ == '__main__':
    palette = {'header': (0.4, 0.1, 0.6), 'titles': (0.2, 0.05, 0.4), 'text': (0, 0, 0)}
    foto = foto4
    Template9(palette, page_size=LETTER).generar_pdf('CV_template_11.pdf', foto)
    print('Generado -> CV_template_11.pdf')