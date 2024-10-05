import sys
from PyQt5 import QtWidgets, QtCore

class CustomLineEdit(QtWidgets.QTextEdit):
    def __init__(self, *args, **kwargs):
        super(CustomLineEdit, self).__init__(*args, **kwargs)

    # Override keyPressEvent to intercept Tab key
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Tab:
            # Move focus to the next widget instead of inserting a tab space
            self.focusNextChild()
        else:
            # Call the default keyPressEvent for other keys
            super(CustomLineEdit, self).keyPressEvent(event)

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up window
        self.setWindowTitle('Tab Key Example')
        self.setGeometry(100, 100, 300, 200)

        # Layout setup
        layout = QtWidgets.QVBoxLayout()

        # Custom QLineEdit (text input) widgets
        self.textInput1 = CustomLineEdit(self)
        self.textInput2 = CustomLineEdit(self)
        self.textInput3 = CustomLineEdit(self)

        # Add widgets to layout
        layout.addWidget(QtWidgets.QLabel("Input 1:"))
        layout.addWidget(self.textInput1)
        layout.addWidget(QtWidgets.QLabel("Input 2:"))
        layout.addWidget(self.textInput2)
        layout.addWidget(QtWidgets.QLabel("Input 3:"))
        layout.addWidget(self.textInput3)

        # Set the layout for the window
        self.setLayout(layout)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
