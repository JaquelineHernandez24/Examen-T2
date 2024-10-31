import requests
from PyQt5.QtWidgets import QMessageBox

class DatabaseClient:
    def __init__(self, url):
        self.url = url

    def fetch_all_records(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()
            print("Datos obtenidos de la API:", data)  # Verificar datos aquí
            return data
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(None, "Error", f"No se pudo conectar con el servidor: {e}")
            return []
