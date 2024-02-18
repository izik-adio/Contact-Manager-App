from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QTimer, QObject, pyqtSignal
from update_contact import Ui_Form as Contact_Ui
from database import DataBase


class Ui_Form(QObject, object):
    searchTextChanged = pyqtSignal(str, str)

    def __init__(self) -> None:
        super().__init__()
        self.searchTextChanged.connect(
            lambda search_text, search_no: self.search(search_text, search_no)
        )
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.handleSearch)
        self.timer.start(500)

        self.update_contact_ui = Contact_Ui()
        self.form = QtWidgets.QWidget()
        self.update_contact_ui.setupUi(self.form)

    def setupUi(self, Form):
        self.DataBase = DataBase()
        Form.setObjectName("Form")
        Form.resize(741, 635)
        Form.setMinimumSize(QtCore.QSize(741, 635))
        Form.setMaximumSize(QtCore.QSize(741, 635))
        Form.setStyleSheet(
            'font: 57 10pt "Dubai Medium";\n'
            "background-color: rgb(0, 0, 63);\n"
            "color: rgb(255, 255, 255);"
        )
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 722, 161))

        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(parent=self.groupBox)
        self.widget.setGeometry(QtCore.QRect(11, 30, 701, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        # Name Input
        self.nameInput = QtWidgets.QLineEdit(parent=self.widget)
        self.nameInput.setObjectName("nameInput")

        self.horizontalLayout.addWidget(self.nameInput)
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        # Email Input
        self.emailInput = QtWidgets.QLineEdit(parent=self.widget)
        self.emailInput.setObjectName("emailInput")

        self.horizontalLayout.addWidget(self.emailInput)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)

        # phone number input
        self.phoneNumInput = QtWidgets.QLineEdit(parent=self.widget)
        self.phoneNumInput.setObjectName("phoneNumInput")

        self.horizontalLayout.addWidget(self.phoneNumInput)
        self.widget1 = QtWidgets.QWidget(parent=self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(10, 69, 701, 41))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)

        # Address input
        self.address_input = QtWidgets.QLineEdit(parent=self.widget1)
        self.address_input.setObjectName("address_input")
        self.horizontalLayout_2.addWidget(self.address_input)
        self.widget2 = QtWidgets.QWidget(parent=self.groupBox)
        self.widget2.setGeometry(QtCore.QRect(550, 110, 158, 39))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # add contact button
        self.addContactBtn = QtWidgets.QDialogButtonBox(parent=self.widget2)
        self.addContactBtn.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "color: rgb(0, 0, 38);\n"
            'font: 57 12pt "Dubai Medium";'
        )
        self.addContactBtn.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Reset
            | QtWidgets.QDialogButtonBox.StandardButton.Save
        )
        self.addContactBtn.setObjectName("addContactBtn")
        self.horizontalLayout_3.addWidget(self.addContactBtn)

        self.addContactBtn.clicked.connect(self.save_reset)

        # delete button
        self.del_btn = QtWidgets.QPushButton(parent=Form)
        self.del_btn.setGeometry(QtCore.QRect(40, 590, 109, 35))
        self.del_btn.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "color: rgb(0, 0, 38);\n"
            'font: 57 12pt "Dubai Medium";'
        )
        self.del_btn.setObjectName("del_btn")
        self.del_btn.clicked.connect(self.delete_contact)

        # update contact button
        self.update_btn = QtWidgets.QPushButton(parent=Form)
        self.update_btn.setGeometry(QtCore.QRect(160, 590, 113, 35))
        self.update_btn.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "color: rgb(0, 0, 38);\n"
            'font: 57 12pt "Dubai Medium";'
        )
        self.update_btn.setObjectName("update_btn")
        self.update_btn.clicked.connect(self.update_contact)

        # tab section
        self.tabSection = QtWidgets.QTabWidget(parent=Form)
        self.tabSection.setGeometry(QtCore.QRect(10, 179, 721, 401))
        self.tabSection.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n"
            "color: rgb(0, 0, 38);\n"
            'font: 57 10pt "Dubai Medium";'
        )
        self.tabSection.setObjectName("tabSection")
        self.tabSection.currentChanged.connect(self.handleSearch)
        self.View = QtWidgets.QWidget()
        self.View.setObjectName("View")
        self.gridLayout = QtWidgets.QGridLayout(self.View)
        self.gridLayout.setObjectName("gridLayout")

        # search section
        self.Search = QtWidgets.QWidget()
        self.Search.setObjectName("Search")

        # search contact table
        self.search_contactView = QtWidgets.QTableWidget(parent=self.Search)
        self.search_contactView.setGeometry(QtCore.QRect(10, 60, 691, 291))
        self.search_contactView.setObjectName("search_contactView")
        self.search_contactView.setColumnCount(4)
        self.search_contactView.setRowCount(0)
        self.search_contactView.itemClicked.connect(self.itemClicked)
        item = QtWidgets.QTableWidgetItem()
        self.search_contactView.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_contactView.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_contactView.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_contactView.setHorizontalHeaderItem(3, item)
        self.widget3 = QtWidgets.QWidget(parent=self.Search)
        self.widget3.setGeometry(QtCore.QRect(10, 10, 691, 37))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.widget3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)

        # search name
        self.searchName = QtWidgets.QLineEdit(parent=self.widget3)
        self.searchName.setObjectName("searchName")

        self.horizontalLayout_4.addWidget(self.searchName)
        self.label_5 = QtWidgets.QLabel(parent=self.widget3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)

        # search phone number
        self.searc_phoneNum = QtWidgets.QLineEdit(parent=self.widget3)
        self.searc_phoneNum.setObjectName("searc_phoneNum")

        self.horizontalLayout_4.addWidget(self.searc_phoneNum)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.tabSection.addTab(self.Search, "")

        self.retranslateUi(Form)
        self.tabSection.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def input_error_dialouge(self, message):
        validate_input = QtWidgets.QMessageBox()
        validate_input.setText(message)
        validate_input.setFont(QtGui.QFont("Dubai Medium", 12))
        validate_input.setWindowTitle("Input Error")
        validate_input.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        validate_input.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        validate_input.exec()

    def info_dialouge(self, message, title):
        contact_created_dialog = QtWidgets.QMessageBox()
        contact_created_dialog.setText(message)
        contact_created_dialog.setFont(QtGui.QFont("Dubai Medium", 12))
        contact_created_dialog.setWindowTitle(title)
        contact_created_dialog.setIcon(QtWidgets.QMessageBox.Icon.Information)
        contact_created_dialog.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Ok
        )
        contact_created_dialog.exec()

    def clear_input(self):
        self.nameInput.setText("")
        self.emailInput.setText("")
        self.address_input.setText("")
        self.phoneNumInput.setText("")

    def save_reset(self, signal):
        if signal.text() == "Reset":
            self.clear_input()
        elif signal.text() == "Save":
            self.validate_Input()

    def validate_Input(self):
        if self.nameInput.text().strip() == "":
            self.input_error_dialouge(
                "The name field cannot be empty.\nPlease input your contact's name"
            )
        elif self.phoneNumInput.text().strip() == "":
            self.input_error_dialouge(
                "The Phone No field cannot be empty.\nPlease input your contact's Phone Number"
            )
        elif self.phoneNumInput.text().strip().isdigit() == False:
            self.input_error_dialouge(
                "Please enter a valid phone number\nconsisting only of digits."
            )
        else:
            if self.DataBase.create_contact(
                self.nameInput.text(),
                self.phoneNumInput.text(),
                self.emailInput.text(),
                self.address_input.text(),
            ):
                self.info_dialouge("Contact Created Successfully", "Contact Created")
            self.clear_input()

    def create_table_item(self, contact):
        return (
            QtWidgets.QTableWidgetItem(contact[0]),
            QtWidgets.QTableWidgetItem(contact[1]),
            QtWidgets.QTableWidgetItem(contact[2]),
            QtWidgets.QTableWidgetItem(contact[3]),
        )

    def itemClicked(self, item):
        current_row = item.row()
        self.search_contactView.selectRow(current_row)

    def handleSearch(self):
        currentTab = self.tabSection.currentWidget().objectName()
        if currentTab == "Search":
            search_text = self.searchName.text()
            search_no = self.searc_phoneNum.text()
            self.searchTextChanged.emit(search_text, search_no)

    def search(self, search_text, search_no):
        searchResult = self.DataBase.search(name=search_text, phone_num=search_no)
        self.search_contactView.setRowCount(len(searchResult))
        for row, contact in enumerate(searchResult):
            contact_item = self.create_table_item(contact)
            for col, item in enumerate(contact_item):
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.search_contactView.setItem(row, col, item)

    def delete_contact_dialog(self, message):
        """Display a confirmation dialog for contact deletion.

        Args:
            message (str): The message to be displayed in the confirmation dialog.

        Returns:
            int: 1 if the user clicks 'Yes', None otherwise.
        """
        delete_contact_dialog = QtWidgets.QMessageBox()
        delete_contact_dialog.setText(message)
        delete_contact_dialog.setFont(QtGui.QFont("Georgia", 12))
        delete_contact_dialog.setWindowTitle("Delete Task Confirmation")
        delete_contact_dialog.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        delete_contact_dialog.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Yes
            | QtWidgets.QMessageBox.StandardButton.No
        )
        clicked_btn = delete_contact_dialog.exec()

        if clicked_btn == QtWidgets.QMessageBox.StandardButton.Yes:
            return 1
        else:
            return None

    def delete_contact(self):
        selected = self.search_contactView.selectedItems()
        if selected == [] or len(selected) > 4:
            self.info_dialouge(
                "Please click on a contact to select it then click\nthe delete button to delete the contact.\n\nN.B: You can't delete more than\n         one contact at a time.",
                "Delete Contact",
            )
        else:
            name = selected[0].text()
            no = selected[1].text()
            delete = self.delete_contact_dialog(
                f"Are you sure you'll like to delete '{name.upper()}' contact details"
            )
            if delete:
                self.DataBase.del_contact(name, no)
                self.info_dialouge(f"{name.upper()} contact details has been deleted.", "Contact Deleted")
            else:
                self.info_dialouge(f"{name.upper()} contact has {"not".upper()} been deleted.", "Contact Not Deleted")

    def update_contact(self):
        selected = self.search_contactView.selectedItems()
        if selected == [] or len(selected) > 4:
            self.info_dialouge(
                "Please click on a contact to select it then click\nthe update button to update the contact.\n\nN.B: You can't update more than\n         one contact at a time.",
                "Update Contact",
            )
        else:
            name = selected[0].text()
            no = selected[1].text()
            user_data = self.DataBase.contact_detail(name, no)
            self.update_contact_ui.fill_inputs(*user_data)
            self.form.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Add Contact"))
        self.label_2.setText(_translate("Form", "Name:"))
        self.label.setText(_translate("Form", "Email:"))
        self.label_4.setText(_translate("Form", "Phone No:"))
        self.label_3.setText(_translate("Form", "Address:"))
        self.del_btn.setText(_translate("Form", "Delete Contact"))
        self.update_btn.setText(_translate("Form", "Update Contact"))


        self.tabSection.setTabText(
            self.tabSection.indexOf(self.View), _translate("Form", "Contact View")
        )
        item = self.search_contactView.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.search_contactView.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Phone No"))
        item = self.search_contactView.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Email"))
        item = self.search_contactView.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Address"))
        self.label_6.setText(_translate("Form", "Name:"))
        self.label_5.setText(_translate("Form", "Phone No:"))
        self.tabSection.setTabText(
            self.tabSection.indexOf(self.Search), _translate("Form", "Search Contact")
        )

        # resize columns of table
        self.search_contactView.setColumnWidth(0, 125)
        self.search_contactView.setColumnWidth(1, 110)
        self.search_contactView.setColumnWidth(2, 185)
        self.search_contactView.setColumnWidth(3, 225)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
