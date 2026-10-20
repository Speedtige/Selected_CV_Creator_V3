# import os, sys, textwrap
# from datetime import datetime
# from reportlab.lib.pagesizes import A4, LETTER
# from reportlab.pdfgen import canvas
# from reportlab.lib import colors
# from reportlab.lib.units import cm
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

# # --- (Tus clases Path y el diccionario PERSONA van aquí, sin cambios) ---
# class Path:
#     def resource_path(relative_path):
#         try:
#             base_path = sys._MEIPASS
#         except Exception:
#             base_path = os.path.abspath(".")
#         return os.path.join(base_path, relative_path)

# img_base = Path.resource_path("Avatares")
# foto0 = f"{img_base}/0.png"
# # ... (fotos 1, 2, 3, 4)
# PERSONA = {
#     # ... (Todo tu diccionario PERSONA va aquí, sin cambios)
#     "Estudiante": "________________________________________",
#     "Nombres": "Cristian Manolo",
#     "Apellidos": "Veliz Cano",
#     # ... (resto del diccionario)
#     "Pie de Página": f"CV Actualizado a {datetime.now().strftime('%Y-%m-%d')}"
# }


# # --- Funciones de ayuda (puedes mantener las tuyas o usar estas) ---
# def safe_draw_image(c, img_path, x, y, size):
#     try:
#         if img_path and os.path.exists(img_path):
#             c.drawImage(img_path, x, y, width=size, height=size, mask='auto')
#     except Exception:
#         pass # O dibujar un placeholder si quieres

# # --- Clase Base de Plantillas ---
# class BaseTemplate:
#     def __init__(self, palette, page_size=A4):
#         self.palette = palette
#         self.page_size = page_size

#     def generar_pdf(self, filename, foto_path):
#         c = canvas.Canvas(filename, pagesize=self.page_size)
#         self.build(c, foto_path)
#         c.showPage()
#         c.save()

# # --- PLANTILLA 1: Estilo Moderno de Dos Columnas (similar a la tuya) ---
# class Template1(BaseTemplate):
#     def build(self, c, foto):
#         w, h = self.page_size
#         margin = 40
#         col_width = (w - 3 * margin) / 2
        
#         # Header
#         c.setFillColorRGB(*self.palette['header'])
#         c.rect(0, h - 100, w, 100, fill=1, stroke=0)
#         c.setFillColor(colors.white)
#         c.setFont('Helvetica-Bold', 28)
#         c.drawString(margin, h - 50, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])
#         c.setFont('Helvetica', 14)
#         c.drawString(margin, h - 75, PERSONA['Profesión'])
#         safe_draw_image(c, foto, w - 120, h - 90, 80)

#         # Columnas
#         y_start = h - 120
        
#         # Columna Izquierda
#         self._draw_section(c, "Experiencia", PERSONA['Experiencia Profesional'], margin, y_start, col_width)
#         self._draw_section(c, "Habilidades", PERSONA['Habilidades Izquierda'], margin, 400, col_width)
#         self._draw_section(c, "Intereses", [PERSONA['Intereses Izquierda']], margin, 250, col_width)

#         # Columna Derecha
#         right_col_x = margin * 2 + col_width
#         self._draw_section(c, "Datos Personales", [f"{k}: {v}" for k, v in PERSONA['Datos Personales Derecha'].items()], right_col_x, y_start, col_width)
#         self._draw_section(c, "Idiomas", PERSONA['Idiomas Derecha'], right_col_x, 400, col_width)
#         self._draw_section(c, "Certificaciones", PERSONA['Certificaciones Derecha'], right_col_x, 250, col_width)
        
#         self._draw_footer(c, w, h)

#     def _draw_section(self, c, title, items, x, y, width):
#         c.setFillColor(colors.black)
#         c.setFont('Helvetica-Bold', 14)
#         c.drawString(x, y, title)
#         y -= 20
#         c.setFont('Helvetica', 10)
#         for item in items:
#             # Texto simple para este ejemplo
#             c.drawString(x, y, f"- {item}")
#             y -= 15
#             if y < 100: # Evitar que se salga de la página
#                 return

