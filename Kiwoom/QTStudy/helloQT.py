import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
print(sys.argv)
label = QLabel("Hello PyQt")
label1 = QPushButton("Order")
label.show()
label1.show()
app.exec()