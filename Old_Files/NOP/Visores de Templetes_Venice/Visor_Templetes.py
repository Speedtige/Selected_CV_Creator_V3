import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QStackedWidget, QScrollArea
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Viewer')
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

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

        # QStackedWidget para mostrar las páginas
        self.stacked_widget = QStackedWidget(self)
        self.layout.addWidget(self.stacked_widget)

        self.setLayout(self.layout)

        self.image_paths = []
        self.current_page = 0

    def open_files(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        files, _ = QFileDialog.getOpenFileNames(self, "Open Images", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp *.gif)", options=options)
        if files:
            self.image_paths = files
            self.create_pages()

    def create_pages(self):
        
        num_pages = (len(self.image_paths) + 49) // 50  # Redondear hacia arriba
        for i in range(num_pages):

            page = QWidget()
            page_layout = QVBoxLayout()

            for row in range(5):

                row_layout = QHBoxLayout()

                for col in range(5):

                    index = i * 50 + row * 5 + col

                    if index < len(self.image_paths):

                        image_path = self.image_paths[index]
                        pixmap = QPixmap(image_path).scaled(100, 100, Qt.KeepAspectRatio)

                        # Crear un label con la miniatura
                        label = QLabel(self)
                        label.setPixmap(pixmap)
                        label.setScaledContents(True)
                        label.setAlignment(Qt.AlignCenter)

                        # Añadir el nombre del video o un número
                        name, _ = os.path.splitext(image_path)
                        name_label = QLabel(name, self)
                        name_label.setFont(QFont('Arial', 6))
                        name_label.setAlignment(Qt.AlignCenter)

                        # Conectar el clic del label al método de reproducción
                        label.mousePressEvent = lambda event, vp=image_path: ImageViewer.print_img(self, vp)

                        # Añadir el label de la miniatura y el nombre del video al layout
                        layout = QVBoxLayout()
                        layout.addWidget(label)
                        layout.addWidget(name_label)
                        row_layout.addLayout(layout)

                page_layout.addLayout(row_layout)

            page.setLayout(page_layout)
            self.stacked_widget.addWidget(page)

        # Ajustar botones de navegación
        self.home_button.setEnabled(num_pages > 1)
        self.prev_button.setEnabled(num_pages > 1)
        self.next_button.setEnabled(num_pages > 1)

        # Ir a la primera página
        self.current_page = 0
        self.stacked_widget.setCurrentIndex(self.current_page)

        self.stacked_widget.setCurrentIndex(0)
        self.home_button.setEnabled(num_pages > 1)
        self.prev_button.setEnabled(num_pages > 1)
        self.next_button.setEnabled(num_pages > 1)

    def print_img(self, vp):
        print(vp)

    def go_to_home(self):
        self.stacked_widget.setCurrentIndex(0)

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.stacked_widget.setCurrentIndex(self.current_page)

    def next_page(self):
        if self.current_page < self.stacked_widget.count() - 1:
            self.current_page += 1
            self.stacked_widget.setCurrentIndex(self.current_page)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())