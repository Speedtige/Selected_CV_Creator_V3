import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QStackedWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QSize

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.image_paths = []
        self.current_page = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Viewer')
        self.setGeometry(100, 100, 800, 600)
        # ---> CORRECCIÓN 4: Evitar que la ventana se redimensione sola
        #self.setFixedSize(self.size()) 

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

    def open_files(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        files, _ = QFileDialog.getOpenFileNames(self, "Seleccionar Imágenes", "", "All Files (*);;Image Files (*.png *.jpg *.jpeg *.bmp *.gif *.ico *.webp)", options=options)
        if files:
            self.image_paths = files
            self.create_pages()

    def create_pages(self):
        # ---> CORRECCIÓN: Eliminar todos los widgets del QStackedWidget correctamente
        # QStackedWidget no tiene método .clear()
        while self.stacked_widget.count():
            widget_to_remove = self.stacked_widget.widget(0)
            self.stacked_widget.removeWidget(widget_to_remove)
            widget_to_remove.deleteLater()
        
        # ---> CORRECCIÓN 1 (continuación): Usar 25 imágenes por página, no 50
        images_per_page = 25
        num_pages = (len(self.image_paths) + images_per_page - 1) // images_per_page
        
        for i in range(num_pages):
            page = QWidget()
            page_layout = QVBoxLayout()

            for row in range(5):
                row_layout = QHBoxLayout()
                for col in range(5):
                    # ---> CORRECCIÓN 1 (continuación): Calcular el índice correctamente
                    index = i * images_per_page + row * 5 + col
                    if index < len(self.image_paths):
                        image_path = self.image_paths[index]
                        
                        # ---> CORRECCIÓN 2: Imágenes más pequeñas y centradas
                        # Se usa un tamaño fijo para el label y se centra el pixmap dentro
                        pixmap = QPixmap(image_path).scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)

                        label = QLabel(self)
                        label.setFixedSize(80, 80) # Tamaño fijo del "cuadrito"
                        label.setPixmap(pixmap)
                        label.setAlignment(Qt.AlignCenter)
                        # Se elimina setScaledContents para que no se deforme

                        name, _ = os.path.splitext(os.path.basename(image_path))
                        name_label = QLabel(name, self)
                        name_label.setFont(QFont('Arial', 6))
                        name_label.setAlignment(Qt.AlignCenter)

                        # ---> CORRECCIÓN 3: El lambda ahora captura la variable 'index' correctamente
                        # para que cada imagen tenga su propio path al hacer clic
                        label.mousePressEvent = lambda event, path=image_path: self.print_img(path)

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

    def print_img(self, vp):
        # ---> CORRECCIÓN 3: Esta función ya estaba correcta, ahora el lambda le pasa el valor bien
        print(vp)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())