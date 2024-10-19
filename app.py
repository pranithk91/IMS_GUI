import sys
from PyQt5 import QtWidgets, QtCore
from test import BillingForm
from DeliveryBillDetails import deliveryBillsUi
from PharmacyEntry import PharmacyWindow

class DeliveryWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel("Delivery Section")
        layout.addWidget(label)
        self.setLayout(layout)

class OPWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel("OP Section")
        layout.addWidget(label)
        self.setLayout(layout)

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    


    def initUI(self):
        # Create a horizontal layout
        hbox = QtWidgets.QHBoxLayout(self)

        # Create a vertical layout for the buttons (left-side menu)
        vbox = QtWidgets.QVBoxLayout()

        # Create the buttons for the menu
        self.pharmacyButton = QtWidgets.QPushButton("Pharmacy")
        self.deliveryButton = QtWidgets.QPushButton("Delivery")
        self.opButton = QtWidgets.QPushButton("OP")

        vbox.addWidget(self.pharmacyButton)
        vbox.addWidget(self.deliveryButton)
        vbox.addWidget(self.opButton)

        # Add stretch to push the buttons to the top of the menu
        vbox.addStretch()

        # Create a stacked widget to hold different pages
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        
        # Create instances of each window
        self.pharmacyWindow = PharmacyWindow()
        self.deliveryWindow = DeliveryWindow()
        self.opWindow = OPWindow()

        # Add the windows to the stacked widget
        self.stackedWidget.addWidget(self.pharmacyWindow)  # Index 0
        self.stackedWidget.addWidget(self.deliveryWindow)   # Index 1
        self.stackedWidget.addWidget(self.opWindow)         # Index 2

        # Connect the buttons to the respective window pages
        self.pharmacyButton.clicked.connect(self.showPharmacy)
        self.deliveryButton.clicked.connect(self.showDelivery)
        self.opButton.clicked.connect(self.showOP)

        # Add the left-side menu and the stacked widget to the horizontal layout
        hbox.addLayout(vbox)             # Left-side menu (buttons)
        hbox.addWidget(self.stackedWidget)  # Main content (stacked windows)

        # Set the default window to be the Pharmacy window
        self.stackedWidget.setCurrentIndex(0)

    def showPharmacy(self):
        self.stackedWidget.setCurrentIndex(0)

    def showDelivery(self):
        self.stackedWidget.setCurrentIndex(1)

    def showOP(self):
        pass
        #self.stackedWidget.setCurrentIndex(2)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.setWindowTitle('Menu Navigation Example')
    mainWin.resize(800, 600)
    mainWin.show()
    sys.exit(app.exec_())