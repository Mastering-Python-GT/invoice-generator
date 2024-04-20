# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'invoice.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1040, 574)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(384, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 0))
        self.widget.setMaximumSize(QSize(250, 16777215))
        self.widget.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_8 = QGridLayout(self.widget)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(57, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.logo = QLabel(self.widget)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(130, 130))
        self.logo.setMaximumSize(QSize(130, 130))
        self.logo.setLayoutDirection(Qt.LeftToRight)
        self.logo.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.logo, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(57, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(250, 30))
        self.label.setMaximumSize(QSize(250, 30))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_8.addWidget(self.label, 1, 0, 1, 3)

        self.companyName = QLineEdit(self.widget)
        self.companyName.setObjectName(u"companyName")
        self.companyName.setMinimumSize(QSize(250, 30))
        self.companyName.setMaximumSize(QSize(250, 30))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(12)
        self.companyName.setFont(font1)

        self.gridLayout_8.addWidget(self.companyName, 2, 0, 1, 3)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(250, 30))
        self.label_2.setMaximumSize(QSize(250, 30))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_8.addWidget(self.label_2, 3, 0, 1, 3)

        self.phone = QLineEdit(self.widget)
        self.phone.setObjectName(u"phone")
        self.phone.setMinimumSize(QSize(250, 30))
        self.phone.setMaximumSize(QSize(250, 30))
        self.phone.setFont(font1)

        self.gridLayout_8.addWidget(self.phone, 4, 0, 1, 3)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(250, 30))
        self.label_3.setMaximumSize(QSize(250, 30))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_8.addWidget(self.label_3, 5, 0, 1, 3)

        self.email = QLineEdit(self.widget)
        self.email.setObjectName(u"email")
        self.email.setMinimumSize(QSize(250, 30))
        self.email.setMaximumSize(QSize(250, 30))
        self.email.setFont(font1)

        self.gridLayout_8.addWidget(self.email, 6, 0, 1, 3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(250, 30))
        self.label_4.setMaximumSize(QSize(250, 30))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_8.addWidget(self.label_4, 7, 0, 1, 3)

        self.companyAddress = QTextEdit(self.widget)
        self.companyAddress.setObjectName(u"companyAddress")
        self.companyAddress.setMinimumSize(QSize(250, 100))
        self.companyAddress.setMaximumSize(QSize(250, 100))
        self.companyAddress.setFont(font1)

        self.gridLayout_8.addWidget(self.companyAddress, 8, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 9, 1, 1, 1)

        self.loadLogo = QPushButton(self.widget)
        self.loadLogo.setObjectName(u"loadLogo")
        self.loadLogo.setMinimumSize(QSize(250, 35))
        self.loadLogo.setMaximumSize(QSize(250, 35))
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(14)
        self.loadLogo.setFont(font2)

        self.gridLayout_8.addWidget(self.loadLogo, 10, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 11, 1, 1, 1)

        self.goInvoice = QPushButton(self.widget)
        self.goInvoice.setObjectName(u"goInvoice")
        self.goInvoice.setMinimumSize(QSize(250, 35))
        self.goInvoice.setMaximumSize(QSize(250, 35))
        self.goInvoice.setFont(font2)

        self.gridLayout_8.addWidget(self.goInvoice, 12, 0, 1, 3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_3, 13, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 1, 2, 1)

        self.horizontalSpacer = QSpacerItem(384, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_7 = QGridLayout(self.page_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setVerticalSpacing(10)
        self.gridLayout_7.setContentsMargins(20, 10, 20, 10)
        self.table = QTableWidget(self.page_2)
        if (self.table.columnCount() < 5):
            self.table.setColumnCount(5)
        font3 = QFont()
        font3.setFamilies([u"Calibri"])
        font3.setPointSize(12)
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table.setObjectName(u"table")
        self.table.setFont(font1)
        self.table.horizontalHeader().setDefaultSectionSize(200)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)

        self.gridLayout_7.addWidget(self.table, 2, 0, 1, 1)

        self.widget1 = QWidget(self.page_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setMinimumSize(QSize(0, 180))
        self.widget1.setMaximumSize(QSize(16777215, 180))
        self.gridLayout_5 = QGridLayout(self.widget1)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.widget2 = QWidget(self.widget1)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setMinimumSize(QSize(200, 60))
        self.widget2.setMaximumSize(QSize(200, 60))
        self.gridLayout_4 = QGridLayout(self.widget2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 30))
        self.label_6.setMaximumSize(QSize(100, 30))
        self.label_6.setFont(font3)

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.n_invoice = QLabel(self.widget2)
        self.n_invoice.setObjectName(u"n_invoice")
        self.n_invoice.setMinimumSize(QSize(100, 30))
        self.n_invoice.setMaximumSize(QSize(100, 30))
        self.n_invoice.setFont(font1)
        self.n_invoice.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.n_invoice, 0, 1, 1, 1)

        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 30))
        self.label_8.setMaximumSize(QSize(100, 30))
        self.label_8.setFont(font3)

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)

        self.date = QLabel(self.widget2)
        self.date.setObjectName(u"date")
        self.date.setMinimumSize(QSize(100, 30))
        self.date.setMaximumSize(QSize(100, 30))
        self.date.setFont(font1)
        self.date.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.date, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget2, 0, 0, 1, 1)

        self.widget3 = QWidget(self.widget1)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setMinimumSize(QSize(450, 120))
        self.widget3.setMaximumSize(QSize(450, 120))
        self.verticalLayout_2 = QVBoxLayout(self.widget3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(200, 30))
        self.label_14.setMaximumSize(QSize(200, 30))
        font4 = QFont()
        font4.setFamilies([u"Calibri"])
        font4.setPointSize(10)
        self.label_14.setFont(font4)
        self.label_14.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.label_14)

        self.client = QLineEdit(self.widget3)
        self.client.setObjectName(u"client")
        self.client.setMinimumSize(QSize(200, 30))
        self.client.setMaximumSize(QSize(200, 30))
        self.client.setFont(font1)

        self.verticalLayout_2.addWidget(self.client)

        self.label_15 = QLabel(self.widget3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(450, 30))
        self.label_15.setMaximumSize(QSize(450, 30))
        self.label_15.setFont(font4)
        self.label_15.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.label_15)

        self.address_client = QLineEdit(self.widget3)
        self.address_client.setObjectName(u"address_client")
        self.address_client.setMinimumSize(QSize(450, 30))
        self.address_client.setMaximumSize(QSize(450, 30))
        self.address_client.setFont(font1)

        self.verticalLayout_2.addWidget(self.address_client)


        self.gridLayout_5.addWidget(self.widget3, 1, 0, 1, 1)

        self.widget4 = QWidget(self.widget1)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setMinimumSize(QSize(305, 130))
        self.widget4.setMaximumSize(QSize(305, 130))
        self.gridLayout_3 = QGridLayout(self.widget4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 30))
        self.label_10.setMaximumSize(QSize(100, 30))
        font5 = QFont()
        font5.setFamilies([u"Calibri"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.label_10.setFont(font5)
        self.label_10.setLayoutDirection(Qt.LeftToRight)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.total = QLineEdit(self.widget4)
        self.total.setObjectName(u"total")
        self.total.setMinimumSize(QSize(200, 30))
        self.total.setMaximumSize(QSize(200, 30))
        self.total.setFont(font2)
        self.total.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.total, 0, 1, 1, 1)

        self.label_11 = QLabel(self.widget4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 30))
        self.label_11.setMaximumSize(QSize(100, 30))
        self.label_11.setFont(font5)
        self.label_11.setLayoutDirection(Qt.LeftToRight)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)

        self.discount = QLineEdit(self.widget4)
        self.discount.setObjectName(u"discount")
        self.discount.setMinimumSize(QSize(200, 30))
        self.discount.setMaximumSize(QSize(200, 30))
        self.discount.setFont(font2)
        self.discount.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.discount, 1, 1, 1, 1)

        self.label_12 = QLabel(self.widget4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(100, 30))
        self.label_12.setMaximumSize(QSize(100, 30))
        self.label_12.setFont(font5)
        self.label_12.setLayoutDirection(Qt.LeftToRight)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)

        self.payment = QLineEdit(self.widget4)
        self.payment.setObjectName(u"payment")
        self.payment.setMinimumSize(QSize(200, 30))
        self.payment.setMaximumSize(QSize(200, 30))
        self.payment.setFont(font2)
        self.payment.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.payment, 2, 1, 1, 1)

        self.label_13 = QLabel(self.widget4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 30))
        self.label_13.setMaximumSize(QSize(100, 30))
        self.label_13.setFont(font5)
        self.label_13.setLayoutDirection(Qt.LeftToRight)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)

        self.rest = QLineEdit(self.widget4)
        self.rest.setObjectName(u"rest")
        self.rest.setMinimumSize(QSize(200, 30))
        self.rest.setMaximumSize(QSize(200, 30))
        self.rest.setFont(font2)
        self.rest.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.rest, 3, 1, 1, 1)


        self.gridLayout_5.addWidget(self.widget4, 0, 2, 2, 1)


        self.gridLayout_7.addWidget(self.widget1, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.page_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 60))
        self.widget_3.setMaximumSize(QSize(16777215, 60))
        self.gridLayout_6 = QGridLayout(self.widget_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(10)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(200, 30))
        self.label_17.setMaximumSize(QSize(200, 30))
        self.label_17.setFont(font4)
        self.label_17.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_6.addWidget(self.label_17, 0, 1, 1, 1)

        self.printSaveInvoice = QPushButton(self.widget_3)
        self.printSaveInvoice.setObjectName(u"printSaveInvoice")
        self.printSaveInvoice.setMinimumSize(QSize(140, 30))
        self.printSaveInvoice.setMaximumSize(QSize(140, 30))
        self.printSaveInvoice.setFont(font1)

        self.gridLayout_6.addWidget(self.printSaveInvoice, 1, 6, 1, 1)

        self.newInvoice = QPushButton(self.widget_3)
        self.newInvoice.setObjectName(u"newInvoice")
        self.newInvoice.setMinimumSize(QSize(100, 30))
        self.newInvoice.setMaximumSize(QSize(100, 30))
        self.newInvoice.setFont(font1)

        self.gridLayout_6.addWidget(self.newInvoice, 1, 5, 1, 1)

        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(200, 30))
        self.label_16.setMaximumSize(QSize(200, 30))
        self.label_16.setFont(font4)
        self.label_16.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout_6.addWidget(self.label_16, 0, 2, 1, 1)

        self.quantity = QLineEdit(self.widget_3)
        self.quantity.setObjectName(u"quantity")
        self.quantity.setMinimumSize(QSize(200, 30))
        self.quantity.setMaximumSize(QSize(200, 30))
        font6 = QFont()
        font6.setFamilies([u"Calibri"])
        font6.setPointSize(13)
        self.quantity.setFont(font6)
        self.quantity.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.quantity, 1, 1, 1, 1)

        self.product = QComboBox(self.widget_3)
        self.product.addItem("")
        self.product.addItem("")
        self.product.addItem("")
        self.product.addItem("")
        self.product.addItem("")
        self.product.setObjectName(u"product")
        self.product.setMinimumSize(QSize(200, 30))
        self.product.setMaximumSize(QSize(200, 30))
        self.product.setFont(font1)

        self.gridLayout_6.addWidget(self.product, 1, 0, 1, 1)

        self.price = QLineEdit(self.widget_3)
        self.price.setObjectName(u"price")
        self.price.setMinimumSize(QSize(200, 30))
        self.price.setMaximumSize(QSize(200, 30))
        self.price.setFont(font6)
        self.price.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.price, 1, 2, 1, 1)

        self.addProduct = QPushButton(self.widget_3)
        self.addProduct.setObjectName(u"addProduct")
        self.addProduct.setMinimumSize(QSize(100, 30))
        self.addProduct.setMaximumSize(QSize(100, 30))
        self.addProduct.setFont(font1)

        self.gridLayout_6.addWidget(self.addProduct, 1, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 1, 4, 1, 1)


        self.gridLayout_7.addWidget(self.widget_3, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_9 = QGridLayout(self.page_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(20)
        self.gridLayout_9.setVerticalSpacing(10)
        self.gridLayout_9.setContentsMargins(20, 0, 20, 10)
        self.pdfView = QPdfView(self.page_3)
        self.pdfView.setObjectName(u"pdfView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pdfView.sizePolicy().hasHeightForWidth())
        self.pdfView.setSizePolicy(sizePolicy)

        self.gridLayout_9.addWidget(self.pdfView, 0, 0, 1, 3)

        self.horizontalSpacer_7 = QSpacerItem(757, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.page_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 30))
        self.pushButton.setMaximumSize(QSize(100, 30))
        self.pushButton.setFont(font2)

        self.gridLayout_9.addWidget(self.pushButton, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.page_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 30))
        self.pushButton_2.setMaximumSize(QSize(100, 30))
        self.pushButton_2.setFont(font2)

        self.gridLayout_9.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"LOGO", None))
        self.label.setText("")
        self.companyName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Company Name", None))
        self.label_2.setText("")
        self.phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.label_3.setText("")
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_4.setText("")
        self.companyAddress.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Calibri'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.companyAddress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.loadLogo.setText(QCoreApplication.translate("MainWindow", u"Load Logo", None))
        self.goInvoice.setText(QCoreApplication.translate("MainWindow", u"Go To Invoice", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Product", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Invoice :", None))
        self.n_invoice.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.date.setText("")
        self.label_14.setText("")
        self.client.setText("")
        self.client.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Client", None))
        self.label_15.setText("")
        self.address_client.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Total :", None))
        self.total.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Discount :", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Payment :", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Rest :", None))
        self.label_17.setText("")
        self.printSaveInvoice.setText(QCoreApplication.translate("MainWindow", u"Print / Save Invoice", None))
        self.newInvoice.setText(QCoreApplication.translate("MainWindow", u"New Invoice", None))
        self.label_16.setText("")
        self.quantity.setText("")
        self.quantity.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.product.setItemText(0, QCoreApplication.translate("MainWindow", u"product-101", None))
        self.product.setItemText(1, QCoreApplication.translate("MainWindow", u"product-102", None))
        self.product.setItemText(2, QCoreApplication.translate("MainWindow", u"product-103", None))
        self.product.setItemText(3, QCoreApplication.translate("MainWindow", u"product-104", None))
        self.product.setItemText(4, QCoreApplication.translate("MainWindow", u"product-105", None))

        self.product.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.price.setText("")
        self.price.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.addProduct.setText(QCoreApplication.translate("MainWindow", u"Add Product", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Print", None))
    # retranslateUi

