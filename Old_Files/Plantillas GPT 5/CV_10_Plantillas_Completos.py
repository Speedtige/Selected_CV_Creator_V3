#!/usr/bin/env python3
# CV_10_Plantillas_Completos.py
# Genera 10 CVs en PDF (ReportLab) con contenido ficticio adaptado
# Compatible con Python 3.8+ and ReportLab
import os, sys, textwrap
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

class Path:
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

# Base avatars folder (expected to contain images 0.png .. 4.png)
img_base = Path.resource_path("Avatares")

foto0 = f"{img_base}/0.png"
foto1 = f"{img_base}/1.png"
foto2 = f"{img_base}/2.png"
foto3 = f"{img_base}/3.png"
foto4 = f"{img_base}/4.png"

# Datos ficticios (proporcionados por el usuario)
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

    "Intereses": (
        "Que Tanto La Empresa como el Jefe o Dueño queden siempre en alto; "
        "seguir estudiando; realizar bien mis tareas; garantizar mi trabajo; "
        "ser mejor persona."
    ),

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


# Utilidades de dibujo y texto
def safe_draw_image(c, img_path, x, y, size):
    ##\"\"\"Dibuja una 'foto circular simulada' (caja blanca circular y la imagen dentro).\"\"\"
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

def draw_wrapped_text(c, x, y, text, max_width_chars=60, leading=14, font='Helvetica', size=10):
    ##\"\"\"Envuelve texto por caracteres (aprox.) y lo dibuja hacia abajo desde (x,y).\"\"\"
    c.setFont(font, size)
    lines = []
    for paragraph in text.split('\\n'):
        wrapped = textwrap.wrap(paragraph, width=max_width_chars)
        if not wrapped:
            lines.append('')
        else:
            lines.extend(wrapped)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y

# Clase base para las plantillas
class BaseTemplate:
    def __init__(self, palette):
        self.palette = palette
    def generar_pdf(self, filename, foto_path):
        c = canvas.Canvas(filename, pagesize=A4)
        self.build(c, foto_path)
        c.showPage()
        c.save()

# Ahora definimos 10 plantillas diferentes visualmente y las llenamos con contenido adaptado
class Template1(BaseTemplate):
    # Header top dark with photo right, two-column body
    def build(self, c, foto):
        w, h = A4
        # header
        c.setFillColorRGB(*self.palette['header']); c.rect(0, h-120, w, 120, fill=1)
        c.setFillColor(colors.white); c.setFont('Helvetica-Bold', 26)
        c.drawString(40, h-70, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])
        safe_draw_image(c, foto, w-150, h-110, 100)
        # contact block
        c.setFillColor(colors.white); c.setFont('Helvetica', 9)
        c.drawString(40, h-95, PERSONA['Correo Electrónico'] + ' | ' + PERSONA['Teléfonos'])
        # left column profile
        y = h-140
        c.setFillColor(colors.black); c.setFont('Helvetica-Bold', 14); c.drawString(40, y, 'Perfil Profesional')
        y -= 18
        y = draw_wrapped_text(c, 40, y, 'Profesional con experiencia práctica en oficios y soporte técnico. ' + PERSONA['Intereses'], max_width_chars=80, leading=12, size=10)
        # right column experience list (shortened)
        xcol = 300; ycol = h-140
        c.setFont('Helvetica-Bold', 12); c.drawString(xcol, ycol, 'Experiencia')
        ycol -= 16
        for item in PERSONA['Experiencia Profesional'][:6]:
            ycol = draw_wrapped_text(c, xcol, ycol, '- ' + item, max_width_chars=40, leading=12, size=9)
            ycol -= 2