#     def _draw_footer(self, c, w, h):
#         c.setFillColorRGB(*self.palette['header'])
#         c.rect(0, 0, w, 30, fill=1, stroke=0)
#         c.setFillColor(colors.white)
#         c.setFont('Helvetica', 10)
#         c.drawCentredString(w / 2, 10, PERSONA['Pie de Página'])

# # --- PLANTILLA 2: Estilo Clásico de una Columna ---
# class Template2(BaseTemplate):
#     def build(self, c, foto):
#         w, h = self.page_size
#         margin = 50
        
#         # Foto y Nombre en la parte superior
#         safe_draw_image(c, foto, margin, h - 150, 100)
#         c.setFillColor(colors.black)
#         c.setFont('Helvetica-Bold', 24)
#         c.drawString(margin + 110, h - 130, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])
#         c.setFont('Helvetica-Oblique', 14)
#         c.drawString(margin + 110, h - 150, PERSONA['Profesión'])
        
#         # Línea separadora
#         c.setStrokeColorRGB(*self.palette['header'])
#         c.setLineWidth(2)
#         c.line(margin, h - 170, w - margin, h - 170)

#         # Contenido de una columna
#         y_pos = h - 200
#         sections = [
#             ("Resumen Profesional", [PERSONA.get('Intereses Izquierda', 'Sin resumen.')]),
#             ("Experiencia Profesional", PERSONA['Experiencia Profesional']),
#             ("Formación Académica", [PERSONA['Formación Académica']]),
#             ("Habilidades", PERSONA['Habilidades']),
#             ("Referencias", PERSONA['Referencias Laborales Izquierda'] + PERSONA['Referencias Personales Izquierda'])
#         ]
        
#         for title, items in sections:
#             c.setFillColorRGB(*self.palette['titles'])
#             c.setFont('Helvetica-Bold', 16)
#             c.drawString(margin, y_pos, title)
#             y_pos -= 25
            
#             c.setFillColor(colors.black)
#             c.setFont('Helvetica', 11)
#             for item in items:
#                 # Usamos textwrap para que no se salga de los márgenes
#                 lines = textwrap.wrap(item, width=80)
#                 for line in lines:
#                     c.drawString(margin, y_pos, line)
#                     y_pos -= 14
#                 y_pos -= 5 # Espacio entre items
#             y_pos -= 15 # Espacio entre secciones


import os, sys, textwrap
from datetime import datetime
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm

# --- (Tus clases Path y el diccionario PERSONA van aquí, sin cambios) ---
class Path:
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

img_base = Path.resource_path("Avatares")
foto0 = f"{img_base}/0.png"
# ... (fotos 1, 2, 3, 4)
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


# --- Funciones de ayuda (puedes mantener las tuyas o usar estas) ---
def safe_draw_image(c, img_path, x, y, size):
    try:
        if img_path and os.path.exists(img_path):
            c.drawImage(img_path, x, y, width=size, height=size, mask='auto')
    except Exception:
        pass

# --- Clase Base de Plantillas ---
class BaseTemplate:
    def __init__(self, palette, page_size=A4):
        self.palette = palette
        self.page_size = page_size

    def generar_pdf(self, filename, foto_path):
        c = canvas.Canvas(filename, pagesize=self.page_size)
        self.build(c, foto_path)
        c.showPage()
        c.save()

