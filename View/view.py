from PySide6.QtWidgets import *
import sys
import Controller.controller


# code found on online doc for qt
# not finished yet - too little knowledge so far - to be continued ;)

"""class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setGeometry(50, 50, 500, 200)
        self.setWindowTitle("Find Acronym")

        # create widgets
        self.edit = QLineEdit()
        self.button = QPushButton("Show Acronym")

        # create layout for the widgets
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        # connect the button
        self.button.clicked.connect(self.getRes())


    def getRes(self):
        Controller.controller.execute(self.edit.text())


if __name__ == '__main__':
    # create the qt app
    app = QApplication(sys.argv)

    # create and show the form
    form = Form()
    form.show()

    # run the qt main loop
    sys.exit(app.exec())"""
