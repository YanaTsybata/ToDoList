import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QCheckBox, QLineEdit, QPushButton, QWidget, QFrame, QScrollArea
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from ui_main import Ui_MainWindow

class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.bt_add_task.clicked.connect(self.add_task)

        # Create a QScrollArea
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("background: transparent; border: none;")

        # Create a widget for the content of QScrollArea
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)

        # Set a content for QScrollArea
        self.scroll_area.setWidget(self.scroll_content)

        # Add QScrollArea in the main_frame
        layout = QVBoxLayout(self.ui.main_frame)
        layout.addWidget(self.scroll_area)

        # Add existing tasks to scroll_layout
        self.scroll_layout.addWidget(self.ui.task_1)
        self.scroll_layout.addWidget(self.ui.task_2)
        self.scroll_layout.addWidget(self.ui.task_3)

        # Add a stretch widget at the end so that tasks are at the top
        self.scroll_layout.addStretch()

        # btn for deleting tasks
        self.ui.bt_delete1.clicked.connect(lambda: self.remove_task(self.ui.task_1))
        self.ui.bt_delete2.clicked.connect(lambda: self.remove_task(self.ui.task_2))
        self.ui.bt_delete_3.clicked.connect(lambda: self.remove_task(self.ui.task_3))

    def add_task(self):
        task_widget = QFrame()
        task_widget.setStyleSheet(self.ui.task_1.styleSheet())
        task_widget.setFixedHeight(self.ui.task_1.height())  # Set the same height as existing tasks

        task_layout = QHBoxLayout(task_widget)
        task_layout.setContentsMargins(9, 9, 9, 9)  # Set the same margins as in existing tasks

        checkbox = QCheckBox()
        checkbox.setFixedSize(self.ui.checkBox_1.size())
        checkbox.setStyleSheet(self.ui.checkBox_1.styleSheet())

        task_edit = QLineEdit()
        task_edit.setFixedHeight(self.ui.lineEdit_1.height())
        task_edit.setStyleSheet(self.ui.lineEdit_1.styleSheet())

        delete_button = QPushButton()
        delete_button.setFixedSize(self.ui.bt_delete1.size())
        delete_button.setStyleSheet(self.ui.bt_delete1.styleSheet())
        delete_button.setIcon(QIcon(":/icons/icons/delete_white_24dp.svg"))
        delete_button.setIconSize(self.ui.bt_delete1.iconSize())

        task_layout.addWidget(checkbox)
        task_layout.addWidget(task_edit)
        task_layout.addWidget(delete_button)

        # Set new task before stretch widget
        self.scroll_layout.insertWidget(self.scroll_layout.count() - 1, task_widget)

        delete_button.clicked.connect(lambda: self.remove_task(task_widget))

    def remove_task(self, task_widget):
        self.scroll_layout.removeWidget(task_widget)
        task_widget.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec())
