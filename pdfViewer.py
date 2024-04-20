from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView
import os

from PySide6.QtCore import QCoreApplication,QMetaObject,QSize,Qt
from PySide6.QtGui import QFont
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtWidgets import QGridLayout, QMainWindow, QPushButton, QSizePolicy, QSpacerItem, QWidget

class PdfViewer(QMainWindow):
    def __init__(self,file):
        super().__init__()

        self.fileName = file
        
        self.m_document = QPdfDocument()

        self.setObjectName(u"qsdlfjlmsjf")
        self.resize(902, 431)
        
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.print_btn = QPushButton(self.centralwidget)
        self.print_btn.setObjectName(u"pushButton_2")
        self.print_btn.setMinimumSize(QSize(100, 30))
        self.print_btn.setMaximumSize(QSize(100, 30))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(14)
        self.print_btn.setFont(font)

        self.gridLayout.addWidget(self.print_btn, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(645, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.cancel_btn = QPushButton(self.centralwidget)
        self.cancel_btn.setObjectName(u"pushButton")
        self.cancel_btn.setMinimumSize(QSize(100, 30))
        self.cancel_btn.setMaximumSize(QSize(100, 30))
        self.cancel_btn.setFont(font)

        self.cancel_btn.clicked.connect(self.cancelPrint)

        self.gridLayout.addWidget(self.cancel_btn, 1, 1, 1, 1)

        self.pdfView = QPdfView(self.centralwidget)
        self.pdfView.setObjectName(u"pdfView")

        self.pdfView.setDocument(self.m_document)
        self.pdfView.setPageMode(QPdfView.PageMode.MultiPage)

        self.m_document.load(self.fileName)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pdfView.sizePolicy().hasHeightForWidth())
        self.pdfView.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pdfView, 0, 0, 1, 3)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

    def cancelPrint(self):
        self.m_document = QPdfDocument()
        os.remove(self.fileName)
        self.deleteLater()


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.print_btn.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))

