from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPalette, QColor, QDesktopServices
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from ui_form import Ui_Widget
import sys

from main_functions import *
from color_settings import *


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Прописываем нажатие на кнопки
        self.ui.pushButton_2.clicked.connect(self.openDialog)
        self.ui.pushButton.clicked.connect(self.Fun_job)
        self.ui.checkBox.clicked.connect(self.Night)

        self.file_path = ""

        self.ui.textBrowser.anchorClicked.connect(lambda url: QDesktopServices.openUrl(url))
        self.ui.textBrowser.setOpenLinks(False)

    def openDialog(self):  # Кнопка "Выбрать файл"
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Text files (*.txt *.md *.html)")

        if not file_path:
            return

        self.file_path = file_path

        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            self.ui.textBrowser.setPlainText(text)

    def Fun_job(self):  # Кнопка "Начать"
        if self.ui.comboBox_2.currentText() != "Выберите язык разметки" and self.ui.comboBox.currentText() != "@Ссылки" and self.ui.textBrowser.toPlainText()!= "":
            # === Usage example ===
            lines = read_file_to_string(self.file_path)

            file_format = ""
            if self.ui.comboBox_2.currentText() == "Обычный":
                file_format = ".txt"
            elif self.ui.comboBox_2.currentText() == "Markdown":
                file_format = ".md"
            elif self.ui.comboBox_2.currentText() == "HTML":
                file_format = ".html"

            user_format = ""
            if self.ui.comboBox.currentText() == "Telegram":
                user_format = "tg"
            elif self.ui.comboBox.currentText() == "Vk":
                user_format = "vk"

            lines = add_hyperlinks_to_string(lines, file_format, user_format)
            save_string_to_file(f"result{file_format}", lines)

            if file_format == ".txt":
                self.ui.textBrowser.setPlainText(lines)
            elif file_format == ".md":                self.ui.textBrowser.setMarkdown(lines)
            elif file_format == ".html":
                self.ui.textBrowser.setHtml(lines)

        else:
            # Создаем диалоговое окно
            Box = QMessageBox()
            Box.setIcon(QMessageBox.Warning)
            Box.setText("Ошибка!")
            Box.setInformativeText(
                "Пожалуйста, выберите язык разметки и предпочтительные ссылки, а также добавьте текст в текстовое поле.")
            Box.exec()

    def Night(self):  # Темная тема
        if self.ui.checkBox.isChecked():
            # Установка темной темы
            self.setStyleSheet(f"background-color: {dark}; color: #ffffff;")  # Фон - #292831, текст - белый
            self.ui.textBrowser.setStyleSheet(f"background-color: {dark}; color: #ffffff;")  # Текст - белый
            self.ui.comboBox.setStyleSheet(f"background-color: {dark}; color: #ffffff;")  # Текст - белый
            self.ui.pushButton.setStyleSheet(f"""
                QPushButton {{
                    border-radius: 10px; /* Закругление углов */
                    border: 2px solid {border}; /* Цвет границы */
                    padding: 6px; /* Отступы внутри кнопки */
                    background-color: {dark}; /* Фон */
                    color: #ffffff; /* Цвет текста */
                }}
                QPushButton:hover {{
                    background-color: {dark_background_aim}; /* Фон при наведении */
                }}
                QPushButton:pressed {{
                    background-color: {dark_background_click}; /* Фон при нажатии */
                }}
            """)
            self.ui.pushButton_2.setStyleSheet(f"""
                QPushButton {{
                    border-radius: 10px; /* Закругление углов */
                    border: 2px solid {border}; /* Цвет границы */
                    padding: 6px; /* Отступы внутри кнопки */
                    background-color: {dark}; /* Фон */
                    color: #ffffff; /* Цвет текста */
                }}
                QPushButton:hover {{
                    background-color: {dark_background_aim}; /* Фон при наведении */
                }}
                QPushButton:pressed {{
                    background-color: {dark_background_click}; /* Фон при нажатии */
                }}
            """)
            self.ui.comboBox.setStyleSheet(f"""
                QComboBox {{
                    border: 2px solid {border};
                    border-radius: 10px;
                    padding: 5px;
                    color: #000000;
                }}
                QComboBox:hover {{
                    background-color: {dark_background_aim}; /* Фон при наведении */
                }}
                QComboBox::down-arrow {{
                    image: url(images/str_1.png); /* Путь к вашему изображению */
                    width: 20px; /* Ширина изображения */
                    height: 20px; /* Высота изображения */
                }}
            """)
            self.ui.comboBox_2.setStyleSheet(f"""
                QComboBox {{
                    border: 2px solid {border};
                    border-radius: 10px;
                    padding: 5px;
                    color: #000000;
                }}
                QComboBox:hover {{
                    background-color: {dark_background_aim}; /* Фон при наведении */
                }}
                QComboBox::down-arrow {{
                    image: url(images/str_1.png); /* Путь к вашему изображению */
                    width: 20px; /* Ширина изображения */
                    height: 20px; /* Высота изображения */
                }}
            """)
            self.ui.checkBox.setStyleSheet(f"""
                QCheckBox {{
                    spacing: 5px; /* Расстояние между флажком и текстом */
                }}
                QCheckBox::indicator {{
                    width: 50px; /* Ширина флажка */
                    height: 50px; /* Высота флажка */
                    image: url('images/ghost_2.png');
                }}
                QCheckBox::indicator::unchecked {{
                    border: 2px solid {border}; /* Цвет границы при неотмеченном состоянии */
                    border-radius: 3px; /* Закругление углов */
                }}
                QCheckBox::indicator::unchecked:hover {{
                    border: 2px solid {border}; /* Цвет границы при наведении на неотмеченном состоянии */
                    background-color: {dark_background_aim};
                }}
                QCheckBox::indicator::checked {{
                    background-color: {dark}; /* Цвет фона при отмеченном состоянии */
                    border: 2px solid {border}; /* Цвет границы при отмеченном состоянии */
                    border-radius: 3px; /* Закругление углов */
                }}
                QCheckBox::indicator::checked:hover {{
                    background-color: {dark_background_aim}; /* Цвет фона при наведении на отмеченном состоянии */
                    border: 2px solid {border}; /* Цвет границы при наведении на отмеченном состоянии */
                }}
            """)
            self.ui.checkBox.setText(QCoreApplication.translate("Widget", u"Светлая тема", None))
        else:
            # Установка светлой темы
            self.setStyleSheet(f"background-color: {light}; color: #000000;")  # Фон - #fad6ff, текст - черный
            self.ui.textBrowser.setStyleSheet(f"background-color: {light}; color: #000000;")  # Текст - черный
            self.ui.comboBox.setStyleSheet(f"background-color: {light}; color: #000000;")  # Текст - черный
            self.ui.pushButton.setStyleSheet(f"""
                QPushButton {{
                    border-radius: 10px; /* Закругление углов */
                    border: 2px solid {border}; /* Цвет границы */
                    padding: 6px; /* Отступы внутри кнопки */
                    background-color: {light}; /* Фон */
                    color: #000000; /* Цвет текста */
                }}
                QPushButton:hover {{
                    background-color: {light_background_aim}; /* Фон при наведении */
                }}
                QPushButton:pressed {{
                    background-color: {light_background_click}; /* Фон при нажатии */
                }}
            """)
            self.ui.pushButton_2.setStyleSheet(f"""
                QPushButton {{
                    border-radius: 10px; /* Закругление углов */
                    border: 2px solid {border}; /* Цвет границы */
                    padding: 6px; /* Отступы внутри кнопки */
                    background-color: {light}; /* Фон */
                    color: #000000; /* Цвет текста */
                }}
                QPushButton:hover {{
                    background-color: {light_background_aim}; /* Фон при наведении */
                }}
                QPushButton:pressed {{
                    background-color: {light_background_click}; /* Фон при нажатии */
                }}
            """)
            self.ui.comboBox.setStyleSheet(f"""
                QComboBox {{
                    border: 2px solid {border};
                    border-radius: 10px;
                    padding: 5px;
                    color: #000000;
                }}
                QComboBox:hover {{
                    background-color: {light_background_aim}; /* Фон при наведении */
                }}
                QComboBox::down-arrow {{
                    image: url(images/str.png); /* Путь к вашему изображению */
                    width: 20px; /* Ширина изображения */
                    height: 20px; /* Высота изображения */
                }}
            """)
            self.ui.comboBox_2.setStyleSheet(f"""
                QComboBox {{
                    border: 2px solid {border};
                    border-radius: 10px;
                    padding: 5px;
                    color: #000000;
                }}
                QComboBox:hover {{
                    background-color: {light_background_aim}; /* Фон при наведении */
                }}
                QComboBox::down-arrow {{
                    image: url(images/str.png); /* Путь к вашему изображению */
                    width: 20px; /* Ширина изображения */
                    height: 20px; /* Высота изображения */
                }}
            """)
            self.ui.checkBox.setStyleSheet(f"""
                QCheckBox {{
                    spacing: 5px; /* Расстояние между флажком и текстом */
                }}
                QCheckBox::indicator {{
                    width: 50px; /* Ширина флажка */
                    height: 50px; /* Высота флажка */
                    image: url('images/ghost_1.png');
                }}
                QCheckBox::indicator::unchecked {{
                    border: 2px solid {border}; /* Цвет границы при неотмеченном состоянии */
                    border-radius: 3px; /* Закругление углов */
                }}
                QCheckBox::indicator::unchecked:hover {{
                    border: 2px solid {border}; /* Цвет границы при наведении на неотмеченном состоянии */
                    background-color: {light_background_aim};
                }}
                QCheckBox::indicator::checked {{
                    background-color: {dark}; /* Цвет фона при отмеченном состоянии */
                    border: 2px solid {border}; /* Цвет границы при отмеченном состоянии */
                    border-radius: 3px; /* Закругление углов */
                }}
                QCheckBox::indicator::checked:hover {{
                    background-color: {dark_background_aim}; /* Цвет фона при наведении на отмеченном состоянии */
                    border: 2px solid {border}; /* Цвет границы при наведении на отмеченном состоянии */
                }}
            """)
            self.ui.checkBox.setText(QCoreApplication.translate("Widget", u"Темная тема", None))


