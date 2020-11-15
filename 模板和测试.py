from PyQt5.Qt import *

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('xx')
        self.resize(500, 500)
        self.set_ui()

    def set_ui(self):
        $coder$

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()


    sys.exit(app.exec())

        