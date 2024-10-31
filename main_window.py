from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox, QHBoxLayout
from PyQt5.QtCore import Qt
from data_table import DataTable  # Asegúrate de tener esta clase bien definida

class MainWindow(QMainWindow):
    def __init__(self, db_client):
        super().__init__()
        self.db_client = db_client
        self.setWindowTitle("Aplicación de Genética Personalizada")
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: #add8e6;")
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        # Textbox para que el usuario ingrese el número de registros a mostrar
        self.record_count_input = QLineEdit(self)
        self.record_count_input.setPlaceholderText("Número de registros a mostrar")
        main_layout.addWidget(self.record_count_input)

        # Layout horizontal para botones y tabla
        h_layout = QHBoxLayout()

        # Botones de control
        load_all_button = QPushButton("Cargar Todos los Registros")
        load_last_button = QPushButton("Cargar Último Registro")
        clear_button = QPushButton("Borrar Tabla")

        # Conectar los eventos de los botones a las funciones
        load_all_button.clicked.connect(self.load_all_records)
        load_last_button.clicked.connect(self.load_last_record)
        clear_button.clicked.connect(self.clear_table)

        # Añadir botones al layout horizontal
        h_layout.addWidget(load_all_button)
        h_layout.addWidget(load_last_button)
        h_layout.addWidget(clear_button)

        # Añadir el layout horizontal al layout principal
        main_layout.addLayout(h_layout)

        # Tabla de datos con 6 columnas (incluyendo Mes de Registro)
        self.table = DataTable(["ID", "Nombre", "Apellido", "Ciudad", "Calle", "Mes de Registro"], 0, 6)
        main_layout.addWidget(self.table)

        # Configurar el contenedor de la ventana
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def load_all_records(self):
        data = self.db_client.fetch_all_records()
        if data:
            try:
                record_limit = int(self.record_count_input.text())
                if record_limit <= 0:
                    raise ValueError("El número debe ser mayor que 0")
                self.table.load_data(data[:record_limit])  # Cargar solo el número de registros especificado
            except ValueError:
                QMessageBox.warning(self, "Advertencia", "Por favor, ingrese un número válido.")
        else:
            QMessageBox.information(self, "Info", "No se encontraron registros.")



    def load_last_record(self):
        data = self.db_client.fetch_all_records()
        if data:
            self.table.load_data([data[-1]])  # Solo cargar el último registro

    def clear_table(self):
        self.table.clear()
