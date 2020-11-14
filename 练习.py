from PyQt5.Qt import *
import sys
app = QApplication(sys.argv)
window =   QWidget()
window.setWindowTitle('瞅你咋的')
window.resize(500, 500)
window.move(400, 200)

Label = QLabel(window)
Label.setText('你瞅啥')
Label.move(200, 200)

window.show()
sys.exit(app.exec_())
