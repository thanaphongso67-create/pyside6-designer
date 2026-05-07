import sys
from PySide6.QtWidgets import QApplication, QMainWindow
# นำเข้า UI ที่เราเพิ่งแปลงมา
from ui_main import Ui_MainWindow 

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ตั้งค่า UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # --- ถ้าอยากเขียนให้ปุ่มทำงาน ให้เขียนต่อตรงนี้ ---
        # ตัวอย่าง: self.ui.pushButton.clicked.connect(self.say_hello)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())