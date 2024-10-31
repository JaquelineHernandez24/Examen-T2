import sys
from PyQt5.QtWidgets import QApplication
from main_app import MainApp  # Asegúrate de que esta importación sea correcta

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
