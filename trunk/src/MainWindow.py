'''
Copyright (C) 2010 Zachary Varberg
@author: Zachary Varberg

This file is part of Steganogra-py.

Steganogra-py is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Steganogra-py is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Steganogra-py.  If not, see <http://www.gnu.org/licenses/>.
'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Mon Jan 25 19:36:49 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 348)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(562, 348))
        MainWindow.setMaximumSize(QtCore.QSize(562, 348))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Steg/stegosaurus-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 561, 331))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.encodeTab = QtGui.QWidget()
        self.encodeTab.setObjectName("encodeTab")
        self.encode_red_bits_combo = QtGui.QComboBox(self.encodeTab)
        self.encode_red_bits_combo.setGeometry(QtCore.QRect(60, 210, 69, 22))
        self.encode_red_bits_combo.setObjectName("encode_red_bits_combo")
        self.encode_red_bits_combo.addItem("")
        self.encode_red_bits_combo.addItem("")
        self.encode_red_bits_combo.addItem("")
        self.encode_red_bits_combo.addItem("")
        self.encode_red_bits_combo.addItem("")
        self.encode_red_bits_combo.addItem("")
        self.encode_red_bits_combo.addItem("")
        self.encode_red_bits_combo.addItem("")
        self.encode_red_bits_combo.addItem("")
        self.encode_green_bits_combo = QtGui.QComboBox(self.encodeTab)
        self.encode_green_bits_combo.setGeometry(QtCore.QRect(240, 210, 69, 22))
        self.encode_green_bits_combo.setObjectName("encode_green_bits_combo")
        self.encode_green_bits_combo.addItem("")
        self.encode_green_bits_combo.addItem("")
        self.encode_green_bits_combo.addItem("")
        self.encode_green_bits_combo.addItem("")
        self.encode_green_bits_combo.addItem("")
        self.encode_green_bits_combo.addItem("")
        self.encode_green_bits_combo.addItem("")
        self.encode_green_bits_combo.addItem("")
        self.encode_green_bits_combo.addItem("")
        self.encode_blue_bits_combo = QtGui.QComboBox(self.encodeTab)
        self.encode_blue_bits_combo.setGeometry(QtCore.QRect(420, 210, 69, 22))
        self.encode_blue_bits_combo.setObjectName("encode_blue_bits_combo")
        self.encode_blue_bits_combo.addItem("")
        self.encode_blue_bits_combo.addItem("")
        self.encode_blue_bits_combo.addItem("")
        self.encode_blue_bits_combo.addItem("")
        self.encode_blue_bits_combo.addItem("")
        self.encode_blue_bits_combo.addItem("")
        self.encode_blue_bits_combo.addItem("")
        self.encode_blue_bits_combo.addItem("")
        self.encode_blue_bits_combo.addItem("")
        self.label = QtGui.QLabel(self.encodeTab)
        self.label.setGeometry(QtCore.QRect(30, 170, 121, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.encodeTab)
        self.label_2.setGeometry(QtCore.QRect(210, 170, 121, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.encodeTab)
        self.label_3.setGeometry(QtCore.QRect(390, 170, 121, 41))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.encode_file_text = QtGui.QLineEdit(self.encodeTab)
        self.encode_file_text.setGeometry(QtCore.QRect(20, 70, 151, 21))
        self.encode_file_text.setObjectName("encode_file_text")
        self.encode_file_browse_button = QtGui.QPushButton(self.encodeTab)
        self.encode_file_browse_button.setGeometry(QtCore.QRect(170, 70, 75, 23))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Steg/folder_explore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.encode_file_browse_button.setIcon(icon1)
        self.encode_file_browse_button.setIconSize(QtCore.QSize(20, 20))
        self.encode_file_browse_button.setObjectName("encode_file_browse_button")
        self.encode_image_browse_button = QtGui.QPushButton(self.encodeTab)
        self.encode_image_browse_button.setGeometry(QtCore.QRect(450, 70, 75, 23))
        self.encode_image_browse_button.setIcon(icon1)
        self.encode_image_browse_button.setIconSize(QtCore.QSize(20, 20))
        self.encode_image_browse_button.setObjectName("encode_image_browse_button")
        self.encode_image_text = QtGui.QLineEdit(self.encodeTab)
        self.encode_image_text.setGeometry(QtCore.QRect(300, 70, 151, 21))
        self.encode_image_text.setObjectName("encode_image_text")
        self.encode_button = QtGui.QPushButton(self.encodeTab)
        self.encode_button.setGeometry(QtCore.QRect(240, 280, 75, 23))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Steg/accept.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.encode_button.setIcon(icon2)
        self.encode_button.setIconSize(QtCore.QSize(24, 24))
        self.encode_button.setObjectName("encode_button")
        self.label_4 = QtGui.QLabel(self.encodeTab)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(self.encodeTab)
        self.label_5.setGeometry(QtCore.QRect(300, 50, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.encodeTab)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 531, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.encode_new_image_text = QtGui.QLineEdit(self.encodeTab)
        self.encode_new_image_text.setGeometry(QtCore.QRect(170, 140, 151, 21))
        self.encode_new_image_text.setObjectName("encode_new_image_text")
        self.encode_new_image_browse_button = QtGui.QPushButton(self.encodeTab)
        self.encode_new_image_browse_button.setGeometry(QtCore.QRect(320, 140, 75, 23))
        self.encode_new_image_browse_button.setIcon(icon1)
        self.encode_new_image_browse_button.setIconSize(QtCore.QSize(20, 20))
        self.encode_new_image_browse_button.setObjectName("encode_new_image_browse_button")
        self.label_13 = QtGui.QLabel(self.encodeTab)
        self.label_13.setGeometry(QtCore.QRect(170, 120, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.encodeTab, "")
        self.decodeTab = QtGui.QWidget()
        self.decodeTab.setObjectName("decodeTab")
        self.decode_file_text = QtGui.QLineEdit(self.decodeTab)
        self.decode_file_text.setGeometry(QtCore.QRect(300, 90, 151, 21))
        self.decode_file_text.setObjectName("decode_file_text")
        self.decode_image_browse_button = QtGui.QPushButton(self.decodeTab)
        self.decode_image_browse_button.setGeometry(QtCore.QRect(170, 90, 75, 23))
        self.decode_image_browse_button.setIcon(icon1)
        self.decode_image_browse_button.setIconSize(QtCore.QSize(20, 20))
        self.decode_image_browse_button.setObjectName("decode_image_browse_button")
        self.decode_button = QtGui.QPushButton(self.decodeTab)
        self.decode_button.setGeometry(QtCore.QRect(240, 280, 75, 23))
        self.decode_button.setIcon(icon2)
        self.decode_button.setIconSize(QtCore.QSize(24, 24))
        self.decode_button.setObjectName("decode_button")
        self.label_7 = QtGui.QLabel(self.decodeTab)
        self.label_7.setGeometry(QtCore.QRect(30, 70, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.decode_red_bits_combo = QtGui.QComboBox(self.decodeTab)
        self.decode_red_bits_combo.setGeometry(QtCore.QRect(60, 210, 69, 22))
        self.decode_red_bits_combo.setObjectName("decode_red_bits_combo")
        self.decode_red_bits_combo.addItem("")
        self.decode_red_bits_combo.addItem("")
        self.decode_red_bits_combo.addItem("")
        self.decode_red_bits_combo.addItem("")
        self.decode_red_bits_combo.addItem("")
        self.decode_red_bits_combo.addItem("")
        self.decode_red_bits_combo.addItem("")
        self.decode_red_bits_combo.addItem("")
        self.decode_red_bits_combo.addItem("")
        self.label_8 = QtGui.QLabel(self.decodeTab)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 531, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.decode_green_bits_combo = QtGui.QComboBox(self.decodeTab)
        self.decode_green_bits_combo.setGeometry(QtCore.QRect(240, 210, 69, 22))
        self.decode_green_bits_combo.setObjectName("decode_green_bits_combo")
        self.decode_green_bits_combo.addItem("")
        self.decode_green_bits_combo.addItem("")
        self.decode_green_bits_combo.addItem("")
        self.decode_green_bits_combo.addItem("")
        self.decode_green_bits_combo.addItem("")
        self.decode_green_bits_combo.addItem("")
        self.decode_green_bits_combo.addItem("")
        self.decode_green_bits_combo.addItem("")
        self.decode_green_bits_combo.addItem("")
        self.decode_blue_bits_combo = QtGui.QComboBox(self.decodeTab)
        self.decode_blue_bits_combo.setGeometry(QtCore.QRect(420, 210, 69, 22))
        self.decode_blue_bits_combo.setObjectName("decode_blue_bits_combo")
        self.decode_blue_bits_combo.addItem("")
        self.decode_blue_bits_combo.addItem("")
        self.decode_blue_bits_combo.addItem("")
        self.decode_blue_bits_combo.addItem("")
        self.decode_blue_bits_combo.addItem("")
        self.decode_blue_bits_combo.addItem("")
        self.decode_blue_bits_combo.addItem("")
        self.decode_blue_bits_combo.addItem("")
        self.decode_blue_bits_combo.addItem("")
        self.label_9 = QtGui.QLabel(self.decodeTab)
        self.label_9.setGeometry(QtCore.QRect(300, 70, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.decode_file_browse_button = QtGui.QPushButton(self.decodeTab)
        self.decode_file_browse_button.setGeometry(QtCore.QRect(450, 90, 75, 23))
        self.decode_file_browse_button.setIcon(icon1)
        self.decode_file_browse_button.setIconSize(QtCore.QSize(20, 20))
        self.decode_file_browse_button.setObjectName("decode_file_browse_button")
        self.decode_image_text = QtGui.QLineEdit(self.decodeTab)
        self.decode_image_text.setGeometry(QtCore.QRect(20, 90, 151, 21))
        self.decode_image_text.setObjectName("decode_image_text")
        self.label_10 = QtGui.QLabel(self.decodeTab)
        self.label_10.setGeometry(QtCore.QRect(210, 170, 121, 41))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtGui.QLabel(self.decodeTab)
        self.label_11.setGeometry(QtCore.QRect(390, 170, 121, 41))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtGui.QLabel(self.decodeTab)
        self.label_12.setGeometry(QtCore.QRect(30, 170, 121, 41))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.decodeTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.encode_file_text)
        MainWindow.setTabOrder(self.encode_file_text, self.encode_file_browse_button)
        MainWindow.setTabOrder(self.encode_file_browse_button, self.encode_image_text)
        MainWindow.setTabOrder(self.encode_image_text, self.encode_image_browse_button)
        MainWindow.setTabOrder(self.encode_image_browse_button, self.encode_new_image_text)
        MainWindow.setTabOrder(self.encode_new_image_text, self.encode_new_image_browse_button)
        MainWindow.setTabOrder(self.encode_new_image_browse_button, self.encode_red_bits_combo)
        MainWindow.setTabOrder(self.encode_red_bits_combo, self.encode_green_bits_combo)
        MainWindow.setTabOrder(self.encode_green_bits_combo, self.encode_blue_bits_combo)
        MainWindow.setTabOrder(self.encode_blue_bits_combo, self.encode_button)
        MainWindow.setTabOrder(self.encode_button, self.decode_image_text)
        MainWindow.setTabOrder(self.decode_image_text, self.decode_image_browse_button)
        MainWindow.setTabOrder(self.decode_image_browse_button, self.decode_file_text)
        MainWindow.setTabOrder(self.decode_file_text, self.decode_file_browse_button)
        MainWindow.setTabOrder(self.decode_file_browse_button, self.decode_red_bits_combo)
        MainWindow.setTabOrder(self.decode_red_bits_combo, self.decode_green_bits_combo)
        MainWindow.setTabOrder(self.decode_green_bits_combo, self.decode_blue_bits_combo)
        MainWindow.setTabOrder(self.decode_blue_bits_combo, self.decode_button)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Steganogra-py", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_red_bits_combo.setItemText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_red_bits_combo.setItemText(1, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_red_bits_combo.setItemText(2, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_red_bits_combo.setItemText(3, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_red_bits_combo.setItemText(4, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_red_bits_combo.setItemText(5, QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_red_bits_combo.setItemText(6, QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_red_bits_combo.setItemText(7, QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_red_bits_combo.setItemText(8, QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_green_bits_combo.setItemText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_green_bits_combo.setItemText(1, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_green_bits_combo.setItemText(2, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_green_bits_combo.setItemText(3, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_green_bits_combo.setItemText(4, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_green_bits_combo.setItemText(5, QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_green_bits_combo.setItemText(6, QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_green_bits_combo.setItemText(7, QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_green_bits_combo.setItemText(8, QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_blue_bits_combo.setItemText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_blue_bits_combo.setItemText(1, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_blue_bits_combo.setItemText(2, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_blue_bits_combo.setItemText(3, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_blue_bits_combo.setItemText(4, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_blue_bits_combo.setItemText(5, QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_blue_bits_combo.setItemText(6, QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_blue_bits_combo.setItemText(7, QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_blue_bits_combo.setItemText(8, QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Number of red bits \n"
"to encode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Number of green bits \n"
"to encode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Number of blue bits \n"
"to encode", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_file_browse_button.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_image_browse_button.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_button.setText(QtGui.QApplication.translate("MainWindow", "Encode!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "File to encode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Image to encode in", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Encode", None, QtGui.QApplication.UnicodeUTF8))
        self.encode_new_image_browse_button.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Encoded image file", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encodeTab), QtGui.QApplication.translate("MainWindow", "Encode", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_image_browse_button.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_button.setText(QtGui.QApplication.translate("MainWindow", "Decode!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Image to decode", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_red_bits_combo.setItemText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_red_bits_combo.setItemText(1, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_red_bits_combo.setItemText(2, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_red_bits_combo.setItemText(3, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_red_bits_combo.setItemText(4, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_red_bits_combo.setItemText(5, QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_red_bits_combo.setItemText(6, QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_red_bits_combo.setItemText(7, QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_red_bits_combo.setItemText(8, QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Decode", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_green_bits_combo.setItemText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_green_bits_combo.setItemText(1, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_green_bits_combo.setItemText(2, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_green_bits_combo.setItemText(3, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_green_bits_combo.setItemText(4, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_green_bits_combo.setItemText(5, QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_green_bits_combo.setItemText(6, QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_green_bits_combo.setItemText(7, QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_green_bits_combo.setItemText(8, QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_blue_bits_combo.setItemText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_blue_bits_combo.setItemText(1, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_blue_bits_combo.setItemText(2, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_blue_bits_combo.setItemText(3, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_blue_bits_combo.setItemText(4, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_blue_bits_combo.setItemText(5, QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_blue_bits_combo.setItemText(6, QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_blue_bits_combo.setItemText(7, QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_blue_bits_combo.setItemText(8, QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "File to save", None, QtGui.QApplication.UnicodeUTF8))
        self.decode_file_browse_button.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Number of green bits \n"
"encoded", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Number of blue bits \n"
"encoded", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Number of red bits \n"
"encoded", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.decodeTab), QtGui.QApplication.translate("MainWindow", "Decode", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

import Steg_rc