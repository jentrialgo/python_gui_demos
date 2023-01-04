import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QListView,
    QProgressBar,
)
import PySide6.QtCore as QtCore
from PySide6.QtGui import QStandardItemModel, QStandardItem

sys.path.insert(0, "../../..")
import demos_res.rest_mock.rest_mock as rest_mock


class RestConsumer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title_label = QLabel("Rest consumer")
        self.get_users_button = QPushButton("Get users")
        self.get_users_button.clicked.connect(self.get_users)
        self.list_view = QListView()
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setVisible(False)

        col = QVBoxLayout()

        col.addWidget(self.title_label)
        col.addWidget(self.get_users_button)
        col.addWidget(self.list_view)
        col.addWidget(self.progress_bar)

        widget = QWidget()
        widget.setLayout(col)
        self.setCentralWidget(widget)

        self.thread = UserDownload()
        self.thread.taskFinished.connect(self.on_finished)

        self.model = QStandardItemModel()
        self.list_view.setModel(self.model)

        self.show()

    def get_users(self):
        self.progress_bar.show()
        self.thread.start()

    @QtCore.Slot()
    def on_finished(self):
        for user in self.thread.response["users"]:
            text = user["firstName"] + " " + user["lastName"]
            self.model.appendRow(QStandardItem(text))
        self.progress_bar.hide()


class UserDownload(QtCore.QThread):
    taskFinished = QtCore.Signal()

    def run(self):
        self.response = rest_mock.get_users()
        self.taskFinished.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RestConsumer()
    sys.exit(app.exec())
