import sys
from PyQt5 import QtWidgets

class FormPopup(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Collection Form")
        self.setGeometry(900, 300, 800, 800)

        # Layout for the form
        layout = QtWidgets.QFormLayout()

        # Input fields
        self.mName = QtWidgets.QTextEdit(self)
        self.mCompany = QtWidgets.QTextEdit(self)
        self.currentStock = QtWidgets.QTextEdit(self)
        self.mType = QtWidgets.QTextEdit(self)
        self.mrp = QtWidgets.QTextEdit(self)
        self.ptr = QtWidgets.QTextEdit(self)
        self.gst = QtWidgets.QTextEdit(self)
        self.hsn = QtWidgets.QTextEdit(self)
        self.offer1 = QtWidgets.QTextEdit(self)
        self.offer2 = QtWidgets.QTextEdit(self)
        self.weight = QtWidgets.QTextEdit(self)

        # Add fields to the layout
        layout.addRow("Medicine Name (MName):", self.mName)
        layout.addRow("Medicine Company (MCompany):", self.mCompany)
        layout.addRow("Current Stock:", self.currentStock)
        layout.addRow("Medicine Type (MType):", self.mType)
        layout.addRow("MRP:", self.mrp)
        layout.addRow("PTR:", self.ptr)
        layout.addRow("GST:", self.gst)
        layout.addRow("HSN:", self.hsn)
        layout.addRow("Offer 1:", self.offer1)
        layout.addRow("Offer 2:", self.offer2)
        layout.addRow("Weight:", self.weight)

        # Submit button to close the form
        self.submitButton = QtWidgets.QPushButton("Submit", self)
        self.submitButton.clicked.connect(self.submitForm)

        # Add submit button to the layout
        layout.addRow(self.submitButton)

        self.setStyleSheet("""
        QTextEdit {
            border: 2px solid #4CAF50;
            border-radius: 5px;
            padding: 5px;
            font-size: 14px;
        }
        QTextEdit:focus {
            border: 2px solid #2196F3;  /* Change border color on focus */
        }
    """)

        # Set the layout
        self.setLayout(layout)

    def submitForm(self):
        # Retrieve the data from input fields (can be saved or processed further)
        form_data = {
            'MName': self.mName.text(),
            'MCompany': self.mCompany.text(),
            'CurrentStock': self.currentStock.text(),
            'MType': self.mType.text(),
            'MRP': self.mrp.text(),
            'PTR': self.ptr.text(),
            'GST': self.gst.text(),
            'HSN': self.hsn.text(),
            'Offer1': self.offer1.text(),
            'Offer2': self.offer2.text(),
            'Weight': self.weight.text(),
        }
        
        # Print the collected form data for now (you can save it or process it)
        print("Form Data Submitted:", form_data)

        # Close the popup dialog
        self.accept()


"""class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 300, 200)

        # Create a button to open the form popup
        self.button = QtWidgets.QPushButton("Open Data Collection Form", self)
        self.button.clicked.connect(self.showFormPopup)

        # Layout for the main window
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def showFormPopup(self):
        # Create and show the form popup
        form = FormPopup()
        form.exec_()

"""
"""if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())"""
