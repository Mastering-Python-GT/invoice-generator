import sys
from PySide6.QtGui import QPixmap, QAction, QCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMenu
from invoice_ui import Ui_MainWindow
from datetime import date
from creteReport import SalesInvoice
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
import os
import shutil

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.m_document = None
        self.logoFile = None
        self.n_invoice.setText("1-2024")
        d_ate = date.today()
        self.today = d_ate.strftime("%d-%m-%Y")
        self.date.setText(self.today)
        

        self.companyName.textChanged.connect(self.company_label)
        self.email.textChanged.connect(self.email_label)
        self.phone.textChanged.connect(self.phone_label)
        self.companyAddress.textChanged.connect(self.companyAddress_label)

        self.client.textChanged.connect(self.client_label)
        self.address_client.textChanged.connect(self.addressClient_label)

        self.quantity.textChanged.connect(self.quantity_label)
        self.price.textChanged.connect(self.price_label)

        self.total.textChanged.connect(self.totalChanged)
        self.discount.textChanged.connect(self.discountChanged)
        self.payment.textChanged.connect(self.paymentChanged)
        self.rest.textChanged.connect(self.restChanged)

        self.goInvoice.clicked.connect(self.go_invoice)
        self.loadLogo.clicked.connect(self.addLogo)
        self.addProduct.clicked.connect(self.add_product)
        self.discount.textChanged.connect(self.discount_change)
        self.payment.textChanged.connect(self.payment_change)
        self.printSaveInvoice.clicked.connect(self.showMenu)

        self.pushButton.clicked.connect(self.cancel)   
        self.newInvoice.clicked.connect(self.new_nvoice)

        self.showMaximized()

    def go_invoice(self):
        self.stackedWidget.setCurrentIndex(1)

    def add_product(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        a = self.product.currentText().split("-", 1)[1]
        b = self.product.currentText()
        c = self.quantity.text()
        d = self.price.text()
        e = int(c) * int(d)
        e = '{:,}'.format(e)
        self.table.setItem(row, 0, QTableWidgetItem(a))
        self.table.setItem(row, 1, QTableWidgetItem(b))
        self.table.setItem(row, 2, QTableWidgetItem(c))
        self.table.setItem(row, 3, QTableWidgetItem(d))
        self.table.setItem(row, 4, QTableWidgetItem(e))

        if self.total.text() == "":
            self.total.setText(e)
        else:
            k = int(self.total.text().replace(",", "")) + \
                int(e.replace(",", ""))
            k = '{:,}'.format(k)
            self.total.setText(k)

    def discount_change(self):
        if self.discount.text().__contains__(","):
            e = self.discount.text().replace(",", "")
            e = '{:,}'.format(int(e))
        else:
            e = int(self.discount.text())
            e = '{:,}'.format(e)

        self.discount.setText(str(e))

    def payment_change(self):
        if self.payment.text().__contains__(","):
            e = self.payment.text().replace(",", "")
            e = '{:,}'.format(int(e))
        else:
            e = int(self.payment.text())
            e = '{:,}'.format(e)

        self.payment.setText(str(e))

    def showMenu(self):

        context = QMenu()

        button_action1 = QAction("Save Invoice")
        button_action1.triggered.connect(self.saveInvoice)
        context.addAction(button_action1)

        button_action2 = QAction("Print Invoice")
        button_action2.triggered.connect(self.printInvoice)
        context.addAction(button_action2)

        context.exec(QCursor.pos())

    def new_nvoice(self):

        for i in range(self.table.rowCount()):
            self.table.removeRow(0)

        self.client.clear()
        self.address_client.clear()
        self.quantity.clear()
        self.price.clear()
        self.total.clear()
        self.discount.clear()
        self.payment.clear()
        self.rest.clear()

        k = self.n_invoice.text()
        k = int(k.split("-", 1)[0]) + 1
        k = str(k)+"-"+str(date.today().year)
        self.n_invoice.setText(k)

    def createInvoice(self):
        SalesInvoice(self.companyName.text(), self.email.text(), self.phone.text(), self.companyAddress.toPlainText().strip(), self.table, self.logoFile, self.total.text(
        ), self.discount.text(), self.payment.text(), self.rest.text(), self.client.text(), self.address_client.text(), self.n_invoice.text())
        
    def saveInvoice(self):

        self.createInvoice()
        file = self.n_invoice.text()+"_"+self.client.text()+".pdf"
        shutil.copy(f'{file}', f'./saved_Invoices/{file}')
        os.remove(file)


    def cancel(self):
        self.m_document = QPdfDocument()
        self.stackedWidget.setCurrentIndex(1)
        file = self.n_invoice.text()+"_"+self.client.text()+".pdf"
        os.remove(file)


    def printInvoice(self):
        self.createInvoice()
        self.m_document = QPdfDocument()
        self.pdfView.setDocument(self.m_document)
        self.pdfView.setPageMode(QPdfView.PageMode.MultiPage)
        file = self.n_invoice.text()+"_"+self.client.text()+".pdf"
        self.m_document.load(file)
        self.stackedWidget.setCurrentIndex(2)

    def addLogo(self):
        self.logoFile = QFileDialog.getOpenFileName(filter="jpg (*.jpg)")[0]
        pixmap = QPixmap(self.logoFile)
        self.logo.setScaledContents(True)
        self.logo.setPixmap(pixmap)

    def client_label(self):
        if self.client.text() == "":
            self.label_14.setText("")
            self.client.setStyleSheet(
                "focus{border-bottom: 2px solid #7B68EE;}")
        else:
            self.label_14.setText("Client")
            self.client.setStyleSheet("border-bottom: 2px solid #7B68EE")

    def addressClient_label(self):
        if self.address_client.text() == "":
            self.label_15.setText("")
            self.address_client.setStyleSheet(
                "focus{border-bottom: 2px solid #7B68EE;}")
        else:
            self.label_15.setText("Address")
            self.address_client.setStyleSheet(
                "border-bottom: 2px solid #7B68EE")

    def email_label(self):
        if self.email.text() == "":
            self.label_3.setText("")
            self.email.setStyleSheet(
                "focus{border-bottom: 2px solid #7B68EE;}")
        else:
            self.label_3.setText("Email")
            self.email.setStyleSheet("border-bottom: 2px solid #7B68EE")

    def phone_label(self):
        if self.phone.text() == "":
            self.label_2.setText("")
            self.phone.setStyleSheet(
                "focus{border-bottom: 2px solid #7B68EE;}")

        else:
            self.label_2.setText("Phone")
            self.phone.setStyleSheet("border-bottom: 2px solid #7B68EE")

    def companyAddress_label(self):
        if self.companyAddress.toPlainText() == "":
            self.label_4.setText("")
            self.companyAddress.setStyleSheet(
                "focus{border-bottom: 2px solid #7B68EE;}")

        else:
            self.label_4.setText("Address")
            self.companyAddress.setStyleSheet(
                "border-bottom: 2px solid #7B68EE")

    def company_label(self):
        if self.companyName.text() == "":
            self.label.setText("")
            self.companyName.setStyleSheet(
                "focus{border-bottom: 2px solid #7B68EE;}")

        else:
            self.label.setText("Company Name")
            self.companyName.setStyleSheet("border-bottom: 2px solid #7B68EE")

    def quantity_label(self):
        if self.quantity.text() == "":
            self.label_17.setText("")
            self.quantity.setStyleSheet(
                "focus{border-bottom: 2px solid #7B68EE;}")

        else:
            self.label_17.setText("Quantity")
            self.quantity.setStyleSheet("border-bottom: 2px solid #7B68EE")

    def price_label(self):
        if self.price.text() == "":
            self.label_16.setText("")
            self.price.setStyleSheet(
                "focus{border-bottom: 2px solid #7B68EE;}")
        else:
            self.label_16.setText("Price")
            self.price.setStyleSheet("border-bottom: 2px solid #7B68EE")

    def totalChanged(self):
        if self.total.text() == "":
            self.total.setStyleSheet(
                "focus{border-bottom: 2px solid #7B68EE;}")
        else:
            self.total.setStyleSheet("border-bottom: 2px solid #7B68EE")

    def discountChanged(self):
        if self.discount.text() == "":
            self.discount.setStyleSheet(
                "focus{border-bottom: 2px solid #7B68EE;}")
        else:
            self.discount.setStyleSheet("border-bottom: 2px solid #7B68EE")

    def paymentChanged(self):
        if self.payment.text() == "":
            self.payment.setStyleSheet(
                "focus{border-bottom: 2px solid #7B68EE;}")
        else:
            self.payment.setStyleSheet("border-bottom: 2px solid #7B68EE")

    def restChanged(self):
        if self.rest.text() == "":
            self.rest.setStyleSheet("focus{border-bottom: 2px solid #7B68EE;}")
        else:
            self.rest.setStyleSheet("border-bottom: 2px solid #7B68EE")


app = QApplication(sys.argv)

app.setStyle('Fusion')

with open("style.qss", "r") as f:
    _style = f.read()
    app.setStyleSheet(_style)

w = MainWindow()

app.exec()


