from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QVBoxLayout, QWidget)
from main_functions import *
from color_settings import *
class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setWindowModality(Qt.NonModal)
        Widget.resize(800, 628)
        icon = QIcon(QIcon.fromTheme(u"accessories-calculator"))
        Widget.setWindowIcon(icon)
        Widget.setLayoutDirection(Qt.LeftToRight)
        Widget.setStyleSheet(f"background-color:{light};")
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Forte"])
        font.setPointSize(26)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox_2 = QComboBox(Widget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(309, 43)
        font1 = QFont()
        font1.setFamilies([u"HoloLens MDL2 Assets"])
        font1.setPointSize(18)
        self.comboBox_2.setFont(font1)
        self.comboBox_2.setStyleSheet(f"""
                        QComboBox {{
                            border: 2px solid {border};
                            border-radius: 10px;
                            padding: 5px;
                            color: #00000;
                        }}
                        QComboBox:hover {{
                            background-color: {light_background_aim}; /* Фон при наведении */
                        }}
                        QComboBox::down-arrow {{
                            image: url(images/str.png); /* Путь к вашему изображению */
                            width: 20px; /* Ширина изображения */
                            height: 20px; /* Высота изображения */
                        }}""")

        self.horizontalLayout_4.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(Widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setMinimumSize(309, 43)
        self.comboBox.setObjectName(u"comboBox")
        font2 = QFont()
        font2.setFamilies([u"HoloLens MDL2 Assets"])
        font2.setPointSize(18)
        self.comboBox.setFont(font2)
        self.comboBox.setStyleSheet(f"""
                        QComboBox {{
                            border: 2px solid {border};
                            border-radius: 10px;
                            padding: 5px;
                            color: #00000;
                        }}
                        QComboBox:hover {{
                            background-color: {light_background_aim}; /* Фон при наведении */
                        }}
                        QComboBox::down-arrow {{
                            image: url(images/str.png); /* Путь к вашему изображению */
                            width: 20px; /* Ширина изображения */
                            height: 20px; /* Высота изображения */
                        }}""")


        self.horizontalLayout_4.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setMaximumSize(QSize(16777215, 241))
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setPixmap(QPixmap("images/cat.png"))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(173, 44))
        self.pushButton_2.setMaximumSize(QSize(173, 44))
        font6 = QFont()
        font6.setFamilies([u"Footlight MT Light"])
        font6.setPointSize(18)
        font6.setKerning(True)
        self.pushButton_2.setFont(font6)
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_2.setStyleSheet(f"""
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
                        }}""")

        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.textBrowser = QTextBrowser(Widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(500,200)
        font4 = QFont()
        font4.setPointSize(14)
        self.textBrowser.setFont(font4)
        self.textBrowser.setStyleSheet(f"""
            QTextBrowser {{
                border-radius: 10px; /* Закругление углов */
                border: 2px solid {border}; /* Цвет границы */
                background-color: {light}; /* Фон */
                color: #000000;
            }}""")

        self.verticalLayout.addWidget(self.textBrowser)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox = QCheckBox(Widget)
        font6 = QFont()
        font6.setFamilies([u"Footlight MT Light"])
        font6.setPointSize(18)
        font6.setKerning(True)
        self.checkBox.setFont(font6)
        self.checkBox.setLayoutDirection(Qt.LeftToRight)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(f"""
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
                        }}""")
        self.checkBox.setText(QCoreApplication.translate("Widget", u"Темная тема", None))
        self.horizontalLayout.addWidget(self.checkBox)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(173, 44))
        self.pushButton.setMaximumSize(QSize(173, 44))
        font6 = QFont()
        font6.setFamilies([u"Footlight MT Light"])
        font6.setPointSize(18)
        font6.setKerning(True)
        self.pushButton.setFont(font6)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setStyleSheet(f"""
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
                        }}""")

        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Welcome to application", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Widget", "Выберите язык разметки", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Widget", "Обычный", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Widget", "HTML", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Widget", "Markdown", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", "@Ссылки", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget", "Telegram", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Widget", "Vk", None))

        self.label_4.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Widget", "Выбрать файл", None))
        self.checkBox.setText(QCoreApplication.translate("Widget", "Светлая тема", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", "Начать", None))
    # retranslateUi

