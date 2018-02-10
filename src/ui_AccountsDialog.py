# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AccountsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AccountsDialog(object):
    def setupUi(self, AccountsDialog):
        AccountsDialog.setObjectName("AccountsDialog")
        AccountsDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AccountsDialog.resize(420, 280)
        AccountsDialog.setMinimumSize(QtCore.QSize(420, 280))
        AccountsDialog.setMaximumSize(QtCore.QSize(420, 280))
        AccountsDialog.setBaseSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(AccountsDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(AccountsDialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.accountIdLE = QtWidgets.QLineEdit(AccountsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accountIdLE.sizePolicy().hasHeightForWidth())
        self.accountIdLE.setSizePolicy(sizePolicy)
        self.accountIdLE.setObjectName("accountIdLE")
        self.verticalLayout_2.addWidget(self.accountIdLE)
        self.label_2 = QtWidgets.QLabel(AccountsDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.apiKeyLE = QtWidgets.QLineEdit(AccountsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apiKeyLE.sizePolicy().hasHeightForWidth())
        self.apiKeyLE.setSizePolicy(sizePolicy)
        self.apiKeyLE.setObjectName("apiKeyLE")
        self.verticalLayout_2.addWidget(self.apiKeyLE)
        self.label_3 = QtWidgets.QLabel(AccountsDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.secretKeyLE = QtWidgets.QLineEdit(AccountsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.secretKeyLE.sizePolicy().hasHeightForWidth())
        self.secretKeyLE.setSizePolicy(sizePolicy)
        self.secretKeyLE.setObjectName("secretKeyLE")
        self.verticalLayout_2.addWidget(self.secretKeyLE)
        self.sandboxCB = QtWidgets.QCheckBox(AccountsDialog)
        self.sandboxCB.setObjectName("sandboxCB")
        self.verticalLayout_2.addWidget(self.sandboxCB)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(AccountsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.traderCB = QtWidgets.QCheckBox(self.groupBox)
        self.traderCB.setObjectName("traderCB")
        self.verticalLayout.addWidget(self.traderCB)
        self.heartbeatCB = QtWidgets.QCheckBox(self.groupBox)
        self.heartbeatCB.setObjectName("heartbeatCB")
        self.verticalLayout.addWidget(self.heartbeatCB)
        self.fundManagerCB = QtWidgets.QCheckBox(self.groupBox)
        self.fundManagerCB.setObjectName("fundManagerCB")
        self.verticalLayout.addWidget(self.fundManagerCB)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(391, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.manageButton = QtWidgets.QPushButton(AccountsDialog)
        self.manageButton.setObjectName("manageButton")
        self.horizontalLayout.addWidget(self.manageButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.updateButton = QtWidgets.QPushButton(AccountsDialog)
        self.updateButton.setObjectName("updateButton")
        self.horizontalLayout.addWidget(self.updateButton)
        self.addButton = QtWidgets.QPushButton(AccountsDialog)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.doneButton = QtWidgets.QPushButton(AccountsDialog)
        self.doneButton.setObjectName("doneButton")
        self.horizontalLayout.addWidget(self.doneButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(AccountsDialog)
        QtCore.QMetaObject.connectSlotsByName(AccountsDialog)

    def retranslateUi(self, AccountsDialog):
        _translate = QtCore.QCoreApplication.translate
        AccountsDialog.setWindowTitle(_translate("AccountsDialog", "Setup Account"))
        self.label.setText(_translate("AccountsDialog", "Account ID:"))
        self.label_2.setText(_translate("AccountsDialog", "API Key:"))
        self.label_3.setText(_translate("AccountsDialog", "Secret Key:"))
        self.sandboxCB.setText(_translate("AccountsDialog", "Sandbox Account?"))
        self.groupBox.setTitle(_translate("AccountsDialog", "Role:"))
        self.traderCB.setText(_translate("AccountsDialog", "Trader"))
        self.heartbeatCB.setText(_translate("AccountsDialog", "Require heartbeat?"))
        self.fundManagerCB.setText(_translate("AccountsDialog", "Fund Manager"))
        self.manageButton.setText(_translate("AccountsDialog", "&Manage"))
        self.updateButton.setText(_translate("AccountsDialog", "&Update"))
        self.addButton.setText(_translate("AccountsDialog", "&Add"))
        self.doneButton.setText(_translate("AccountsDialog", "&Done"))

