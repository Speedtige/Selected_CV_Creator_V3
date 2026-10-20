import os, sys, textwrap
from datetime import datetime
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
    ],
    "Pasatiempos": [
        "Leer libros de ciencia ficción",
        "Jugar fútbol",
        "Practicar yoga",
        "Caminar en la naturaleza",
        "Ver películas",
        "Escuchar música"
    ],
    "Comidas Favoritas": [
        "Pizza",
        "Sushi",
        "Tacos",
        "Pasta",
        "Hamburguesas",
        "Ensaladas"
    ],
    "Idiomas": [
        "Español (Nativo)",
        "Inglés (Intermedio)",
        "Francés (Básico)"
    ],
    "Certificaciones": [
        "Certificación en Computación",
        "Certificación en Electricidad Básica",
        "Certificación en Carpintería"
    ],
    "Proyectos Personales": [
        "Desarrollo de una aplicación móvil",
        "Creación de un blog de tecnología",
        "Participación en un proyecto de voluntariado"
    ],
    "Datos Personales Izquierda": {
        "Identificación": "XXXX XXXXX XXXX",
        "Nit": "XXXXXXXX",
        "Fecha de Nacimiento": "XX/XX/XXXX",
        "Sexo": "Masculino",
        "Estado Civil": "Soltero",
        "Dirección": "XXXXXXXX Zona X, XX CL XXXXX XXXX 0X-0",
        "Pretensión Salarial": "Q 2500.00"
    },
    "Datos Personales Derecha": {
        "Identificación": "YYYY YYYYY YYYY",
        "Nit": "YYYYYYYY",
        "Fecha de Nacimiento": "YY/YY/YYYY",
        "Sexo": "Femenino",
        "Estado Civil": "Casado",
        "Dirección": "YYYYYYYY Zona Y, YY CL YYYYY YYYY 0Y-0",
        "Pretensión Salarial": "Q 3000.00"
    },
    "Habilidades Izquierda": [
        "Manejo de Carro y Moto",
        "Carpintería básica",
        "Electricidad básica",
        "Administración básica",
        "Atención al Cliente",
        "Reparación de Hardware y Software",
        "Dibujo técnico",
        "Seguir órdenes directas"
    ],
    "Habilidades Derecha": [
        "Programación en Python",
        "Diseño Gráfico",
        "Redacción de Contenidos",
        "Gestión de Proyectos",
        "Análisis de Datos",
        "Marketing Digital",
        "Comunicación Efectiva",
        "Trabajo en Equipo"
    ],
    "Intereses Izquierda": "Que Tanto La Empresa como el Jefe o Dueño queden siempre en alto; seguir estudiando; realizar bien mis tareas; garantizar mi trabajo; ser mejor persona.",
    "Intereses Derecha": "Desarrollar nuevas habilidades; viajar y conocer diferentes culturas; aprender sobre tecnología; contribuir a proyectos comunitarios; mejorar mis competencias profesionales.",
    "Referencias Laborales Izquierda": [
        "Lic. Henry Estuardo Ayala Dardon — Alcalde de San Lorenzo Suchitepéquez — Cel. XXXX-XXXX",
        "P.C. Narciso Morales García — Encargado RRHH Municipalidad San Lorenzo — Cel. XXXX-XXXX",
        "Ing. Jorge Eduardo Kestler — Ingeniero Supervisor Obras Municipales — Cel. XXXX-XXXX"
    ],
    "Referencias Laborales Derecha": [
        "Dr. Juan Pérez — Director de Recursos Humanos — Cel. YYYY-YYYY",
        "Ing. María López — Gerente de Proyectos — Cel. YYYY-YYYY",
        "Lic. Carlos Gómez — Coordinador de Marketing — Cel. YYYY-YYYY"
    ],
    "Referencias Personales Izquierda": [
        "Martin López Mendoza — Profesor — Cel. XXXX-XXXX",
        "Lic. LAE. Ángel Estuardo López Mejía — Cel. XXXX-XXXX",
        "Ing. Julio Cesar Montufar Flores — Cel. XXXX-XXXX"
    ],
    "Referencias Personales Derecha": [
        "Dra. Ana Martínez — Médica — Cel. YYYY-YYYY",
        "Ing. Luis Hernández — Ingeniero Civil — Cel. YYYY-YYYY",
        "Lic. Sofia Ramírez — Abogada — Cel. YYYY-YYYY"
    ],
    "Pasatiempos Izquierda": [
        "Leer libros de ciencia ficción",
        "Jugar fútbol",
        "Practicar yoga",
        "Caminar en la naturaleza",
        "Ver películas",
        "Escuchar música"
    ],
    "Pasatiempos Derecha": [
        "Tocar guitarra",
        "Pintar",
        "Escribir cuentos",
        "Hacer senderismo",
        "Cocinar",
        "Jardinería"
    ],
    "Comidas Favoritas Izquierda": [
        "Pizza",
        "Sushi",
        "Tacos",
        "Pasta",
        "Hamburguesas",
        "Ensaladas"
    ],
    "Comidas Favoritas Derecha": [
        "Ceviche",
        "Pollo al horno",
        "Ensalada de frutas",
        "Sopa de pollo",
        "Arroz con pollo",
        "Postre de chocolate"
    ],
    "Idiomas Izquierda": [
        "Español (Nativo)",
        "Inglés (Intermedio)",
        "Francés (Básico)"
    ],
    "Idiomas Derecha": [
        "Español (Nativo)",
        "Inglés (Avanzado)",
        "Alemán (Intermedio)"
    ],
    "Certificaciones Izquierda": [
        "Certificación en Computación",
        "Certificación en Electricidad Básica",
        "Certificación en Carpintería"
    ],
    "Certificaciones Derecha": [
        "Certificación en Marketing Digital",
        "Certificación en Gestión de Proyectos",
        "Certificación en Análisis de Datos"
    ],
    "Proyectos Personales Izquierda": [
        "Desarrollo de una aplicación móvil",
        "Creación de un blog de tecnología",
        "Participación en un proyecto de voluntariado"
    ],
    "Proyectos Personales Derecha": [
        "Desarrollo de una página web",
        "Creación de un canal de YouTube",
        "Participación en un hackathon"
    ],
    "Pie de Página": f"CV Actualizado a {datetime.now().strftime('%Y-%m-%d')}"
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

        # Dibujar las columnas
        c.setFillColor(colors.white)
        c.rect(30, 50, w/2 - 40, h-130, fill=1, stroke=1)
        c.rect(w/2 + 10, 50, w/2 - 40, h-130, fill=1, stroke=1)

        x = 40
        y = h-120
        c.setFillColor(colors.black)
        c.setFont('Helvetica-Bold', 14)
        c.drawString(x, y, 'Experiencia')
        y -= 12
        for it in PERSONA['Experiencia Profesional']:
            y = draw_wrapped_text(c, x, y, '- ' + it, max_width_chars=50, leading=10, size=9)
            y -= 4
        y -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(x, y, 'Habilidades')
        y -= 12
        for skill in PERSONA['Habilidades Izquierda']:
            y = draw_wrapped_text(c, x, y, '- ' + skill, max_width_chars=50, leading=10, size=9)
            y -= 4
        y -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(x, y, 'Intereses')
        y -= 12
        y = draw_wrapped_text(c, x, y, PERSONA['Intereses Izquierda'], max_width_chars=50, leading=10, size=9)
        y -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(x, y, 'Referencias Laborales')
        y -= 12
        for ref in PERSONA['Referencias Laborales Izquierda']:
            y = draw_wrapped_text(c, x, y, '- ' + ref, max_width_chars=50, leading=10, size=9)
            y -= 4
        y -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(x, y, 'Referencias Personales')
        y -= 12
        for ref in PERSONA['Referencias Personales Izquierda']:
            y = draw_wrapped_text(c, x, y, '- ' + ref, max_width_chars=50, leading=10, size=9)
            y -= 4
        # y -= 10
        # c.setFont('Helvetica-Bold', 14)
        # c.drawString(x, y, 'Pasatiempos')
        # y -= 12
        # for hobby in PERSONA['Pasatiempos Izquierda']:
        #     y = draw_wrapped_text(c, x, y, '- ' + hobby, max_width_chars=50, leading=10, size=9)
        #     y -= 4
        # y -= 10
        # c.setFont('Helvetica-Bold', 14)
        # c.drawString(x, y, 'Comidas Favoritas')
        # y -= 12
        # for food in PERSONA['Comidas Favoritas Izquierda']:
        #     y = draw_wrapped_text(c, x, y, '- ' + food, max_width_chars=50, leading=10, size=9)
        #     y -= 4

        rx = 320
        ry = h-120
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Datos Personales')
        ry -= 12
        for key in ['Identificación', 'Nit', 'Fecha de Nacimiento', 'Sexo', 'Estado Civil', 'Dirección', 'Pretensión Salarial']:
            c.setFont('Helvetica', 9)
            c.drawString(rx, ry, f'{key}: {PERSONA["Datos Personales Derecha"].get(key, "-")}')
            ry -= 11
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Idiomas')
        ry -= 12
        for language in PERSONA['Idiomas Derecha']:
            ry = draw_wrapped_text(c, rx, ry, '- ' + language, max_width_chars=50, leading=10, size=9)
            ry -= 4
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Certificaciones')
        ry -= 12
        for cert in PERSONA['Certificaciones Derecha']:
            ry = draw_wrapped_text(c, rx, ry, '- ' + cert, max_width_chars=50, leading=10, size=9)
            ry -= 4
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Proyectos Personales')
        ry -= 12
        for project in PERSONA['Proyectos Personales Derecha']:
            ry = draw_wrapped_text(c, rx, ry, '- ' + project, max_width_chars=50, leading=10, size=9)
            ry -= 4
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Habilidades')
        ry -= 12
        for skill in PERSONA['Habilidades Derecha']:
            ry = draw_wrapped_text(c, rx, ry, '- ' + skill, max_width_chars=50, leading=10, size=9)
            ry -= 4
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Intereses')
        ry -= 12
        ry = draw_wrapped_text(c, rx, ry, PERSONA['Intereses Derecha'], max_width_chars=50, leading=10, size=9)
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Referencias Laborales')
        ry -= 12
        for ref in PERSONA['Referencias Laborales Derecha']:
            ry = draw_wrapped_text(c, rx, ry, '- ' + ref, max_width_chars=50, leading=10, size=9)
            ry -= 4
        ry -= 10
        c.setFont('Helvetica-Bold', 14)
        c.drawString(rx, ry, 'Referencias Personales')
        ry -= 12
        for ref in PERSONA['Referencias Personales Derecha']:
            ry = draw_wrapped_text(c, rx, ry, '- ' + ref, max_width_chars=50, leading=10, size=9)
            ry -= 4
        # ry -= 10
        # c.setFont('Helvetica-Bold', 14)
        # c.drawString(rx, ry, 'Pasatiempos')
        # ry -= 12
        # for hobby in PERSONA['Pasatiempos Derecha']:
        #     ry = draw_wrapped_text(c, rx, ry, '- ' + hobby, max_width_chars=50, leading=10, size=9)
        #     ry -= 4
        # ry -= 10
        # c.setFont('Helvetica-Bold', 14)
        # c.drawString(rx, ry, 'Comidas Favoritas')
        # ry -= 12
        # for food in PERSONA['Comidas Favoritas Derecha']:
        #     ry = draw_wrapped_text(c, rx, ry, '- ' + food, max_width_chars=50, leading=10, size=9)
        #     ry -= 4
        self.draw_footer(c, w, h)

    def draw_footer(self, c, w, h):
        footer_y = 50
        c.rect(0, footer_y - 20, w, 20, fill=1)
        c.setFillColor(colors.white)
        c.setFont('Helvetica-Bold', 10)
        #c.drawCentredString(w / 2, footer_y - 10, 'CV Actualizado')
        c.setFont('Helvetica', 10)
        c.drawCentredString(w / 2, footer_y - 13, PERSONA['Pie de Página'])
        c.setFillColor(colors.black)
        c.line(40, footer_y - 15, w - 40, footer_y - 15)

if __name__ == '__main__':
    palette = {'header': (0.4, 0.1, 0.6), 'titles': (0.2, 0.05, 0.4), 'text': (0, 0, 0)}
    foto = foto4
    Template9(palette, page_size=LETTER).generar_pdf('CV_template_16.pdf', foto)
    print('Generado -> CV_template_16.pdf')