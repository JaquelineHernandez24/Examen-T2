from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget

class SecondaryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Secundaria")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()
        label = QLabel("Esta es la ventana secundaria.")
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
