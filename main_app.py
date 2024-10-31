from PyQt5.QtWidgets import QMainWindow
from main_window import MainWindow  # Asegúrate de que esta importación sea correcta
from database_client import DatabaseClient  # Importa tu cliente de base de datos

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_client = DatabaseClient("https://6721118a98bbb4d93ca75401.mockapi.io/api/v1/users")  # Cambia la URL si es necesario
        self.window = MainWindow(self.db_client)
        self.setCentralWidget(self.window)
