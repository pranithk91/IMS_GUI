import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class BillingForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a grid layout
        grid = QtWidgets.QGridLayout()

        # Define the Roboto font for all widgets
        robotoFontBold = QtGui.QFont()
        robotoFontBold.setFamily("Roboto")
        robotoFontBold.setPointSize(14)
        robotoFontBold.setBold(True)
        robotoFontBold.setWeight(75)

        # Apply the font to the entire application by setting the default font
        self.setFont(robotoFontBold)

        # Labels and input fields
        self.billNoLabel = QtWidgets.QLabel('Bill No:')
        self.billNoLabel.setFixedWidth(181)
        self.billNoLabel.setFixedHeight(41)  # Set fixed height for labels
        self.billNoInput = QtWidgets.QLineEdit(self)
        self.billNoInput.setFixedWidth(201)
        self.billNoInput.setFixedHeight(41)  # Set fixed height for input widgets

        self.dateLabel = QtWidgets.QLabel('Date:')
        self.dateLabel.setGeometry(QtCore.QRect(10, 70, 181, 41)) 
        #self.dateLabel.setFixedHeight(41)
        self.dateInput = QtWidgets.QDateEdit(self)
        self.dateInput.setGeometry(QtCore.QRect(10, 110, 181, 51))
        #self.dateInput.setFixedWidth(201)
        #self.dateInput.setFixedHeight(41)
        self.dateInput.setCalendarPopup(True)
        self.dateInput.setDate(QtCore.QDate.currentDate())  # Set current date as default

        self.nameLabel = QtWidgets.QLabel('Name:')
        self.nameLabel.setFixedWidth(181)
        self.nameLabel.setFixedHeight(41)
        self.nameInput = QtWidgets.QLineEdit(self)
        self.nameInput.setFixedWidth(201)
        self.nameInput.setFixedHeight(41)

        self.medicineNameLabel = QtWidgets.QLabel('Medicine Name:')
        self.medicineNameLabel.setFixedWidth(181)
        self.medicineNameLabel.setFixedHeight(41)
        self.medicineNameInput = QtWidgets.QLineEdit(self)
        self.medicineNameInput.setFixedWidth(201)
        self.medicineNameInput.setFixedHeight(41)

        self.quantityLabel = QtWidgets.QLabel('Quantity:')
        self.quantityLabel.setFixedWidth(181)
        self.quantityLabel.setFixedHeight(41)
        self.quantityInput = QtWidgets.QLineEdit(self)
        self.quantityInput.setFixedWidth(201)
        self.quantityInput.setFixedHeight(41)
        self.quantityInput.setValidator(QtGui.QIntValidator(1, 1000))  # Restrict to numbers only

        self.medicineTypeLabel = QtWidgets.QLabel('Medicine Type:')
        self.medicineTypeLabel.setFixedWidth(181)
        self.medicineTypeLabel.setFixedHeight(41)
        self.medicineTypeInput = QtWidgets.QComboBox(self)
        self.medicineTypeInput.setFixedWidth(201)
        self.medicineTypeInput.setFixedHeight(41)
        self.medicineTypeInput.addItems(['Tablet', 'Syrup', 'Injection'])

        self.unitPriceLabel = QtWidgets.QLabel('Unit Price:')
        self.unitPriceLabel.setFixedWidth(181)
        self.unitPriceLabel.setFixedHeight(41)
        self.unitPriceInput = QtWidgets.QLineEdit(self)
        self.unitPriceInput.setFixedWidth(201)
        self.unitPriceInput.setFixedHeight(41)
        self.unitPriceInput.setValidator(QtGui.QDoubleValidator(0.01, 10000.00, 2))  # Float validator

        self.totalPriceLabel = QtWidgets.QLabel('Total Price:')
        self.totalPriceLabel.setFixedWidth(181)
        self.totalPriceLabel.setFixedHeight(41)
        self.totalPriceDisplay = QtWidgets.QLabel('0.00')  # Will be calculated automatically
        self.totalPriceDisplay.setFixedWidth(201)
        self.totalPriceDisplay.setFixedHeight(41)

        self.paymentModeLabel = QtWidgets.QLabel('Payment Mode:')
        self.paymentModeLabel.setFixedWidth(181)
        self.paymentModeLabel.setFixedHeight(41)
        self.paymentModeInput = QtWidgets.QComboBox(self)
        self.paymentModeInput.setFixedWidth(201)
        self.paymentModeInput.setFixedHeight(41)
        self.paymentModeInput.addItems(['Cash', 'Card', 'UPI'])

        self.billTotalLabel = QtWidgets.QLabel('Bill Total:')
        self.billTotalLabel.setFixedWidth(181)
        self.billTotalLabel.setFixedHeight(41)
        self.billTotalDisplay = QtWidgets.QLabel('0.00')  # Will display total bill amount
        self.billTotalDisplay.setFixedWidth(201)
        self.billTotalDisplay.setFixedHeight(41)

        # Add a button to calculate total price
        self.calculateButton = QtWidgets.QPushButton('Calculate Total', self)
        self.calculateButton.setFixedWidth(382)  # Make button span both columns
        self.calculateButton.setFixedHeight(41)  # Set button height
        self.calculateButton.clicked.connect(self.calculateTotal)

        # Apply the stylesheet to all labels
        label_style = "color: #17784E; background-color: #FBFBFA; font-weight: bold;"
        self.billNoLabel.setStyleSheet(label_style)
        self.dateLabel.setStyleSheet(label_style)
        self.nameLabel.setStyleSheet(label_style)
        self.medicineNameLabel.setStyleSheet(label_style)
        self.quantityLabel.setStyleSheet(label_style)
        self.medicineTypeLabel.setStyleSheet(label_style)
        self.unitPriceLabel.setStyleSheet(label_style)
        self.totalPriceLabel.setStyleSheet(label_style)
        self.paymentModeLabel.setStyleSheet(label_style)
        self.billTotalLabel.setStyleSheet(label_style)

        # Add widgets to the grid (row, column)
        #grid.addWidget(self.billNoLabel, 0, 0)
        #grid.addWidget(self.billNoInput, 1, 0)

        grid.addWidget(self.dateLabel, 0,0)
        grid.addWidget(self.dateInput, 1,0)

        #grid.addWidget(self.nameLabel, 2, 0)
        #grid.addWidget(self.nameInput, 2, 1)

        #grid.addWidget(self.medicineNameLabel, 3, 0)
        #grid.addWidget(self.medicineNameInput, 3, 1)

        """grid.addWidget(self.quantityLabel, 4, 0)
        grid.addWidget(self.quantityInput, 4, 1)

        grid.addWidget(self.medicineTypeLabel, 5, 0)
        grid.addWidget(self.medicineTypeInput, 5, 1)

        grid.addWidget(self.unitPriceLabel, 6, 0)
        grid.addWidget(self.unitPriceInput, 6, 1)

        grid.addWidget(self.totalPriceLabel, 7, 0)
        grid.addWidget(self.totalPriceDisplay, 7, 1)

        grid.addWidget(self.paymentModeLabel, 8, 0)
        grid.addWidget(self.paymentModeInput, 8, 1)

        grid.addWidget(self.billTotalLabel, 9, 0)
        grid.addWidget(self.billTotalDisplay, 9, 1)

        grid.addWidget(self.calculateButton, 10, 0, 1, 2)"""

        # Set the layout for the widget
        self.setLayout(grid)

    def calculateTotal(self):
        # Get quantity and unit price
        try:
            quantity = int(self.quantityInput.text())
            unit_price = float(self.unitPriceInput.text())
            total_price = quantity * unit_price

            # Display total price
            self.totalPriceDisplay.setText(f'{total_price:.2f}')

            # Display bill total (could include tax, discount, etc. if needed)
            self.billTotalDisplay.setText(f'{total_price:.2f}')
        except ValueError:
            # Handle case where inputs are empty or invalid
            QtWidgets.QMessageBox.warning(self, 'Input Error', 'Please enter valid Quantity and Unit Price.')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = BillingForm()
    window.setWindowTitle('Billing Form')
    window.resize(1841, 1071)  # Set window size to 1841x1071
    window.show()
    sys.exit(app.exec_())
