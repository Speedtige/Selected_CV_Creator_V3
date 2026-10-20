
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys, os

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QHBoxLayout, QPushButton, QLabel, QFileDialog, QStackedWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
##====================================================================================
# --- Clase para manejo de rutas de recursos (Sin cambios) ---
##====================================================================================
class Path():

    # =========================
    # ✨ Debuelve, la Dirección Exacta de Cualquier, Archivo dentro de la App-Desk
    # =========================
    def resource_path(relative_path):    ## Forma #1 resource_path(relative_path)
        """Get absolute path to resource, works for dev and for pyinstaller"""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    # =========================
    # ✨ Debuelve, la Dirección Exacta de Cualquier, Archivo dentro de la App-Desk
    # =========================
    def resource_path_app():    ## Forma #2 resource_path_app()

        try:
            path_app = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))

        except Exception as e:
            print(e)

        except IOError as error:
            print( error )

        return path_app

class ImageViewer(QWidget):

    def __init__(self):
        super().__init__()

        # Ruta de la imagen
        img_path = Path.resource_path("Ico\\1.ico")

        self.initUI()
        self.center_on_screen()

    def initUI(self):

        self.setWindowTitle('Image Viewer')
        self.layout = QVBoxLayout()

        # =========================
        # CONTENEDOR DE PÁGINAS
        # =========================
        self.container = QWidget()
        self.container_layout = QVBoxLayout(self.container)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setSpacing(0)

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setStyleSheet('background-color: #252525;')

        self.container_layout.addWidget(self.stacked_widget)

        # =========================
        # SCROLL (SOLO TAB 01)
        # =========================
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.container)

        self.layout.addWidget(scroll)

        # Botón para abrir archivos
        self.open_button = QPushButton('Open Files', self)
        self.open_button.clicked.connect(self.open_files)
        self.layout.addWidget(self.open_button)

        # Botones de navegación
        self.navigation_layout = QHBoxLayout()
        self.home_button = QPushButton('Home', self)
        self.home_button.clicked.connect(self.go_to_home)
        self.prev_button = QPushButton('Previous', self)
        self.prev_button.clicked.connect(self.prev_page)
        self.next_button = QPushButton('Next', self)
        self.next_button.clicked.connect(self.next_page)
        self.navigation_layout.addWidget(self.home_button)
        self.navigation_layout.addWidget(self.prev_button)
        self.navigation_layout.addWidget(self.next_button)
        self.layout.addLayout(self.navigation_layout)

        self.setLayout(self.layout)

        self.image_paths = []
        self.current_page = 0

    def open_files(self):

        # 🔥 LIMPIAR ANTES (IMPORTANTE)
        self.clear_stack()

        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        files, _ = QFileDialog.getOpenFileNames(self, "Seleccionar Imágenes", "", "All Files (*);;Image Files (*.png *.jpg *.jpeg *.bmp *.gif *.ico *.webp)", options=options)
        if files:
            self.image_paths = files
            self.create_pages()

    def create_pages(self):
        
        num_pages = (len(self.image_paths) + 49) // 50  # Redondear hacia arriba
        for i in range(num_pages):
            page = QWidget()
            page_layout = QVBoxLayout()
            page_layout.setContentsMargins(0, 0, 0, 0)
            page_layout.setSpacing(3)

            for row in range(10):
                row_layout = QHBoxLayout()
                for col in range(10):
                    index = i * 50 + row * 5 + col
                    if index < len(self.image_paths):
                        image_path = self.image_paths[index]

                        pixmap = QPixmap(image_path).scaled(
                            100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation
                        )

                        # Crear un label con la miniatura
                        label = QLabel(self)
                        label.setPixmap(pixmap)
                        label.setScaledContents(True)
                        label.setAlignment(Qt.AlignCenter)
                        label.setScaledContents(True)

                        # Añadir el nombre del video o un número
                        name, _ = os.path.splitext(os.path.basename(image_path))
                        name_label = QLabel(name, self)
                        name_label.setFont(QFont('Arial', 6))
                        name_label.setAlignment(Qt.AlignCenter)

                        # Conectar el clic del label al método de reproducción
                        label.mousePressEvent = lambda event, vp=image_path: self.print_img(vp)

                        # Añadir el label de la miniatura y el nombre del video al layout
                        layout = QVBoxLayout()
                        layout.addWidget(label)
                        layout.addWidget(name_label)
                        row_layout.addLayout(layout)

                page_layout.addLayout(row_layout)

            page.setLayout(page_layout)
            self.stacked_widget.addWidget(page)

        # Ajustar botones de navegación
        self.update_navigation_buttons()

        # Ir a la primera página
        self.current_page = 0
        self.stacked_widget.setCurrentIndex(self.current_page)

    def print_img(self, vp):
        print(vp)
        os.startfile(vp)

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
##-------------------------------------------------------------------------
    # =========================
    # LIMPIA FUNCIONES EN: STACK INTERNO (PÁGINAS)
    # =========================
    def clear_stack(self):
        for i in reversed(range(self.stacked_widget.count())):
            widget = self.stacked_widget.widget(i)
            self.stacked_widget.removeWidget(widget)
            widget.deleteLater()

        self.current_page = 0
##-------------------------------------------------------------------------
    # =========================
    # 🎵 Centrar App
    # =========================
    def center_on_screen(self):

        screen = QApplication.primaryScreen().availableGeometry()
        w, h = 800, 600
        x = (screen.width() - w) // 2
        y = (screen.height() - h) // 2 + 10
        self.setGeometry(x, y, w, h)
##-------------------------------------------------------------------------
    # =========================
    # ✨ Metodo para Obtener Cualquier Tecla Pulsada dentro de la App.
    # =========================
    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Escape:
            sys.exit()
##-------------------------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())
##-------------------------------------------------------------------------