# --- PLANTILLA 1: Estilo Moderno de Dos Columnas ---
class Template1(BaseTemplate):
    def build(self, c, foto):
        w, h = self.page_size
        margin = 40
        col_width = (w - 3 * margin) / 2
        
        # Header
        c.setFillColorRGB(*self.palette['header'])
        c.rect(0, h - 100, w, 100, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont('Helvetica-Bold', 28)
        c.drawString(margin, h - 50, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])
        c.setFont('Helvetica', 14)
        c.drawString(margin, h - 75, PERSONA['Profesión'])
        safe_draw_image(c, foto, w - 120, h - 90, 80)

        # Columnas
        y_start = h - 120
        
        # Columna Izquierda
        self._draw_section(c, "Experiencia", PERSONA['Experiencia Profesional'], margin, y_start, col_width)
        self._draw_section(c, "Habilidades", PERSONA['Habilidades Izquierda'], margin, 400, col_width)
        self._draw_section(c, "Intereses", [PERSONA['Intereses Izquierda']], margin, 250, col_width)

        # Columna Derecha
        right_col_x = margin * 2 + col_width
        self._draw_section(c, "Datos Personales", [f"{k}: {v}" for k, v in PERSONA['Datos Personales Derecha'].items()], right_col_x, y_start, col_width)
        self._draw_section(c, "Idiomas", PERSONA['Idiomas Derecha'], right_col_x, 400, col_width)
        
        self._draw_footer(c, w, h)

    def _draw_section(self, c, title, items, x, y, width):
        c.setFillColor(colors.black)
        c.setFont('Helvetica-Bold', 14)
        c.drawString(x, y, title)
        y -= 20
        c.setFont('Helvetica', 10)
        for item in items:
            c.drawString(x, y, f"- {item}")
            y -= 15
            if y < 100:
                return

    def _draw_footer(self, c, w, h):
        c.setFillColorRGB(*self.palette['header'])
        c.rect(0, 0, w, 30, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont('Helvetica', 10)
        c.drawCentredString(w / 2, 10, PERSONA['Pie de Página'])

# --- PLANTILLA 2: Estilo Clásico de una Columna (COMPLETADA) ---
class Template2(BaseTemplate):
    def build(self, c, foto):
        w, h = self.page_size
        margin = 50
        
        # Foto y Nombre en la parte superior
        safe_draw_image(c, foto, margin, h - 150, 100)
        c.setFillColor(colors.black)
        c.setFont('Helvetica-Bold', 24)
        c.drawString(margin + 110, h - 130, PERSONA['Nombres'] + ' ' + PERSONA['Apellidos'])
        c.setFont('Helvetica-Oblique', 14)
        c.drawString(margin + 110, h - 150, PERSONA['Profesión'])
        
        # Línea separadora
        c.setStrokeColorRGB(*self.palette['header'])
        c.setLineWidth(2)
        c.line(margin, h - 170, w - margin, h - 170)

        # Contenido de una columna
        y_pos = h - 200
        sections = [
            ("Resumen Profesional", [PERSONA.get('Intereses Izquierda', 'Sin resumen.')]),
            ("Experiencia Profesional", PERSONA['Experiencia Profesional']),
            ("Formación Académica", [PERSONA['Formación Académica']]),
            ("Habilidades", PERSONA['Habilidades']),
            ("Referencias", PERSONA['Referencias Laborales Izquierda'] + PERSONA['Referencias Personales Izquierda'])
        ]
        
        for title, items in sections:
            c.setFillColorRGB(*self.palette['titles'])
            c.setFont('Helvetica-Bold', 16)
            c.drawString(margin, y_pos, title)
            y_pos -= 25
            
            c.setFillColor(colors.black)
            c.setFont('Helvetica', 11)
            for item in items:
                lines = textwrap.wrap(item, width=80)
                for line in lines:
                    c.drawString(margin, y_pos, line)
                    y_pos -= 14
                y_pos -= 5
            y_pos -= 15
        
        # ---> TERMINACIÓN DEL CÓDIGO
        # Pie de página simple
        c.setFillColor(colors.grey)
        c.setFont('Helvetica-Oblique', 9)
        c.drawCentredString(w / 2, 30, PERSONA['Pie de Página'])

# # --- PLANTILLA 3: Estilo Minimalista con Barra Lateral ---
# class Template3(BaseTemplate):
#     def build(self, c, foto):
#         w, h = self.page_size
        
#         # Barra lateral izquierda
#         c.setFillColorRGB(*self.palette['header'])
#         c.rect(0, 0, 180, h, fill=1, stroke=0)
        
#         # Foto en la barra lateral
#         safe_draw_image(c, foto, 40, h - 150, 100)
        
#         # Nombre y Profesión en la barra lateral
#         c.setFillColor(colors.white)
#         c.setFont('Helvetica-Bold', 18)
#         c.drawCentredString(90, h - 280, PERSON

# --- PLANTILLA 3: Estilo Minimalista con Barra Lateral ---
class Template3(BaseTemplate):
    def build(self, c, foto):
        w, h = self.page_size
        
        # Barra lateral izquierda
        c.setFillColorRGB(*self.palette['header'])
        c.rect(0, 0, 180, h, fill=1, stroke=0)
        
        # Foto en la barra lateral
        safe_draw_image(c, foto, 40, h - 150, 100)
        
        # Nombre y Profesión en la barra lateral
        c.setFillColor(colors.white)
        c.setFont('Helvetica-Bold', 18)
        c.drawCentredString(90, h - 280, PERSONA['Nombres'])
        c.setFont('Helvetica', 12)
        c.drawCentredString(90, h - 300, PERSONA['Profesión'])
        
        # Datos Personales en la barra lateral
        y_pos = h - 350
        c.setFont('Helvetica-Bold', 12)
        c.drawString(20, y_pos, "Datos")
        y_pos -= 20
        c.setFont('Helvetica', 10)
        for key, value in PERSONA['Datos Personales Derecha'].items():
            c.drawString(20, y_pos, f"{key}: {value}")
            y_pos -= 15
            if y_pos < 100: break # Evitar que se salga

        # Contenido principal (a la derecha de la barra)
        main_x = 200
        main_y = h - 100
        main_width = w - main_x - 40
        
        # Título principal
        c.setFillColor(colors.black)
        c.setFont('Helvetica-Bold', 24)
        c.drawString(main_x, main_y, "Perfil Profesional")
        main_y -= 40
        
        # Resumen
        c.setFont('Helvetica', 11)
        resumen_lines = textwrap.wrap(PERSONA['Intereses Izquierda'], width=70)
        for line in resumen_lines:
            c.drawString(main_x, main_y, line)
            main_y -= 14
        main_y -= 25
        
        # Secciones
        sections_to_draw = [
            ("Experiencia", PERSONA['Experiencia Profesional']),
            ("Habilidades", PERSONA['Habilidades Izquierda']),
            ("Idiomas", PERSONA['Idiomas Derecha'])
        ]
        
        for title, items in sections_to_draw:
            c.setFont('Helvetica-Bold', 16)
            c.drawString(main_x, main_y, title)
            main_y -= 20
            c.setFont('Helvetica', 10)
            for item in items:
                c.drawString(main_x + 20, main_y, f"- {item}")
                main_y -= 15
            main_y -= 20

# --- BLOQUE PRINCIPAL PARA GENERAR LOS PDFs ---
if __name__ == '__main__':
    # Paleta de colores para cada plantilla
    palette1 = {'header': (0.2, 0.4, 0.8), 'titles': (0.1, 0.2, 0.4), 'text': (0, 0, 0)} # Azul
    palette2 = {'header': (0.7, 0.1, 0.1), 'titles': (0.5, 0.05, 0.05), 'text': (0, 0, 0)} # Rojo
    palette3 = {'header': (0.2, 0.6, 0.2), 'titles': (0.1, 0.3, 0.1), 'text': (0, 0, 0)} # Verde

    # Ruta a una foto de ejemplo (asegúrate de que exista o el código la saltará)
    # He usado foto0 como ejemplo, puedes cambiarla por cualquiera
    foto_a_usar = foto0 

    print("Generando PDFs...")

    # Generar la Plantilla 1
    Template1(palette1, page_size=LETTER).generar_pdf('CV_Template1_Moderno.pdf', foto_a_usar)
    print("Generado -> CV_Template1_Moderno.pdf")

    # Generar la Plantilla 2
    Template2(palette2, page_size=LETTER).generar_pdf('CV_Template2_Clasico.pdf', foto_a_usar)
    print("Generado -> CV_Template2_Clasico.pdf")

    # Generar la Plantilla 3
    Template3(palette3, page_size=LETTER).generar_pdf('CV_Template3_Minimalista.pdf', foto_a_usar)
    print("Generado -> CV_Template3_Minimalista.pdf")

    print("¡Todos los PDFs han sido creados con éxito!")
