import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from database import DataBase


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(490, 177)
        Form.setMinimumSize(490, 177)
        Form.setMaximumSize(490, 177)
        Form.setStyleSheet(
            'font: 57 12pt "Dubai Medium";\n'
            "background-color: rgb(0, 0, 63);\n"
            "color: rgb(255, 255, 255);"
        )
        self.layoutWidget = QtWidgets.QWidget(parent=Form)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 470, 164))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nameInput = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.nameInput.setStyleSheet(
            "background-color: rgb(0, 0, 63);\n" "color: rgb(255, 255, 255);"
        )
        self.nameInput.setObjectName("nameInput")
        self.horizontalLayout.addWidget(self.nameInput)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.numInput = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.numInput.setStyleSheet(
            "background-color: rgb(0, 0, 63);\n" "color: rgb(255, 255, 255);"
        )
        self.numInput.setObjectName("numInput")
        self.horizontalLayout_2.addWidget(self.numInput)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.emailInput = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.emailInput.setStyleSheet(
            "background-color: rgb(0, 0, 63);\n" "color: rgb(255, 255, 255);"
        )
        self.emailInput.setObjectName("emailInput")
        self.horizontalLayout_4.addWidget(self.emailInput)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(
            self.label_4, 0, QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.addressInput = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.addressInput.setStyleSheet(
            "background-color: rgb(0, 0, 63);\n"
            "gridline-color: rgb(255, 255, 255);\n"
            "border-color: rgb(255, 255, 255);\n"
            "color: rgb(255, 255, 255);"
        )
        self.addressInput.setObjectName("addressInput")
        self.horizontalLayout_5.addWidget(self.addressInput)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_6.addItem(spacerItem)
        self.saveButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.saveButton.setStyleSheet(
            "color: rgb(0, 0, 63);\n" "background-color: rgb(255, 255, 255);"
        )
        self.saveButton.setObjectName("saveButton")
        # update contact detail on click
        self.saveButton.clicked.connect(self.validate_Input)

        self.horizontalLayout_6.addWidget(self.saveButton)
        self.clearButton = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.clearButton.setStyleSheet(
            "color: rgb(0, 0, 63);\n" "background-color: rgb(255, 255, 255);"
        )
        self.clearButton.setObjectName("clearButton")
        # clear entries if clear button is clicked
        self.clearButton.clicked.connect(self.clear)
        self.horizontalLayout_6.addWidget(self.clearButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        # initialize the database.
        self.database = DataBase()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def fill_inputs(self, name, num, email, address):
        self.previous_name = name
        self.previous_no = num
        self.nameInput.setText(name)
        self.numInput.setText(num)
        self.emailInput.setText(email)
        self.addressInput.setText(address)

    def clear(self):
        self.nameInput.setText("")
        self.numInput.setText("")
        self.emailInput.setText("")
        self.addressInput.setText("")

    def update_contact_dialog(self, message):
        update_contact_dialog = QtWidgets.QMessageBox()
        update_contact_dialog.setText(message)
        update_contact_dialog.setFont(QtGui.QFont("Georgia", 12))
        update_contact_dialog.setWindowTitle("Update Task Confirmation")
        update_contact_dialog.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        update_contact_dialog.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Yes
            | QtWidgets.QMessageBox.StandardButton.No
        )
        clicked_btn = update_contact_dialog.exec()

        if clicked_btn == QtWidgets.QMessageBox.StandardButton.Yes:
            return 1
        else:
            return None

    def input_error_dialouge(self, message):
        validate_input = QtWidgets.QMessageBox()
        validate_input.setText(message)
        validate_input.setFont(QtGui.QFont("Dubai Medium", 12))
        validate_input.setWindowTitle("Input Error")
        validate_input.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        validate_input.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        validate_input.exec()

    def validate_Input(self):
        if self.nameInput.text().strip() == "":
            self.input_error_dialouge(
                "The name field cannot be empty.\nPlease input your contact's name"
            )
        elif self.numInput.text().strip() == "":
            self.input_error_dialouge(
                "The Phone No field cannot be empty.\nPlease input your contact's Phone Number"
            )
        elif self.numInput.text().strip().isdigit() == False:
            self.input_error_dialouge(
                "Please enter a valid phone number\nconsisting only of digits."
            )
        else:
            self.new_data = self.update_contact()
            self.database.update_contact(
                previous_name=self.previous_name,
                name=self.new_data[0],
                email=self.new_data[2],
                phone_num=self.new_data[1],
                addr=self.new_data[3],
                previous_num=self.previous_no,
            )
            self.clear()

            contact_update_dialog = QtWidgets.QMessageBox()
            contact_update_dialog.setText("Contact Has Been Updated!")
            contact_update_dialog.setFont(QtGui.QFont("Dubai Medium", 12))
            contact_update_dialog.setWindowTitle("Successful Update")
            contact_update_dialog.setIcon(QtWidgets.QMessageBox.Icon.Information)
            contact_update_dialog.setStandardButtons(
                QtWidgets.QMessageBox.StandardButton.Ok
            )
            contact_update_dialog.exec()

    def update_contact(self):
        update_contact = self.update_contact_dialog(
            "Are you sure you'll like to save this changes?"
        )
        if update_contact:
            return (
                self.nameInput.text(),
                self.numInput.text(),
                self.emailInput.text(),
                self.addressInput.text(),
            )

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Update Contact"))
        self.label.setText(_translate("Form", "Name:"))
        self.label_2.setText(_translate("Form", "Phone No:"))
        self.label_3.setText(_translate("Form", "Email:"))
        self.label_4.setText(_translate("Form", "Address:"))
        self.saveButton.setText(_translate("Form", "Save"))
        self.clearButton.setText(_translate("Form", "Clear"))


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec())
