
#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
'''
CV Template Selector – Visualizador y Apertura de Plantillas de Currículum
Selected CV Creator V2 es una aplicación de escritorio desarrollada en Python con PyQt5
que permite visualizar y seleccionar plantillas de currículum (CV) a partir de una
galería de diseños.

El programa muestra una colección de plantillas de currículum en formato de vista
previa (imágenes) y permite abrir automáticamente el archivo editable correspondiente
(DOCX) para que el usuario pueda modificarlo en su procesador de texto.

Características principales:
Visualización de plantillas de currículum en formato imagen
Navegación entre diferentes diseños mediante paginación
Interfaz gráfica simple con botones de navegación
Apertura automática del archivo editable de la plantilla seleccionada
Vista previa ampliada de cada diseño
Navegación rápida entre páginas (Home / Previous / Next)
Carga automática de plantillas desde una carpeta del sistema
Interfaz centrada automáticamente en pantalla

Funcionamiento del programa:
La aplicación carga todas las plantillas disponibles desde una carpeta local.
Cada plantilla se muestra como imagen de vista previa.
El usuario puede navegar entre los diferentes diseños.
Al seleccionar una plantilla, el programa abre automáticamente el archivo DOCX
correspondiente para su edición.

Tecnologías utilizadas:
Python
PyQt5 (interfaz gráfica)
QStackedWidget para navegación entre páginas
QThread para carga de contenido
Webbrowser para abrir archivos editables

Aplicación:
Esta herramienta es útil para:
Seleccionar plantillas de currículum profesional
Crear CV de forma rápida
Visualizar diseños antes de editarlos
Sistemas de generación de CV basados en plantillas
'''
#--> Se encuentra alojado en MEGA:
#--> https://mega.nz/file/W0NyWKaC#K_tSeS3xIU5s7DCRnGe8JeWDxgcHgf9Olloj_qf-Puk

import sys
import os
import webbrowser as wb

from PyQt5 import QtCore, QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, \
    QLabel, QFileDialog, QStackedWidget, QMessageBox
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QSize, QThread, pyqtSignal

##===============================================================================
##===============================================================================

class Path():

    ##(Dir. Raiz.)
    ## Solamente para obtener el Directorio donde se encuentra Ejecutandose la app.
    def resource_path_app():    ## Forma #2

        try:
            path_app = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))

        except Exception as e:
            print(e)

        except IOError as error:
            print( error )

        return path_app

    ##=========================================================
    ##=========================================================

    def resource_path(relative_path):
        """Get absolute path to resource, works for dev and for pyinstaller"""
        try:
            #PyInstaller Create a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

##===============================================================================
##===============================================================================

bundle_dir = Path.resource_path_app()
path_imgs = os.path.join(bundle_dir, "", "")

BASE_DIR = os.path.join(bundle_dir, "", "")
PLANTILLA_DIR_WORD = path_imgs+r'Plantillas'
Ico_app = Path.resource_path('Ico\\1.png')

##===============================================================================
##===============================================================================

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.image_paths = []
        self.plantillas_word_modif = []
        self.current_page = 0
        self.initUI()

