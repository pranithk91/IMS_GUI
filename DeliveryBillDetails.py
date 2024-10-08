from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from database import fetchInvoiceNumbers, fetchMedicineNames, insertBillItemsData, fetchMagencyNames, insertDeliveryBillData

class CustomTextEdit(QtWidgets.QTextEdit):
    focus_out_signal = QtCore.pyqtSignal()  # Custom signal for focus out

    def focusOutEvent(self, event):
        # Emit custom signal when the focus is lost
        self.focus_out_signal.emit()
        super(CustomTextEdit, self).focusOutEvent(event)
    


class Ui_mainWindow(object):

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1841, 1071)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        medicineData, medNames = fetchMedicineNames()
        invNums = fetchInvoiceNumbers()
        mAgencyNames,mAgencyData = fetchMagencyNames()

        """def focusOutEvent(self, event):
            # Emit custom signal when the focus is lost
            QtCore.pyqtSignal().focus_out_signal.emit()
            super(QtWidgets.QTextEdit, self).focusOutEvent(event)"""

        def showInvoiceWarning():
            invNum = self.invNumEdit.toPlainText()
            if invNum in invNums:
                self.invWarningLabel.setText("Invoice already in the system!!!")
            else:
                self.invWarningLabel.setText("")

        def show_error_message(self, message):
            # Display error message to the user in a message box
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setText(f"An error occurred: {message}")
            error_dialog.setWindowTitle("Error")
            error_dialog.exec_()

        def updateMedDets():
            
            medName = self.medNameCombobox.currentText()
            if medName:
                medDets = medicineData[(medicineData['MName'] == medName)]
                print(medDets)
                self.currQtyLabel.setText("Current Qty: "+ str(medDets.iloc[0]['CurrentStock']))
                self.mfrLabel.setText("Mfr: " + str(medDets.iloc[0]['MCompany']))            
                self.typeLabel.setText( "Type: "+str(medDets.iloc[0]['MType']))
                self.oldMRPLabel.setText( "MRP: "+str(medDets.iloc[0]['MRP']))
                self.gstLabel.setText( "GST: "+str(medDets.iloc[0]['GST']))
                self.weightLabel.setText( "Weight: "+str(medDets.iloc[0]['Weight']))
                self.offerLabel.setText( "Offer: "+str(medDets.iloc[0]['Offer1'])+'+'+str(medDets.iloc[0]['Offer2']))
                self.hsnLabel.setText( "HSN: "+str(medDets.iloc[0]['HSN']))
            

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
        robotoFont.setPointSize(12)

        
        self.label = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.label.setGeometry(QtCore.QRect(10, 22, 541, 51))
        Segoefont = QtGui.QFont()
        Segoefont.setFamily("Segoe UI Black")
        Segoefont.setPointSize(24)
        Segoefont.setBold(True)
        Segoefont.setWeight(75)
        self.label.setFont(Segoefont)
        self.label.setObjectName("label")


        today = QtCore.QDate.currentDate()
        #Invoice Details
        self.invDateLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.invDateLabel.setGeometry(QtCore.QRect(10, 70, 181, 41))        
        self.invDateLabel.setFont(robotoFontBold)
        self.invDateLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.invDateLabel.setObjectName("invDateLabel")

        self.invDateSelect = QtWidgets.QDateEdit(self.deliveryBillsFrame,calendarPopup=True)
        self.invDateSelect.setGeometry(QtCore.QRect(10, 110, 181, 51))
        self.invDateSelect.setFont(robotoFont)
        self.invDateSelect.setDate(today)
        self.invDateSelect.setStyleSheet("""QCalendarWidget QAbstractItemView:enabled {
                background-color: #f0f0f0;  /* Background color of the dates */
                color: black;                /* Text color of the dates */
                selection-background-color: #0078d7;  /* Selected date background */
                selection-color: white;      /* Selected date text color */
            }
            QCalendarWidget QToolButton {
                color: black;                /* Color of the month/year header buttons */
                background-color: #f0f0f0;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #0078d7;   /* Hover color of the month/year buttons */
                color: white;
            }
            QCalendarWidget QMenu {
                background-color: #f0f0f0;   /* Background color of the year/month dropdown */
                color: black;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: #d3d3d3;   /* Background color of the navigation bar */
            }
            QCalendarWidget QSpinBox {
                color: black;                /* Year spinbox text color */
                background-color: #f0f0f0;   /* Year spinbox background */
            }""")
        self.invDateSelect.setObjectName("invDateSelect")

        self.invWarningLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.invWarningLabel.setGeometry(QtCore.QRect(500, 110, 301, 41))
        self.invWarningLabel.setFont(robotoFontBold)
        self.invWarningLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.invWarningLabel.setObjectName("invNoLabel")

        self.invNoLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.invNoLabel.setGeometry(QtCore.QRect(810, 70, 181, 41))        
        self.invNoLabel.setFont(robotoFontBold)
        self.invNoLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.invNoLabel.setObjectName("invNoLabel")

        self.invNumEdit = CustomTextEdit(self.deliveryBillsFrame)
        self.invNumEdit.setGeometry(QtCore.QRect(810, 110, 181, 51))
        self.invNumEdit.setFont(robotoFont)
        self.invNumEdit.setTabChangesFocus(True)
        self.invNumEdit.setObjectName("invNumEdit")
        self.invNumEdit.focus_out_signal.connect(showInvoiceWarning)
   

        self.medAgencyLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.medAgencyLabel.setGeometry(QtCore.QRect(10, 190, 181, 41))   
        self.medAgencyLabel.setFont(robotoFontBold)
        self.medAgencyLabel.setStyleSheet("QComboBox {font-size: 16px; background-color: #FBFBFA;} QComboBox QAbstractItemView {font-size: 14px;}")
        self.medAgencyLabel.setObjectName("medAgencyLabel")

        self.medAgencyCombobox = QtWidgets.QComboBox(self.deliveryBillsFrame)
        self.medAgencyCombobox.setEnabled(True)
        self.medAgencyCombobox.setEditable(True)
        self.medAgencyCombobox.setGeometry(QtCore.QRect(10, 230, 411, 51))
        self.medAgencyCombobox.setFont(robotoFont)
        self.medAgencyCombobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.medAgencyCombobox.setPlaceholderText('Select')
        self.medAgencyCombobox.setObjectName("medAgencyCombobox")
        self.medAgencyCombobox.addItems(mAgencyNames)
        medAgencyCompleter = QtWidgets.QCompleter(mAgencyNames, self.medAgencyCombobox)
        medAgencyCompleter.setCaseSensitivity(QtCore.Qt.CaseInsensitive)  # Case-insensitive matching
        medAgencyCompleter.setFilterMode(QtCore.Qt.MatchStartsWith)  # Show suggestions if input matches anywhere in the string
        self.medAgencyCombobox.setCompleter(medAgencyCompleter)


        self.billAmountLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.billAmountLabel.setGeometry(QtCore.QRect(470, 190, 111, 41))
        self.billAmountLabel.setFont(robotoFontBold)
        self.billAmountLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.billAmountLabel.setObjectName("billAmountLabel")

        self.billAmountInput = QtWidgets.QTextEdit(self.deliveryBillsFrame)
        self.billAmountInput.setGeometry(QtCore.QRect(470, 230, 161, 51))
        self.billAmountInput.setFont(robotoFont)
        self.billAmountInput.setTabChangesFocus(True)
        self.billAmountInput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.billAmountInput.setObjectName("billAmountInput")

        self.discountInbillLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.discountInbillLabel.setGeometry(QtCore.QRect(770, 190, 101, 41))        
        self.discountInbillLabel.setFont(robotoFontBold)
        self.discountInbillLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.discountInbillLabel.setObjectName("discountInFileLabel")

        self.discountCheckBox = QtWidgets.QCheckBox(self.deliveryBillsFrame)
        self.discountCheckBox.setGeometry(QtCore.QRect(800, 230, 31, 41))
        self.discountCheckBox.setText("")
        self.discountCheckBox.setObjectName("discountCheckBox")
        self.discountCheckBox.setStyleSheet("""QCheckBox::indicator {
                                                width: 25px;
                                                height: 25px;
                                                background-color: #FBFBFA;
                                                
                                                border-style: solid;
                                                border-width: 2px;
                                                border-color: black black black black;
                                            }
                                            QCheckBox::indicator:checked {
                                                background-color: #17784E;
                                            }
                                            """)

        self.discountLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.discountLabel.setGeometry(QtCore.QRect(680, 190, 81, 41))        
        self.discountLabel.setFont(robotoFontBold)
        self.discountLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.discountLabel.setObjectName("discountLabel")

        self.discountInput = QtWidgets.QTextEdit(self.deliveryBillsFrame)
        self.discountInput.setGeometry(QtCore.QRect(680, 230, 81, 51))
        self.discountInput.setFont(robotoFont)
        self.discountInput.setTabChangesFocus(True)
        self.discountInput.setObjectName("discountInput")

        self.billInFileLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.billInFileLabel.setGeometry(QtCore.QRect(890, 190, 101, 41))        
        self.billInFileLabel.setFont(robotoFontBold)
        self.billInFileLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.billInFileLabel.setObjectName("billInFileLabel")
        

        self.billInFileCheckBox = QtWidgets.QCheckBox(self.deliveryBillsFrame)
        self.billInFileCheckBox.setGeometry(QtCore.QRect(920, 230, 31, 41))
        #self.billInFileCheckBox.setFont(robotoFont)
        self.billInFileCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.billInFileCheckBox.setObjectName("billInFileCheckbox")
        self.billInFileCheckBox.setStyleSheet("""QCheckBox::indicator {
                                                width: 25px;
                                                height: 25px;
                                                background-color: #FBFBFA;
                                                
                                                border-style: solid;
                                                border-width: 2px;
                                                border-color: black black black black;
                                            }
                                            QCheckBox::indicator:checked {
                                                background-color: #17784E;
                                            }
                                            """)
        

        #Bill Items Addition 

        self.deliveryDateLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.deliveryDateLabel.setGeometry(QtCore.QRect(10, 340, 181, 41))        
        self.deliveryDateLabel.setFont(robotoFontBold)
        self.deliveryDateLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.deliveryDateLabel.setObjectName("deliveryDateLabel")

        self.deliveryDateSelect = QtWidgets.QDateEdit(self.deliveryBillsFrame,calendarPopup=True)
        self.deliveryDateSelect.setGeometry(QtCore.QRect(10, 380, 181, 51))
        self.deliveryDateSelect.setFont(robotoFont)
        self.deliveryDateSelect.setDate(today)
        self.deliveryDateSelect.setStyleSheet("""QCalendarWidget QAbstractItemView:enabled {
                background-color: #f0f0f0;  /* Background color of the dates */
                color: black;                /* Text color of the dates */
                selection-background-color: #0078d7;  /* Selected date background */
                selection-color: white;      /* Selected date text color */
            }
            QCalendarWidget QToolButton {
                color: black;                /* Color of the month/year header buttons */
                background-color: #f0f0f0;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #0078d7;   /* Hover color of the month/year buttons */
                color: white;
            }
            QCalendarWidget QMenu {
                background-color: #f0f0f0;   /* Background color of the year/month dropdown */
                color: black;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: #d3d3d3;   /* Background color of the navigation bar */
            }
            QCalendarWidget QSpinBox {
                color: black;                /* Year spinbox text color */
                background-color: #f0f0f0;   /* Year spinbox background */
            }""")
        self.deliveryDateSelect.setObjectName("deliveryDateSelect")

        self.medNameLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.medNameLabel.setGeometry(QtCore.QRect(240, 340, 181, 41))        
        self.medNameLabel.setFont(robotoFontBold)
        self.medNameLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.medNameLabel.setObjectName("medNameLabel")   

        self.medNameCombobox = QtWidgets.QComboBox(self.deliveryBillsFrame)
        self.medNameCombobox.setEnabled(True)
        self.medNameCombobox.setEditable(True)
        self.medNameCombobox.setPlaceholderText('Select')
        self.medNameCombobox.setGeometry(QtCore.QRect(240, 380, 181, 51))
        self.medNameCombobox.setFont(robotoFont)
        self.medNameCombobox.setStyleSheet("QComboBox {font-size: 16px; background-color: #FBFBFA;} QComboBox QAbstractItemView {font-size: 14px;}")
        self.medNameCombobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))        
        self.medNameCombobox.setObjectName("medNameCombobox")
        self.medNameCombobox.addItems(medNames)
        self.medNameCombobox.currentIndexChanged.connect(updateMedDets)        
        medNameCompleter = QtWidgets.QCompleter(medNames, self.medNameCombobox)
        medNameCompleter.setCaseSensitivity(QtCore.Qt.CaseInsensitive)  # Case-insensitive matching
        medNameCompleter.setFilterMode(QtCore.Qt.MatchStartsWith)  # Show suggestions if input matches anywhere in the string
        self.medNameCombobox.setCompleter(medNameCompleter)

        self.mrpLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.mrpLabel.setGeometry(QtCore.QRect(450, 340, 61, 41))        
        self.mrpLabel.setFont(robotoFontBold)
        self.mrpLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.mrpLabel.setObjectName("mrpLabel")

        self.mrpInput = QtWidgets.QTextEdit(self.deliveryBillsFrame)
        self.mrpInput.setGeometry(QtCore.QRect(450, 380, 71, 51))
        self.mrpInput.setFont(robotoFont)
        self.mrpInput.setTabChangesFocus(True)
        self.mrpInput.setObjectName("mrpInput")        
              
        self.qtyLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.qtyLabel.setGeometry(QtCore.QRect(550, 340, 61, 41))        
        self.qtyLabel.setFont(robotoFontBold)
        self.qtyLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.qtyLabel.setObjectName("qtyLabel")

        self.qtyInput = QtWidgets.QTextEdit(self.deliveryBillsFrame)
        self.qtyInput.setGeometry(QtCore.QRect(550, 380, 71, 51))
        self.qtyInput.setFont(robotoFont)
        self.qtyInput.setTabChangesFocus(True)
        self.qtyInput.setObjectName("qtyInput")

        self.batchNumLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.batchNumLabel.setGeometry(QtCore.QRect(650, 340, 141, 41))        
        self.batchNumLabel.setFont(robotoFontBold)
        self.batchNumLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.batchNumLabel.setObjectName("batchNumLabel")        

        self.batchNumInput = QtWidgets.QTextEdit(self.deliveryBillsFrame)
        self.batchNumInput.setGeometry(QtCore.QRect(650, 380, 151, 51))
        self.batchNumInput.setFont(robotoFont)
        self.batchNumInput.setTabChangesFocus(True)
        self.batchNumInput.setObjectName("batchNumInput") 

        self.expDateLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.expDateLabel.setGeometry(QtCore.QRect(840, 340, 121, 41))        
        self.expDateLabel.setFont(robotoFontBold)
        self.expDateLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.expDateLabel.setObjectName("expDateLabel")

        self.ExpDateInput = QtWidgets.QTextEdit(self.deliveryBillsFrame)
        self.ExpDateInput.setGeometry(QtCore.QRect(840, 380, 151, 51))
        self.ExpDateInput.setFont(robotoFont)
        self.ExpDateInput.setTabChangesFocus(True)
        self.ExpDateInput.setObjectName("ExpDateInput")      

        #Current Medicine Details
        self.currQtyLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.currQtyLabel.setGeometry(QtCore.QRect(0, 450, 121, 41))

        self.currQtyLabel.setFont(robotoFont)
        self.currQtyLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; ")
        self.currQtyLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.currQtyLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.currQtyLabel.setLineWidth(1)
        self.currQtyLabel.setMidLineWidth(3)
        self.currQtyLabel.setTextFormat(QtCore.Qt.AutoText)
        self.currQtyLabel.setObjectName("currQtyLabel")

        self.mfrLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.mfrLabel.setGeometry(QtCore.QRect(150, 450, 121, 41))
        self.mfrLabel.setFont(robotoFont)
        self.mfrLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; ")
        self.mfrLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mfrLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mfrLabel.setObjectName("mfrLabel")

        self.typeLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.typeLabel.setGeometry(QtCore.QRect(300, 450, 121, 41))
        self.typeLabel.setFont(robotoFont)
        self.typeLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; ")
        self.typeLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.typeLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.typeLabel.setObjectName("typeLabel")

        self.oldMRPLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.oldMRPLabel.setGeometry(QtCore.QRect(440, 450, 81, 41))
        self.oldMRPLabel.setFont(robotoFont)
        self.oldMRPLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; ")
        self.oldMRPLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.oldMRPLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.oldMRPLabel.setObjectName("oldMRPLabel")

        self.gstLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.gstLabel.setGeometry(QtCore.QRect(690, 450, 71, 41))
        self.gstLabel.setFont(robotoFont)
        self.gstLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; ")
        self.gstLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gstLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gstLabel.setObjectName("gstLabel")

        self.weightLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.weightLabel.setGeometry(QtCore.QRect(780, 450, 101, 41))
        self.weightLabel.setFont(robotoFont)
        self.weightLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; ")
        self.weightLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.weightLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.weightLabel.setObjectName("weightLabel")

        self.offerLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.offerLabel.setGeometry(QtCore.QRect(900, 450, 91, 41))
        self.offerLabel.setFont(robotoFont)
        self.offerLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; ")
        self.offerLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.offerLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.offerLabel.setObjectName("offerLabel")

        self.hsnLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.hsnLabel.setGeometry(QtCore.QRect(540, 450, 131, 41))
        self.hsnLabel.setFont(robotoFont)
        self.hsnLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; ")
        self.hsnLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hsnLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hsnLabel.setObjectName("hsnLabel")

        self.saleableStockLabel = QtWidgets.QLabel(self.deliveryBillsFrame)
        self.saleableStockLabel.setGeometry(QtCore.QRect(210, 520, 151, 41))        
        self.saleableStockLabel.setFont(robotoFontBold)
        self.saleableStockLabel.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        self.saleableStockLabel.setObjectName("discountInFileLabel")

        self.saleableStockCheckBox = QtWidgets.QCheckBox(self.deliveryBillsFrame)
        self.saleableStockCheckBox.setGeometry(QtCore.QRect(370, 523, 31, 41))
        self.saleableStockCheckBox.setText("")
        self.saleableStockCheckBox.setObjectName("discountCheckBox")
        self.saleableStockCheckBox.setStyleSheet("""QCheckBox::indicator {
                                                width: 20px;
                                                height: 20px;
                                                background-color: #FBFBFA;
                                                
                                                border-style: solid;
                                                border-width: 2px;
                                                border-color: black black black black;
                                            }
                                            QCheckBox::indicator:checked {
                                                background-color: #17784E;
                                            }
                                            """)

        self.billItemList = []

        def onAddItemsButton():
            #billItemList 
            try:
                medName = self.medNameCombobox.currentText()
                medDets = medicineData[(medicineData['MName'] == medName)]
                newPrice = self.mrpInput.toPlainText()
                quantity = self.qtyInput.toPlainText()
                batchNum = self.batchNumInput.toPlainText()
                expDate = self.ExpDateInput.toPlainText()
                
                
            
                if not medName or not quantity or not newPrice:
                    QMessageBox.warning(self, "Input Error", "Missing Fields")
                    return
                currPrice = medDets.iloc[0]['MRP']
                priceChange = int(newPrice)-int(currPrice)
                newRow = [medName,newPrice,quantity,batchNum, expDate, priceChange]
                self.billItemList.append(newRow)

                rowCount = self.billItemsTable.rowCount()
                self.billItemsTable.insertRow(rowCount)
                
                for index, col in enumerate(newRow):
                    self.billItemsTable.setItem(rowCount, index, QtWidgets.QTableWidgetItem(str(col)))
                
                self.medNameCombobox.setCurrentIndex(-1)
                self.mrpInput.clear()
                self.qtyInput.clear()
                self.batchNumInput.clear()
                self.ExpDateInput.clear()

                print(self.billItemList)
            except Exception as e:
                show_error_message(self.deliveryBillsFrame,message=str(e))

        def onSubmitBillButton():
            if len(self.billItemList) > 0: 
                qdateDeliveryDate = self.deliveryDateSelect.date()
                deliveryDate = qdateDeliveryDate.toString("yyyy-MM-dd")
                invoiceNumber = self.invNumEdit.toPlainText()
                qdateInvoiceDate = self.invDateSelect.date()
                invoiceDate = qdateInvoiceDate.toString("yyyy-MM-dd")
                mAgencyName = self.medAgencyCombobox.currentText()
                billAmount = self.billAmountInput.toPlainText()
                discountinBill = self.discountCheckBox.isChecked()
                discountPercent = self.discountInput.toPlainText()
                billInFile = self.billInFileCheckBox.isChecked()
                saleableStock = self.saleableStockCheckBox.isChecked()

                print(invoiceDate, invoiceNumber, mAgencyName, billAmount, discountinBill, discountPercent, billInFile, saleableStock)
                #invDate, invNumber, mAgency, billAmount, discountInBill, discountPercent, billInFile
                insertDeliveryBillData(invoiceDate, invoiceNumber, mAgencyName, billAmount, discountinBill, discountPercent, billInFile,saleableStock)

                for row in self.billItemList:
                    print(deliveryDate, row[0], row[2], row[1], row[5], row[3], row[4], invoiceNumber)
                    insertBillItemsData(deliveryDate, row[0], row[2], row[1], row[5], row[3], row[4], invoiceNumber,saleableStock)
                self.billItemList = []
                rowCount = self.billItemsTable.rowCount()
                for r in range(rowCount):
                    self.billItemsTable.removeRow(r)
            else: 
                QMessageBox.warning("Input some data from a bill")
                return

        #Add Items Button
        self.addItemButton = QtWidgets.QPushButton(self.deliveryBillsFrame)
        self.addItemButton.setGeometry(QtCore.QRect(430, 510, 141, 51))
        self.addItemButton.setFont(robotoFontBold)
        self.addItemButton.setAutoFillBackground(False)
        self.addItemButton.setStyleSheet("color: #17784E; background-color: #FBFBFA; ")
        self.addItemButton.setFlat(False)
        self.addItemButton.clicked.connect(onAddItemsButton)
        self.addItemButton.setObjectName("addItemButton")

        def selectRow(row):
            rowData = []
            for i in range(6):
                rowData.append(self.billItemsTable.item(row, i).text())

            medName = self.medNameCombobox.findText(rowData[0])     
            self.medNameCombobox.setCurrentIndex(medName)
            #medDets = medicineData[(medicineData['MName'] == medName)]
            self.mrpInput.setText(rowData[1])
            self.qtyInput.setText(rowData[2])
            self.batchNumInput.setText(rowData[3])
            self.ExpDateInput.setText(rowData[4])
            medDets = medicineData[(medicineData['MName'] == rowData[0])]
            updateMedDets()
            self.billItemsTable.removeRow(row)

        #Bill Items Table
        self.billItemsTable = QtWidgets.QTableWidget(self.deliveryBillsFrame)
        self.billItemsTable.setGeometry(QtCore.QRect(10, 580, 981, 311))
        self.billItemsTable.setObjectName("billItemsTable")
        self.billItemsTable.setColumnCount(6)
        self.billItemsTable.setFont(robotoFont)
        self.billItemsTable.setHorizontalHeaderLabels(['Name', 'New Price', 'Qty', 'Batch No', 'Exp Date', 'Price Change' ])
        self.billItemsTable.setRowCount(0)
        header = self.billItemsTable.horizontalHeader()
        header.setFont(robotoFont)
        header.setStyleSheet("color: #17784E; background-color: #FBFBFA; font-weight: bold;")
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.billItemsTable.cellDoubleClicked.connect(selectRow)

        #Bill Submit Button
        self.billSubmitButton = QtWidgets.QPushButton(self.deliveryBillsFrame)
        self.billSubmitButton.setGeometry(QtCore.QRect(430, 910, 141, 51))        
        self.billSubmitButton.setFont(robotoFontBold)
        self.billSubmitButton.clicked.connect(onSubmitBillButton)
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
        self.deliveryBillsFrame.setTabOrder(self.invDateSelect, self.invNumEdit)
        self.deliveryBillsFrame.setTabOrder(self.invNumEdit, self.medAgencyCombobox)
        self.deliveryBillsFrame.setTabOrder(self.medAgencyCombobox, self.billAmountInput)
        self.deliveryBillsFrame.setTabOrder(self.billAmountInput, self.discountInput)
        self.deliveryBillsFrame.setTabOrder(self.discountInput, self.discountCheckBox)
        self.deliveryBillsFrame.setTabOrder(self.discountCheckBox, self.billInFileCheckBox)
        self.deliveryBillsFrame.setTabOrder(self.billInFileCheckBox, self.deliveryDateSelect)
        self.deliveryBillsFrame.setTabOrder(self.deliveryDateSelect, self.medNameCombobox)
        self.deliveryBillsFrame.setTabOrder(self.medNameCombobox, self.mrpInput)
        self.deliveryBillsFrame.setTabOrder(self.mrpInput, self.qtyInput)
        self.deliveryBillsFrame.setTabOrder(self.qtyInput, self.batchNumInput)
        self.deliveryBillsFrame.setTabOrder(self.batchNumInput, self.ExpDateInput)
        self.deliveryBillsFrame.setTabOrder(self.ExpDateInput, self.saleableStockCheckBox)
        self.deliveryBillsFrame.setTabOrder(self.saleableStockCheckBox, self.addItemButton)
        self.deliveryBillsFrame.setTabOrder(self.addItemButton, self.billSubmitButton)
        self.deliveryBillsFrame.setTabOrder(self.billSubmitButton, self.billItemsTable)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Dr Preethi\'s Skin Hair and Laser Clinic"))
        self.currQtyLabel.setText(_translate("mainWindow", "Current Qty:"))
        self.addItemButton.setText(_translate("mainWindow", "Add Item"))
        self.label.setStyleSheet(_translate("mainWindow", "color: #17784E; background-color: #FBFBFA; font-weight: bold;"))
        self.label.setText(_translate("mainWindow", "Delivery Bill Details"))
        #self.billInFileCombobox.setPlaceholderText(_translate("mainWindow", "Choose from the list"))
        self.billItemsTable.setStyleSheet(_translate("mainWindow", "color: #17784E; background-color: #FBFBFA; font-weight: bold;"))
        self.medNameLabel.setText(_translate("mainWindow", "Medicine Name"))
        self.billSubmitButton.setText(_translate("mainWindow", "Submit"))
        self.mrpLabel.setText(_translate("mainWindow", "MRP"))
        self.qtyLabel.setText(_translate("mainWindow", "Qty"))
        self.deliveryDateLabel.setText(_translate("mainWindow", "Delivery Date"))
        self.medAgencyLabel.setText(_translate("mainWindow", "Medical Agency"))
        self.medAgencyCombobox.setPlaceholderText(_translate("mainWindow", "Choose from the list"))
        self.invDateLabel.setText(_translate("mainWindow", "Invoice Date"))
        self.billInFileLabel.setText(_translate("mainWindow", "Bill In File"))
        self.discountInbillLabel.setText(_translate("mainWindow", "Disc In Bill"))
        self.saleableStockLabel.setText(_translate("mainWindow", "Saleable Stock"))
        self.invNoLabel.setText(_translate("mainWindow", "Invoice Number"))
        self.expDateLabel.setText(_translate("mainWindow", "Expiry Date"))
        self.billAmountLabel.setText(_translate("mainWindow", "Bill Amount"))
        self.discountLabel.setText(_translate("mainWindow", "Discount"))
        self.batchNumLabel.setText(_translate("mainWindow", "Batch Number"))
        self.medNameCombobox.setPlaceholderText(_translate("mainWindow", "Choose from the list"))
        self.mfrLabel.setText(_translate("mainWindow", "Mfr:"))
        self.typeLabel.setText(_translate("mainWindow", "Type:"))
        self.oldMRPLabel.setText(_translate("mainWindow", "MRP:"))
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