class Template2(BaseTemplate):
    # Left sidebar with photo, right content with profile, education and skills in bullets
    def build(self, c, foto):
        w, h = A4
        sidebar_w = 160
        c.setFillColorRGB(*self.palette['header']); c.rect(0, 0, sidebar_w, h, fill=1)
        safe_draw_image(c, foto, 30, h-220, 100)
        c.setFillColor(colors.white); c.setFont('Helvetica-Bold', 14); c.drawString(20, h-260, PERSONA['Nombres'])
        c.setFont('Helvetica', 10); c.drawString(20, h-275, PERSONA['Profesión'])
        # right content
        x = sidebar_w + 30; y = h-60
        c.setFillColor(colors.black); c.setFont('Helvetica-Bold', 16); c.drawString(x, y, 'Perfil Profesional')
        y -= 18
        y = draw_wrapped_text(c, x, y, PERSONA['Intereses'], max_width_chars=80, leading=12, size=10)
        y -= 6
        c.setFont('Helvetica-Bold', 14); c.drawString(x, y, 'Formación Académica'); y -= 16
        c.setFont('Helvetica', 10); c.drawString(x, y, PERSONA['Formación Académica']); y -= 18
        c.setFont('Helvetica-Bold', 14); c.drawString(x, y, 'Habilidades'); y -= 14
        for hskill in PERSONA['Habilidades'][:6]:
            c.setFont('Helvetica', 10); c.drawString(x, y, '- ' + hskill); y -= 12

# class Template3(BaseTemplate):
#     # Centered portrait with name and sections below separated by lines
#     def build(self, c, foto):
#         w, h = A4
#         safe_draw_image(c, foto, w/2-65, h-220, 130)
#         c.setFont('Helvetica-Bold', 22); c.setFillColor(colors.black); c.drawCentredString(w/2, h-260, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])
#         y = h-300
#         c.setLineWidth(0.8); c.setStrokeColor(colors.grey); c.line(60, y, w-60, y); y -= 20
#         c.setFont('Helvetica-Bold', 14); c.drawString(60, y, 'Datos Personales'); y -= 16
#         # personal details
#         details = ['Identificación','Nit','Fecha de Nacimiento','Sexo','Estado Civil','Dirección','Pretensión Salarial']
#         for d in details:
#             c.setFont('Helvetica', 10); c.drawString(60, y, f'{d}: {PERSONA.get(d,\"-\")}'); y -= 14
#         y -= 6
#         c.setFont('Helvetica-Bold', 14); c.drawString(60, y, 'Experiencia Relevante'); y -= 16
#         for item in PERSONA['Experiencia Profesional'][:5]:
#             y = draw_wrapped_text(c, 60, y, '- ' + item, max_width_chars=90, leading=12, size=10)
#             y -= 4

class Template3(BaseTemplate):
    # Centered portrait with name and sections below separated by lines
    def build(self, c, foto):
        w, h = A4
        safe_draw_image(c, foto, w/2-65, h-220, 130)

        c.setFont('Helvetica-Bold', 22)
        c.setFillColor(colors.black)
        c.drawCentredString(w/2, h-260, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])

        y = h-300
        c.setLineWidth(0.8)
        c.setStrokeColor(colors.grey)
        c.line(60, y, w-60, y)
        y -= 20

        c.setFont('Helvetica-Bold', 14)
        c.drawString(60, y, 'Datos Personales')
        y -= 16

        # personal details
        details = [
            'Identificación','Nit','Fecha de Nacimiento','Sexo',
            'Estado Civil','Dirección','Pretensión Salarial'
        ]

        for d in details:
            c.setFont('Helvetica', 10)
            c.drawString(60, y, f'{d}: {PERSONA.get(d, "-")}')
            y -= 14

        y -= 6

        c.setFont('Helvetica-Bold', 14)
        c.drawString(60, y, 'Experiencia Relevante')
        y -= 16

        for item in PERSONA['Experiencia Profesional'][:5]:
            y = draw_wrapped_text(
                c, 60, y,
                '- ' + item,
                max_width_chars=90,
                leading=12,
                size=10
            )
            y -= 4


