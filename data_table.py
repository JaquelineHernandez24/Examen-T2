
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class DataTable(QTableWidget):
    def __init__(self, headers, rows, columns):
        super().__init__(rows, columns)
        self.setHorizontalHeaderLabels(headers)

    def load_data(self, data):
        # Verificar que data sea una lista de diccionarios
        if not isinstance(data, list) or (data and not isinstance(data[0], dict)):
            print("Error: los datos deben ser una lista de diccionarios.")
            return

        self.setRowCount(len(data))
        for row_idx, record in enumerate(data):
            self.setItem(row_idx, 0, QTableWidgetItem(str(record.get("id", ""))))
            self.setItem(row_idx, 1, QTableWidgetItem(record.get("name", "")))
            self.setItem(row_idx, 2, QTableWidgetItem(record.get("lastname", "")))
            self.setItem(row_idx, 3, QTableWidgetItem(record.get("city", "")))
            self.setItem(row_idx, 4, QTableWidgetItem(record.get("street", "")))
            self.setItem(row_idx, 5, QTableWidgetItem(record.get("registrationMonth", "")))

    def clear(self):
        self.setRowCount(0)
