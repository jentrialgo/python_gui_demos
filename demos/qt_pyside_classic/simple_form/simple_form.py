import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


class DecimalToBinary(QMainWindow):
    def __init__(self):
        super().__init__()

        self.entry_box = QLineEdit()
        self.result_label = QLabel()

        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear)

        col = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()

        row1.addWidget(self.entry_box)
        row1.addWidget(self.convert_button)
        row1.addWidget(self.clear_button)

        row2.addWidget(self.result_label)

        col.addLayout(row1)
        col.addLayout(row2)

        widget = QWidget()
        widget.setLayout(col)
        self.setCentralWidget(widget)

        self.show()

    def convert(self):
        decimal = int(self.entry_box.text())
        self.result_label.setText(bin(decimal))

    def clear(self):
        self.entry_box.clear()
        self.result_label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DecimalToBinary()
    sys.exit(app.exec_())