class Template4(BaseTemplate):
    # Top photo large, name centered over a light band, two columns below
    def build(self, c, foto):
        w, h = A4
        # big top photo
        safe_draw_image(c, foto, 40, h-300, 150)
        c.setFillColorRGB(*self.palette['header']); c.rect(220, h-200, 340, 80, fill=1)
        c.setFillColor(colors.white); c.setFont('Helvetica-Bold', 20); c.drawCentredString(390, h-160, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])
        # left column: perfil + habilidades
        x = 40; y = h-330
        c.setFont('Helvetica-Bold', 14); c.setFillColor(colors.black); c.drawString(x, y, 'Perfil'); y -= 16
        y = draw_wrapped_text(c, x, y, PERSONA['Intereses'], max_width_chars=40, leading=12, size=10)
        y -= 6
        c.setFont('Helvetica-Bold', 14); c.drawString(x, y, 'Habilidades'); y -= 14
        for hskill in PERSONA['Habilidades'][:8]:
            c.setFont('Helvetica', 10); c.drawString(x, y, '- ' + hskill); y -= 12
        # right column: experiencia larga
        rx = 260; ry = h-250
        c.setFont('Helvetica-Bold', 14); c.drawString(rx, ry, 'Experiencia'); ry -= 16
        for item in PERSONA['Experiencia Profesional'][:8]:
            ry = draw_wrapped_text(c, rx, ry, '- ' + item, max_width_chars=40, leading=12, size=9)
            ry -= 4

class Template5(BaseTemplate):
    # Decorative circle header left, name right, compact sections below
    def build(self, c, foto):
        w, h = A4
        c.setFillColorRGB(*self.palette['header'])
        c.circle(80, h-100, 70, fill=1)
        safe_draw_image(c, foto, 32, h-142, 96)
        c.setFont('Helvetica-Bold', 20); c.setFillColor(self.palette.get('titles', colors.black))
        c.drawString(180, h-80, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])
        y = h-140
        c.setFont('Helvetica-Bold', 12); c.drawString(40, y, 'Perfil'); y -= 14
        y = draw_wrapped_text(c, 40, y, PERSONA['Intereses'], max_width_chars=90, leading=12, size=10)
        y -= 6
        c.setFont('Helvetica-Bold', 12); c.drawString(40, y, 'Formación'); y -= 14
        c.setFont('Helvetica', 10); c.drawString(40, y, PERSONA['Formación Académica']); y -= 16
        c.setFont('Helvetica-Bold', 12); c.drawString(40, y, 'Referencias'); y -= 14
        for ref in PERSONA['Referencias Laborales'][:2]:
            y = draw_wrapped_text(c, 40, y, ref, max_width_chars=90, leading=12, size=9)
            y -= 6

class Template6(BaseTemplate):
    # Thin top strip, large name left, skills as boxes
    def build(self, c, foto):
        w, h = A4
        c.setFillColorRGB(*self.palette['header']); c.rect(0, h-60, w, 60, fill=1)
        c.setFont('Helvetica-Bold', 24); c.setFillColor(colors.white); c.drawString(40, h-45, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])
        safe_draw_image(c, foto, w-140, h-140, 100)
        # skills boxes
        x = 40; y = h-140
        for i,skill in enumerate(PERSONA['Habilidades'][:6]):
            c.setFillColorRGB(0.95,0.95,0.95); c.rect(x, y-40, 160, 30, fill=1, stroke=0)
            c.setFillColor(colors.black); c.setFont('Helvetica', 10); c.drawString(x+6, y-20, skill)
            x += 170
            if x > w-180:
                x = 40; y -= 50

