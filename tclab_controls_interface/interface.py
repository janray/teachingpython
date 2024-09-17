# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (  # type: ignore
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (  # type: ignore
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (  # type: ignore
    QApplication,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from pyqtgraph import GraphicsLayoutWidget  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 550)
        MainWindow.setMinimumSize(QSize(900, 550))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setMinimumSize(QSize(700, 0))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color:none")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plotWindow = GraphicsLayoutWidget(self.frame)
        self.plotWindow.setObjectName("plotWindow")

        self.horizontalLayout_2.addWidget(self.plotWindow)

        self.horizontalLayout.addWidget(self.frame)

        self.horizontalSpacer = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setMaximumSize(QSize(100, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.portsComboBox = QComboBox(self.frame_2)
        self.portsComboBox.setObjectName("portsComboBox")

        self.verticalLayout.addWidget(self.portsComboBox)

        self.portConnectBtn = QPushButton(self.frame_2)
        self.portConnectBtn.setObjectName("portConnectBtn")

        self.verticalLayout.addWidget(self.portConnectBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.plotBtn = QPushButton(self.frame_2)
        self.plotBtn.setObjectName("plotBtn")

        self.verticalLayout.addWidget(self.plotBtn)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.setPointField = QLineEdit(self.frame_2)
        self.setPointField.setObjectName("setPointField")

        self.verticalLayout.addWidget(self.setPointField)

        self.setPointBtn = QPushButton(self.frame_2)
        self.setPointBtn.setObjectName("setPointBtn")

        self.verticalLayout.addWidget(self.setPointBtn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "TCLAB Interface", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "PORTS:", None))
        self.portConnectBtn.setText(QCoreApplication.translate("MainWindow", "Connect", None))
        self.plotBtn.setText(QCoreApplication.translate("MainWindow", "PLOT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "SET POINT:", None))
        self.setPointBtn.setText(QCoreApplication.translate("MainWindow", "Set", None))

    # retranslateUi