##===============================================================================
##===============================================================================

    def initUI(self):
        self.setWindowTitle('Selected_CV_Creator_V3')
        self.setGeometry(100, 100, 500, 700)
        self.setFixedSize(self.size())

        self.setWindowIcon(QIcon(Ico_app))
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.center_on_screen()
        self.message()

        # QStackedWidget para mostrar las páginas
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.setStyleSheet("background-color: #d7aeff;")
        self.layout.addWidget(self.stacked_widget)

        # Botones de navegación
        self.navigation_layout = QHBoxLayout()
        self.navigation_layout.setContentsMargins(0, 0, 0, 0)
        self.navigation_layout.setSpacing(0)

        self.home_button = QPushButton('Home', self)
        self.home_button.clicked.connect(self.go_to_home)

        self.prev_button = QPushButton('<', self)
        self.prev_button.setStyleSheet("background-color: rgba(0, 0, 0, 50); color: white;")
        self.prev_button.setFont(QFont('Arial', 20))
        self.prev_button.clicked.connect(self.prev_page)
        self.prev_button.setFixedSize(50, 50)
        self.prev_button.move(25, self.height() // 2 - 25)

        self.next_button = QPushButton('>', self)
        self.next_button.setStyleSheet("background-color: rgba(0, 0, 0, 50); color: white;")
        self.next_button.setFont(QFont('Arial', 20))
        self.next_button.clicked.connect(self.next_page)
        self.next_button.setFixedSize(50, 50)
        self.next_button.move(self.width() - 75, self.height() // 2 - 25)

        self.navigation_layout.addWidget(self.home_button)
        
        self.layout.addLayout(self.navigation_layout)

        self.setLayout(self.layout)
        self.open_files()

##===============================================================================
##===============================================================================

    def message(self):
        QMessageBox.information(self, "Aviso", "Pacienia, en lo que se Cargan los 175 Nuevos CV´s.\
            \n\nDesarrollado por: Cristian M. Veliz Cano.\
            \nDistribución:  Gratuita.\
            \n\nMuchas, Gracias...")

## Metodo para Obtener Cualquier Tecla Pulsada dentro de la App.
    def keyPressEvent(self, event):

        ## print(event.key()) 
        ## print(help(Qt.Key)) ##<-Para Obtener Alluda Sobre los Eventos al Precionar Una Tecla en el Teclado-(Key-Board).-

        if event.key() == Qt.Key_Escape: ## Key Board (Teclado - Tecla Escape (ESC))
            sys.exit()              ## Exit (Clouse App) Cerrar la Aplicación
        
    def center_on_screen(self):

        screen = QApplication.primaryScreen().availableGeometry()
        w, h = self.width(), self.height()
        x = (screen.width() - w) // 2
        y = (screen.height() - h) // 2
        self.setGeometry(x, y, w, h)

    def open_files(self):

        PLANTILLA_DIR_WORD_PATH = os.listdir(PLANTILLA_DIR_WORD)

        for x in PLANTILLA_DIR_WORD_PATH:
            if x.endswith('.png'):
                self.image_paths.append(f'{PLANTILLA_DIR_WORD}/{x}')

        try:

            self.worker = PageWorker(self.image_paths)
            self.worker.pages_ready.connect(self.create_pages)  # Signal -> slot
            self.worker.start()


        except Exception as e:
            print(e)

        #self.create_pages()

##===============================================================================
##===============================================================================

    def create_pages(self):
        while self.stacked_widget.count():
            widget_to_remove = self.stacked_widget.widget(0)
            self.stacked_widget.removeWidget(widget_to_remove)
            widget_to_remove.deleteLater()
        
        images_per_page = 1
        num_pages = (len(self.image_paths) + images_per_page - 1) // images_per_page
        cant_plantillas = len(self.image_paths)+1
        print(cant_plantillas)
        
        for i in range(num_pages):
            
            page = QWidget()
            page_layout = QVBoxLayout()
            page_layout.setContentsMargins(0, 0, 0, 0)
            page_layout.setSpacing(0)

            for row in range(1):
                
                row_layout = QHBoxLayout()
                page_layout.setContentsMargins(0, 0, 0, 0)
                page_layout.setSpacing(2)

                for col in range(1):
                    index = i * images_per_page + row * 1 + col

                    if index < len(self.image_paths):
                        image_path = self.image_paths[index]
                        
                        # ---> CORRECCIÓN 2: Crear el label sin un tamaño fijo
                        label = QLabel(self)
                        # label.setFixedSize(80, 80) # <--- ESTA LÍNEA SE ELIMINA
                        label.setAlignment(Qt.AlignCenter)
                        
                        # Cargar el pixmap original sin escalarlo todavía
                        pixmap = QPixmap(image_path).scaled(1000, 1000, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                        label.setPixmap(pixmap) # Poner el pixmap original
                        label.setScaledContents(True)

                        name, _ = os.path.splitext(os.path.basename(image_path))
                        cant = cant_plantillas
                        name_label = QLabel(f'{name}    -   {cant}', self)
                        name_label.setFont(QFont('Arial', 14))
                        name_label.setAlignment(Qt.AlignCenter)

                        label.mousePressEvent = lambda event, path=image_path: self.open_file_CV(path)

                        layout = QVBoxLayout()
                        layout.addWidget(label)
                        layout.addWidget(name_label)
                        row_layout.addLayout(layout)

                page_layout.addLayout(row_layout)

            page.setLayout(page_layout)
            self.stacked_widget.addWidget(page)

        self.update_navigation_buttons()
        self.current_page = 0
        self.stacked_widget.setCurrentIndex(self.current_page)

    def open_file_CV(self, vp):
        print(vp)

        try:

            fpath, fname = os.path.split(vp)
            text = f'Plantillas_reportlab'

            name = fname.replace(".png", ".docx")
            path_plantilla = f'{fpath}/{name}'
            print(path_plantilla)

            wb.open_new(path_plantilla)

        except Exception as e:
            print(e)

    def go_to_home(self):
        self.current_page = 0
        self.stacked_widget.setCurrentIndex(self.current_page)
        self.update_navigation_buttons()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.stacked_widget.setCurrentIndex(self.current_page)
            self.update_navigation_buttons()

    def next_page(self):
        if self.current_page < self.stacked_widget.count() - 1:
            self.current_page += 1
            self.stacked_widget.setCurrentIndex(self.current_page)
            self.update_navigation_buttons()

    def update_navigation_buttons(self):
        self.home_button.setEnabled(self.stacked_widget.count() > 1)
        self.prev_button.setEnabled(self.current_page > 0)
        self.next_button.setEnabled(self.current_page < self.stacked_widget.count() - 1)

    def resizeEvent(self, event):

        super().resizeEvent(event)
        self.prev_button.move(25, self.height() // 2 - 25)
        self.next_button.move(self.width() - 75, self.height() // 2 - 25)

##===============================================================================
##===============================================================================

class PageWorker(QtCore.QThread):
    pages_ready = QtCore.pyqtSignal(list)

    def __init__(self, image_paths):
        super().__init__()
        self.image_paths = image_paths

    def run(self):
        pages = []
        images_per_page = 1
        num_pages = (len(self.image_paths) + images_per_page - 1) // images_per_page

        for i in range(num_pages):
            page_data = []
            for row in range(1):
                for col in range(1):
                    index = i*images_per_page + row*5 + col
                    if index < len(self.image_paths):
                        page_data.append(self.image_paths[index])
            pages.append(page_data)

        self.pages_ready.emit(pages)

##===============================================================================
##===============================================================================

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())

##===============================================================================
##===============================================================================