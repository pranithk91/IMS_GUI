from PyQt5 import QtCore, QtGui, QtWidgets
from database import fetch_invoice_numbers, fetch_medicine_names, insert_data, fetch_magency_names


class Ui_mainWindow(object):

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1841, 1071)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        medicineData, medNames = fetch_medicine_names()
        invNums = fetch_invoice_numbers()
        mAgencyNames = fetch_magency_names()

        def updateMedDets():
            medName = self.medNameCombobox.currentText()
            medDets = medicineData[(medicineData['MName'] == medName)]
            print(medDets)

        #Delivery Bills Frame
        self.deliveryBillsFrame = QtWidgets.QFrame(self.centralwidget)
        self.deliveryBillsFrame.setGeometry(QtCore.QRect(420, 0, 1001, 1031))
        self.deliveryBillsFrame.setStyleSheet(" background-color:#F6F8F5;")
        self.deliveryBillsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.deliveryBillsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.deliveryBillsFrame.setObjectName("deliveryBillsFrame")

        #Defining Fonts
        robotoFontBold = QtGui.QFont()
        robotoFontBold.setFamily("Roboto")
        robotoFontBold.setPointSize(14)
        robotoFontBold.setBold(True)
        robotoFontBold.setWeight(75)

        robotoFont = QtGui.QFont()
        robotoFont.setFamily("Roboto")
        robotoFont.setPointSize(14)

        
        self.label = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.label.setGeometry(QtCore.QRect(10, 22, 541, 51))
        Segoefont = QtGui.QFont()
        Segoefont.setFamily("Segoe UI Black")
        Segoefont.setPointSize(24)
        Segoefont.setBold(True)
        Segoefont.setWeight(75)
        self.label.setFont(Segoefont)
        self.label.setObjectName("label")



        #Invoice Details
        self.invDateLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.invDateLabel.setGeometry(QtCore.QRect(10, 70, 181, 41))        
        self.invDateLabel.setFont(robotoFontBold)
        self.invDateLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.invDateLabel.setObjectName("invDateLabel")

        self.invDateSelect = QtWidgets.QDateEdit(self.deliveryBillsFrame)
        self.invDateSelect.setGeometry(QtCore.QRect(10, 110, 181, 51))
        self.invDateSelect.setFont(robotoFont)
        self.invDateSelect.setObjectName("invDateSelect")

        self.invNoLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.invNoLabel.setGeometry(QtCore.QRect(810, 70, 181, 41))        
        self.invNoLabel.setFont(robotoFontBold)
        self.invNoLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.invNoLabel.setObjectName("invNoLabel")

        self.invNumEdit = QtWidgets.QTextEdit(self.deliveryBillsFrame)
        self.invNumEdit.setGeometry(QtCore.QRect(810, 110, 181, 51))
        self.invNumEdit.setFont(robotoFont)
        self.invNumEdit.setObjectName("invNumEdit")
   

        self.medAgencyLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.medAgencyLabel.setGeometry(QtCore.QRect(10, 190, 181, 41))   
        self.medAgencyLabel.setFont(robotoFontBold)
        self.medAgencyLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.medAgencyLabel.setObjectName("medAgencyLabel")

        self.medAgencyCombobox = QtWidgets.QComboBox(self.deliveryBillsFrame)
        self.medAgencyCombobox.setEnabled(True)
        self.medAgencyCombobox.setGeometry(QtCore.QRect(10, 230, 411, 51))
        self.medAgencyCombobox.setFont(robotoFont)
        self.medAgencyCombobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.medAgencyCombobox.setEditable(False)
        self.medAgencyCombobox.setObjectName("medAgencyCombobox")
       


        self.billAmountLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.billAmountLabel.setGeometry(QtCore.QRect(470, 190, 101, 41))
        self.billAmountLabel.setFont(robotoFontBold)
        self.billAmountLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.billAmountLabel.setObjectName("billAmountLabel")

        self.billAmountInput = QtWidgets.QTextEdit(self.deliveryBillsFrame)
        self.billAmountInput.setGeometry(QtCore.QRect(470, 230, 161, 51))
        self.billAmountInput.setFont(robotoFont)
        self.billAmountInput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.billAmountInput.setObjectName("billAmountInput")

        self.discountLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.discountLabel.setGeometry(QtCore.QRect(680, 190, 81, 41))        
        self.discountLabel.setFont(robotoFontBold)
        self.discountLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.discountLabel.setObjectName("discountLabel")

        self.discountInput = QtWidgets.QTextEdit(self.deliveryBillsFrame)
        self.discountInput.setGeometry(QtCore.QRect(680, 230, 81, 51))
        self.discountInput.setFont(robotoFont)
        self.discountInput.setObjectName("discountInput")

        self.billInFileLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.billInFileLabel.setGeometry(QtCore.QRect(810, 190, 181, 41))        
        self.billInFileLabel.setFont(robotoFontBold)
        self.billInFileLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.billInFileLabel.setObjectName("billInFileLabel")

        self.billInFileCombobox = QtWidgets.QComboBox(self.deliveryBillsFrame)
        self.billInFileCombobox.setEnabled(True)
        self.billInFileCombobox.setGeometry(QtCore.QRect(810, 230, 181, 51))
        self.billInFileCombobox.setFont(robotoFont)
        self.billInFileCombobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.billInFileCombobox.setEditable(False)
        self.billInFileCombobox.setObjectName("billInFileCombobox")

        #Bill Items Addition 

        self.deliveryDateLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.deliveryDateLabel.setGeometry(QtCore.QRect(10, 340, 181, 41))        
        self.deliveryDateLabel.setFont(robotoFontBold)
        self.deliveryDateLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.deliveryDateLabel.setObjectName("deliveryDateLabel")

        self.deliveryDateSelect = QtWidgets.QDateEdit(self.deliveryBillsFrame)
        self.deliveryDateSelect.setGeometry(QtCore.QRect(10, 380, 181, 51))
        self.deliveryDateSelect.setFont(robotoFont)
        self.deliveryDateSelect.setObjectName("deliveryDateSelect")

        self.medNameLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.medNameLabel.setGeometry(QtCore.QRect(240, 340, 181, 41))        
        self.medNameLabel.setFont(robotoFontBold)
        self.medNameLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.medNameLabel.setObjectName("medNameLabel")   

        self.medNameCombobox = QtWidgets.QComboBox(self.deliveryBillsFrame)
        self.medNameCombobox.setEnabled(True)
        self.medNameCombobox.setEditable(True)
        self.medNameCombobox.setGeometry(QtCore.QRect(240, 380, 181, 51))
        self.medNameCombobox.setFont(robotoFont)
        self.medNameCombobox.setStyleSheet("QComboBox {font-size: 16px; background-color: #FBFBFA;} QComboBox QAbstractItemView {font-size: 14px;}")
        self.medNameCombobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))        
        self.medNameCombobox.setObjectName("medNameCombobox")
        self.medNameCombobox.addItems(medNames)
        self.medNameCombobox.currentIndexChanged.connect(updateMedDets)        
        completer = QtWidgets.QCompleter(medNames, self.medNameCombobox)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)  # Case-insensitive matching
        completer.setFilterMode(QtCore.Qt.MatchStartsWith)  # Show suggestions if input matches anywhere in the string
        #delegate = MyDelegate(self.medNameCombobox)
        #completer.popup().setItemDelegate(delegate)
        self.medNameCombobox.setCompleter(completer)

        
        


        

        self.qtyLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.qtyLabel.setGeometry(QtCore.QRect(470, 340, 91, 41))        
        self.qtyLabel.setFont(robotoFontBold)
        self.qtyLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.qtyLabel.setObjectName("qtyLabel")

        self.qtyInput = QtWidgets.QTextEdit(self.deliveryBillsFrame)
        self.qtyInput.setGeometry(QtCore.QRect(470, 380, 91, 51))
        self.qtyInput.setFont(robotoFont)
        self.qtyInput.setObjectName("qtyInput")

        self.batchNumLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.batchNumLabel.setGeometry(QtCore.QRect(610, 340, 181, 41))        
        self.batchNumLabel.setFont(robotoFontBold)
        self.batchNumLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.batchNumLabel.setObjectName("batchNumLabel")        

        self.batchNumInput = QtWidgets.QTextEdit(self.deliveryBillsFrame)
        self.batchNumInput.setGeometry(QtCore.QRect(610, 380, 151, 51))
        self.batchNumInput.setFont(robotoFont)
        self.batchNumInput.setObjectName("batchNumInput") 

        self.expDateLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.expDateLabel.setGeometry(QtCore.QRect(810, 340, 181, 41))        
        self.expDateLabel.setFont(robotoFontBold)
        self.expDateLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.expDateLabel.setObjectName("expDateLabel")

        self.ExpDateInput = QtWidgets.QTextEdit(self.deliveryBillsFrame)
        self.ExpDateInput.setGeometry(QtCore.QRect(810, 380, 181, 51))
        self.ExpDateInput.setFont(robotoFont)
        self.ExpDateInput.setObjectName("ExpDateInput")      

        #Current Medicine Details
        self.currQtyLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.currQtyLabel.setGeometry(QtCore.QRect(10, 450, 121, 41))

        self.currQtyLabel.setFont(robotoFont)
        self.currQtyLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.currQtyLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.currQtyLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.currQtyLabel.setLineWidth(1)
        self.currQtyLabel.setMidLineWidth(3)
        self.currQtyLabel.setTextFormat(QtCore.Qt.AutoText)
        self.currQtyLabel.setObjectName("currQtyLabel")

        self.mfrLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.mfrLabel.setGeometry(QtCore.QRect(170, 450, 121, 41))
        self.mfrLabel.setFont(robotoFont)
        self.mfrLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.mfrLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mfrLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mfrLabel.setObjectName("mfrLabel")

        self.typeLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.typeLabel.setGeometry(QtCore.QRect(330, 450, 121, 41))
        self.typeLabel.setFont(robotoFont)
        self.typeLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.typeLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.typeLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.typeLabel.setObjectName("typeLabel")

        self.gstLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.gstLabel.setGeometry(QtCore.QRect(660, 450, 71, 41))
        self.gstLabel.setFont(robotoFont)
        self.gstLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.gstLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gstLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gstLabel.setObjectName("gstLabel")

        self.weightLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.weightLabel.setGeometry(QtCore.QRect(760, 450, 101, 41))
        self.weightLabel.setFont(robotoFont)
        self.weightLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.weightLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.weightLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.weightLabel.setObjectName("weightLabel")

        self.offerLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.offerLabel.setGeometry(QtCore.QRect(900, 450, 91, 41))
        self.offerLabel.setFont(robotoFont)
        self.offerLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.offerLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.offerLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.offerLabel.setObjectName("offerLabel")

        self.hsnLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.hsnLabel.setGeometry(QtCore.QRect(480, 450, 151, 41))
        self.hsnLabel.setFont(robotoFont)
        self.hsnLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.hsnLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hsnLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hsnLabel.setObjectName("hsnLabel")


        #Add Items Button
        self.addItemButton = QtWidgets.QPushButton(self.deliveryBillsFrame)
        self.addItemButton.setGeometry(QtCore.QRect(430, 510, 141, 51))
        self.addItemButton.setFont(robotoFontBold)
        self.addItemButton.setAutoFillBackground(False)
        self.addItemButton.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.addItemButton.setFlat(False)
        self.addItemButton.setObjectName("addItemButton")

        #Bill Items Table
        self.billItemstableWidget = QtWidgets.QTableWidget(self.deliveryBillsFrame)
        self.billItemstableWidget.setGeometry(QtCore.QRect(10, 580, 981, 311))
        self.billItemstableWidget.setObjectName("billItemstableWidget")
        self.billItemstableWidget.setColumnCount(0)
        self.billItemstableWidget.setRowCount(0)

        #Bill Submit Button
        self.billSubmitButton = QtWidgets.QPushButton(self.deliveryBillsFrame)
        self.billSubmitButton.setGeometry(QtCore.QRect(430, 910, 141, 51))        
        self.billSubmitButton.setFont(robotoFontBold)
        self.billSubmitButton.setMouseTracking(False)
        self.billSubmitButton.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.billSubmitButton.setObjectName("billSubmitButton")

        #Left Navigation Frame
        self.menuFrame = QtWidgets.QFrame(self.centralwidget)
        self.menuFrame.setGeometry(QtCore.QRect(0, 0, 341, 1031))
        self.menuFrame.setStyleSheet(" background-color: #F6F8F5; font-weight: bold;")
        self.menuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.menuFrame.setObjectName("frame")

        self.pharmacyMenuButton = QtWidgets.QPushButton(self.menuFrame)
        self.pharmacyMenuButton.setGeometry(QtCore.QRect(0, 300, 341, 61))        
        self.pharmacyMenuButton.setFont(robotoFontBold)
        self.pharmacyMenuButton.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.pharmacyMenuButton.setObjectName("pharmacyMenuButton")

        self.proceduresMenuButton = QtWidgets.QPushButton(self.menuFrame)
        self.proceduresMenuButton.setGeometry(QtCore.QRect(0, 390, 341, 61))        
        self.proceduresMenuButton.setFont(robotoFontBold)
        self.proceduresMenuButton.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.proceduresMenuButton.setObjectName("proceduresMenuButton")

        self.opMenuButton = QtWidgets.QPushButton(self.menuFrame)
        self.opMenuButton.setGeometry(QtCore.QRect(0, 210, 341, 61))        
        self.opMenuButton.setFont(robotoFontBold)
        self.opMenuButton.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.opMenuButton.setObjectName("opMenuButton")

        self.medListMenuButton = QtWidgets.QPushButton(self.menuFrame)
        self.medListMenuButton.setGeometry(QtCore.QRect(0, 480, 341, 61))        
        self.medListMenuButton.setFont(robotoFontBold)
        self.medListMenuButton.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.medListMenuButton.setObjectName("medListMenuButton")

        self.summaryMenuButton = QtWidgets.QPushButton(self.menuFrame)
        self.summaryMenuButton.setGeometry(QtCore.QRect(0, 660, 341, 61))        
        self.summaryMenuButton.setFont(robotoFontBold)
        self.summaryMenuButton.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.summaryMenuButton.setObjectName("summaryMenuButton")

        self.medDeliveriesMenuButton = QtWidgets.QPushButton(self.menuFrame)
        self.medDeliveriesMenuButton.setGeometry(QtCore.QRect(0, 570, 341, 61))        
        self.medDeliveriesMenuButton.setFont(robotoFontBold)
        self.medDeliveriesMenuButton.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.medDeliveriesMenuButton.setObjectName("medDeliveriesMenuButton")

        self.consumablesMenuButton = QtWidgets.QPushButton(self.menuFrame)
        self.consumablesMenuButton.setGeometry(QtCore.QRect(0, 750, 341, 61))        
        self.consumablesMenuButton.setFont(robotoFontBold)
        self.consumablesMenuButton.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.consumablesMenuButton.setObjectName("consumablesMenuButton")

        #Design Frame
        self.designFrame = QtWidgets.QFrame(self.centralwidget)
        self.designFrame.setGeometry(QtCore.QRect(340, -1, 81, 1031))
        self.designFrame.setStyleSheet("color: #17784E; background-color: #EEDDDD; font-weight: bold;")
        self.designFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.designFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.designFrame.setObjectName("designFrame")

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1841, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.invDateSelect, self.invNumEdit)
        mainWindow.setTabOrder(self.invNumEdit, self.medAgencyCombobox)
        mainWindow.setTabOrder(self.medAgencyCombobox, self.billAmountInput)
        mainWindow.setTabOrder(self.billAmountInput, self.discountInput)
        mainWindow.setTabOrder(self.discountInput, self.deliveryDateSelect)
        mainWindow.setTabOrder(self.deliveryDateSelect, self.medNameCombobox)
        mainWindow.setTabOrder(self.medNameCombobox, self.qtyInput)
        mainWindow.setTabOrder(self.qtyInput, self.batchNumInput)
        mainWindow.setTabOrder(self.batchNumInput, self.ExpDateInput)
        mainWindow.setTabOrder(self.ExpDateInput, self.addItemButton)
        mainWindow.setTabOrder(self.addItemButton, self.billSubmitButton)
        mainWindow.setTabOrder(self.billSubmitButton, self.billItemstableWidget)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Dr Preethi\'s Skin Hair and Laser Clinic"))
        self.currQtyLabel.setText(_translate("mainWindow", "Current Qty:"))
        self.addItemButton.setText(_translate("mainWindow", "Add Item"))
        self.label.setStyleSheet(_translate("mainWindow", "color: #17784E; background-color: #FBFBFA; font-weight: bold;"))
        self.label.setText(_translate("mainWindow", "Delivery Bill Details"))
        self.billInFileCombobox.setPlaceholderText(_translate("mainWindow", "Choose from the list"))
        self.billItemstableWidget.setStyleSheet(_translate("mainWindow", "color: #17784E; background-color: #FBFBFA; font-weight: bold;"))
        self.medNameLabel.setText(_translate("mainWindow", "Medicine Name"))
        self.billSubmitButton.setText(_translate("mainWindow", "Submit"))
        self.qtyLabel.setText(_translate("mainWindow", "Quantity"))
        self.deliveryDateLabel.setText(_translate("mainWindow", "Delivery Date"))
        self.medAgencyLabel.setText(_translate("mainWindow", "Medical Agency"))
        self.medAgencyCombobox.setPlaceholderText(_translate("mainWindow", "Choose from the list"))
        self.invDateLabel.setText(_translate("mainWindow", "Invoice Date"))
        self.billInFileLabel.setText(_translate("mainWindow", "Bill In File"))
        self.invNoLabel.setText(_translate("mainWindow", "Invoice Number"))
        self.expDateLabel.setText(_translate("mainWindow", "Expiry Date"))
        self.billAmountLabel.setText(_translate("mainWindow", "Bill Amount"))
        self.discountLabel.setText(_translate("mainWindow", "Discount"))
        self.batchNumLabel.setText(_translate("mainWindow", "Batch Number"))
        self.medNameCombobox.setPlaceholderText(_translate("mainWindow", "Choose from the list"))
        self.mfrLabel.setText(_translate("mainWindow", "Mfr:"))
        self.typeLabel.setText(_translate("mainWindow", "Type:"))
        self.gstLabel.setText(_translate("mainWindow", "GST:"))
        self.weightLabel.setText(_translate("mainWindow", "Weight:"))
        self.offerLabel.setText(_translate("mainWindow", "Offer:"))
        self.hsnLabel.setText(_translate("mainWindow", "HSN:"))
        self.pharmacyMenuButton.setText(_translate("mainWindow", "Pharmacy"))
        self.proceduresMenuButton.setText(_translate("mainWindow", "Procedures"))
        self.opMenuButton.setText(_translate("mainWindow", "OP"))
        self.medListMenuButton.setText(_translate("mainWindow", "Medicine List"))
        self.summaryMenuButton.setText(_translate("mainWindow", "Summary"))
        self.medDeliveriesMenuButton.setText(_translate("mainWindow", "Medicine Deliveries"))
        self.consumablesMenuButton.setText(_translate("mainWindow", "Consumables Deliveries"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