class Template7(BaseTemplate):
    # Left column long list, right column summary
    def build(self, c, foto):
        w, h = A4
        left_w = 260
        c.setFillColorRGB(*self.palette['header']); c.rect(0, 0, left_w, h, fill=1)
        safe_draw_image(c, foto, 50, h-200, 100)
        c.setFillColor(colors.white); c.setFont('Helvetica-Bold', 14); c.drawString(30, h-280, PERSONA['Nombres'])
        # left list: contacts and basic data
        ly = h-320
        c.setFont('Helvetica', 10); c.drawString(20, ly, 'Correo: ' + PERSONA['Correo Electrónico']); ly -= 14
        c.drawString(20, ly, 'Tel: ' + PERSONA['Teléfonos']); ly -= 14
        c.drawString(20, ly, 'Dirección: ' + PERSONA['Dirección']); ly -= 18
        # right summary
        rx = left_w + 30; ry = h-80
        c.setFillColor(colors.black); c.setFont('Helvetica-Bold', 16); c.drawString(rx, ry, 'Perfil y Experiencia'); ry -= 18
        ry = draw_wrapped_text(c, rx, ry, PERSONA['Intereses'], max_width_chars=70, leading=12, size=10)
        ry -= 6
        c.setFont('Helvetica-Bold', 14); c.drawString(rx, ry, 'Experiencia (selección)'); ry -= 16
        for item in PERSONA['Experiencia Profesional'][:7]:
            ry = draw_wrapped_text(c, rx, ry, '- ' + item, max_width_chars=70, leading=12, size=9)
            ry -= 4

class Template8(BaseTemplate):
    # Clean top band, centered name, two stacked boxes for experience and education
    def build(self, c, foto):
        w, h = A4
        c.setFillColorRGB(*self.palette['header']); c.rect(0, h-100, w, 100, fill=1)
        safe_draw_image(c, foto, 40, h-220, 110)
        c.setFillColor(colors.white); c.setFont('Helvetica-Bold', 22); c.drawCentredString(w/2, h-60, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])
        # boxes
        bx = 60; by = h-320
        c.setFillColor(colors.white); c.rect(bx, by-220, w-120, 200, fill=1, stroke=0)
        text_y = by-30
        c.setFillColor(colors.black); c.setFont('Helvetica-Bold', 14); c.drawString(bx+10, text_y, 'Experiencia'); text_y -= 18
        for item in PERSONA['Experiencia Profesional'][:8]:
            text_y = draw_wrapped_text(c, bx+10, text_y, '- ' + item, max_width_chars=110, leading=12, size=10)
            text_y -= 4

# class Template9(BaseTemplate):
#     # Narrow top bar, name large left, photo small right, sections below split
#     def build(self, c, foto):
#         w, h = A4
#         c.setFillColorRGB(*self.palette['header']); c.rect(0, h-80, w, 80, fill=1)
#         c.setFillColor(colors.white); c.setFont('Helvetica-Bold', 26); c.drawString(40, h-55, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])
#         safe_draw_image(c, foto, w-110, h-70, 70)
#         # left column details
#         x = 40; y = h-120
#         c.setFont('Helvetica-Bold', 14); c.drawString(x, y, 'Datos Personales'); y -= 14
#         for key in ['Identificación','Nit','Fecha de Nacimiento','Sexo','Estado Civil']:
#             c.setFont('Helvetica', 10); c.drawString(x, y, f'{key}: {PERSONA.get(key,\"-\")}'); y -= 12
#         # right column experiences
#         rx = 300; ry = h-120
#         c.setFont('Helvetica-Bold', 14); c.drawString(rx, ry, 'Experiencia'); ry -= 14
#         for item in PERSONA['Experiencia Profesional'][:6]:
#             ry = draw_wrapped_text(c, rx, ry, '- ' + item, max_width_chars=50, leading=12, size=10)
#             ry -= 4

