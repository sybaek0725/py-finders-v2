import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap
import os

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class ImageDisplay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Image Display")
        self.setGeometry(100, 100, 500, 500)
        
        self.image_label = QLabel(self)
        pixmap = QPixmap(resource_path("image.png"))
        
        # Set the pixmap on the label
        self.image_label.setPixmap(pixmap)
        self.image_label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageDisplay()
    window.show()
    sys.exit(app.exec())