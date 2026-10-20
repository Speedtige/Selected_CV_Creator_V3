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