class Template9(BaseTemplate):
    # Narrow top bar, name large left, photo small right, sections below split
    def build(self, c, foto):
        w, h = A4

        # Header
        c.setFillColorRGB(*self.palette['header'])
        c.rect(0, h-80, w, 80, fill=1)

        c.setFillColor(colors.white)
        c.setFont('Helvetica-Bold', 26)
        c.drawString(40, h-55, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])

        safe_draw_image(c, foto, w-110, h-70, 70)

        # Left column
        x = 40
        y = h-120

        c.setFont('Helvetica-Bold', 14)
        c.drawString(x, y, 'Datos Personales')
        y -= 14

        for key in ['Identificación','Nit','Fecha de Nacimiento','Sexo','Estado Civil']:
            c.setFont('Helvetica', 10)
            c.drawString(x, y, f'{key}: {PERSONA.get(key, "-")}')
            y -= 12

        # Right column
        rx = 300
        ry = h-120

        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Experiencia')
        ry -= 14

        for item in PERSONA['Experiencia Profesional'][:6]:
            ry = draw_wrapped_text(
                c,
                rx,
                ry,
                '- ' + item,
                max_width_chars=50,
                leading=12,
                size=10
            )
            ry -= 4


class Template10(BaseTemplate):
    # Footer band with contact, large centered name mid-page, skills list below
    def build(self, c, foto):
        w, h = A4
        c.setFillColorRGB(*self.palette['header']); c.rect(0, 0, w, 100, fill=1)
        c.setFillColor(colors.white); c.setFont('Helvetica-Bold', 26); c.drawCentredString(w/2, h-140, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])
        safe_draw_image(c, foto, w/2-60, h-260, 120)
        # skills and references
        x = 60; y = h-420
        c.setFont('Helvetica-Bold', 14); c.drawString(x, y, 'Habilidades'); y -= 16
        for skill in PERSONA['Habilidades'][:8]:
            c.setFont('Helvetica', 10); c.drawString(x, y, '- ' + skill); y -= 12
        y -= 6
        c.setFont('Helvetica-Bold', 14); c.drawString(x, y, 'Referencias'); y -= 14
        for ref in PERSONA['Referencias Personales'][:3]:
            y = draw_wrapped_text(c, x, y, ref, max_width_chars=90, leading=12, size=10)
            y -= 6

# Paletas de colores para cada template (RGB normalizado)
PALETTES = [
    {'header':(0.1,0.2,0.5),'titles':(0.2,0.3,0.6),'text':(0,0,0)},
    {'header':(0.2,0.5,0.2),'titles':(0.1,0.3,0.1),'text':(0,0,0)},
    {'header':(0.5,0.2,0.2),'titles':(0.4,0.1,0.1),'text':(0,0,0)},
    {'header':(0.6,0.4,0.1),'titles':(0.5,0.3,0.1),'text':(0,0,0)},
    {'header':(0.2,0.2,0.6),'titles':(0.1,0.1,0.4),'text':(0,0,0)},
    {'header':(0.6,0.1,0.4),'titles':(0.3,0.05,0.2),'text':(0,0,0)},
    {'header':(0.1,0.4,0.6),'titles':(0.05,0.2,0.4),'text':(0,0,0)},
    {'header':(0.3,0.3,0.3),'titles':(0.2,0.2,0.2),'text':(0,0,0)},
    {'header':(0.4,0.1,0.6),'titles':(0.2,0.05,0.4),'text':(0,0,0)},
    {'header':(0.1,0.6,0.6),'titles':(0.05,0.4,0.4),'text':(0,0,0)},
]

TEMPLATES = [Template1,Template2,Template3,Template4,Template5,Template6,Template7,Template8,Template9,Template10]

if __name__ == '__main__':
    fotos = [foto0,foto1,foto2,foto3,foto4,foto0,foto1,foto2,foto3,foto4]
    for i, Temp in enumerate(TEMPLATES):
        out = f'CV_COMPLETO_{i+1}.pdf'
        try:
            Temp(PALETTES[i]).generar_pdf(out, fotos[i])
            print('Generado ->', out)
        except Exception as e:
            print('Fallo al generar', out, '->', e)
