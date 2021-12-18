# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testpage/testpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TestWindow(object):
    def setupUi(self, TestWindow):
        TestWindow.setObjectName("TestWindow")
        TestWindow.setEnabled(True)
        TestWindow.resize(1231, 902)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TestWindow.sizePolicy().hasHeightForWidth())
        TestWindow.setSizePolicy(sizePolicy)
        TestWindow.setMinimumSize(QtCore.QSize(1000, 700))
        TestWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        TestWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        TestWindow.setAutoFillBackground(False)
        TestWindow.setStyleSheet("background-color: #FFFFFF;\n"
"color: #0A2A49;")
        TestWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(TestWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(1000, 700))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setSizeIncrement(QtCore.QSize(5, 5))
        self.stackedWidget.setBaseSize(QtCore.QSize(0, 0))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_choose_test = QtWidgets.QWidget()
        self.page_choose_test.setMinimumSize(QtCore.QSize(0, 0))
        self.page_choose_test.setStyleSheet("QComboBox {\n"
"     border: 2px solid #3F5E7B;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 30px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #0A2A49;\n"
"    border-radius: 25px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: #0B263B;\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"     background-color: #0A2A49;\n"
" }\n"
"\n"
"QPushButton:disabled {\n"
"     background-color: #1F4971;\n"
"    color: grey;\n"
" }\n"
"")
        self.page_choose_test.setObjectName("page_choose_test")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_choose_test)
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(50)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.spisok_testov = QtWidgets.QComboBox(self.page_choose_test)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spisok_testov.sizePolicy().hasHeightForWidth())
        self.spisok_testov.setSizePolicy(sizePolicy)
        self.spisok_testov.setMinimumSize(QtCore.QSize(600, 40))
        self.spisok_testov.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spisok_testov.setBaseSize(QtCore.QSize(0, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(10, 42, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 42, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 42, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 112, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 42, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 42, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 42, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 112, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 42, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 42, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(10, 42, 73))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.spisok_testov.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.spisok_testov.setFont(font)
        self.spisok_testov.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spisok_testov.setAutoFillBackground(False)
        self.spisok_testov.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.spisok_testov.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.spisok_testov.setDuplicatesEnabled(False)
        self.spisok_testov.setFrame(True)
        self.spisok_testov.setModelColumn(0)
        self.spisok_testov.setObjectName("spisok_testov")
        self.verticalLayout_2.addWidget(self.spisok_testov)
        self.spisok_razdelov = QtWidgets.QComboBox(self.page_choose_test)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spisok_razdelov.sizePolicy().hasHeightForWidth())
        self.spisok_razdelov.setSizePolicy(sizePolicy)
        self.spisok_razdelov.setMinimumSize(QtCore.QSize(600, 40))
        self.spisok_razdelov.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.spisok_razdelov.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.spisok_razdelov.setFont(font)
        self.spisok_razdelov.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spisok_razdelov.setStyleSheet("")
        self.spisok_razdelov.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.spisok_razdelov.setIconSize(QtCore.QSize(16, 16))
        self.spisok_razdelov.setDuplicatesEnabled(False)
        self.spisok_razdelov.setFrame(True)
        self.spisok_razdelov.setObjectName("spisok_razdelov")
        self.verticalLayout_2.addWidget(self.spisok_razdelov)
        self.nav_to_page_user_btn = QtWidgets.QPushButton(self.page_choose_test)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nav_to_page_user_btn.sizePolicy().hasHeightForWidth())
        self.nav_to_page_user_btn.setSizePolicy(sizePolicy)
        self.nav_to_page_user_btn.setMinimumSize(QtCore.QSize(400, 60))
        self.nav_to_page_user_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nav_to_page_user_btn.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.nav_to_page_user_btn.setFont(font)
        self.nav_to_page_user_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nav_to_page_user_btn.setFlat(False)
        self.nav_to_page_user_btn.setObjectName("nav_to_page_user_btn")
        self.verticalLayout_2.addWidget(self.nav_to_page_user_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.stackedWidget.addWidget(self.page_choose_test)
        self.page_user = QtWidgets.QWidget()
        self.page_user.setEnabled(True)
        self.page_user.setMinimumSize(QtCore.QSize(0, 0))
        self.page_user.setStyleSheet("QPushButton {\n"
"    background-color: #0A2A49;\n"
"    border-radius: 25px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: #0B263B;\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"     background-color: #0A2A49;\n"
" }\n"
"\n"
"QPushButton:disabled {\n"
"     background-color: #1F4971;\n"
"    color: grey;\n"
" }\n"
"")
        self.page_user.setObjectName("page_user")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_user)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.user_name_input = QtWidgets.QLineEdit(self.page_user)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_name_input.sizePolicy().hasHeightForWidth())
        self.user_name_input.setSizePolicy(sizePolicy)
        self.user_name_input.setMinimumSize(QtCore.QSize(600, 60))
        self.user_name_input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.user_name_input.setFont(font)
        self.user_name_input.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.user_name_input.setStyleSheet("border: 0px;\n"
"border-bottom: 2px solid #0A2A49;")
        self.user_name_input.setAlignment(QtCore.Qt.AlignCenter)
        self.user_name_input.setObjectName("user_name_input")
        self.verticalLayout.addWidget(self.user_name_input)
        self.nav_to_page_choose_test = QtWidgets.QPushButton(self.page_user)
        self.nav_to_page_choose_test.setMinimumSize(QtCore.QSize(600, 60))
        self.nav_to_page_choose_test.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.nav_to_page_choose_test.setFont(font)
        self.nav_to_page_choose_test.setObjectName("nav_to_page_choose_test")
        self.verticalLayout.addWidget(self.nav_to_page_choose_test)
        self.nav_to_page_questions = QtWidgets.QPushButton(self.page_user)
        self.nav_to_page_questions.setMinimumSize(QtCore.QSize(600, 60))
        self.nav_to_page_questions.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.nav_to_page_questions.setFont(font)
        self.nav_to_page_questions.setObjectName("nav_to_page_questions")
        self.verticalLayout.addWidget(self.nav_to_page_questions)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.stackedWidget.addWidget(self.page_user)
        self.page_questions = QtWidgets.QWidget()
        self.page_questions.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_questions.sizePolicy().hasHeightForWidth())
        self.page_questions.setSizePolicy(sizePolicy)
        self.page_questions.setStyleSheet("QPushButton {\n"
"    background-color: #0A2A49;\n"
"    border-radius: 25px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: #0B263B;\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"     background-color: #0A2A49;\n"
" }\n"
"\n"
"QPushButton:disabled {\n"
"     background-color: #1F4971;\n"
"    color: grey;\n"
" }\n"
"")
        self.page_questions.setObjectName("page_questions")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_questions)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(20, 50, 20, 20)
        self.verticalLayout_3.setSpacing(50)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_razdel = QtWidgets.QLabel(self.page_questions)
        self.label_razdel.setMinimumSize(QtCore.QSize(800, 0))
        self.label_razdel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_razdel.setFont(font)
        self.label_razdel.setScaledContents(True)
        self.label_razdel.setAlignment(QtCore.Qt.AlignCenter)
        self.label_razdel.setObjectName("label_razdel")
        self.verticalLayout_3.addWidget(self.label_razdel)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.progress_label = QtWidgets.QLabel(self.page_questions)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.progress_label.setFont(font)
        self.progress_label.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_label.setObjectName("progress_label")
        self.horizontalLayout_8.addWidget(self.progress_label)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_4.setSpacing(25)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_question = QtWidgets.QLabel(self.page_questions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_question.sizePolicy().hasHeightForWidth())
        self.label_question.setSizePolicy(sizePolicy)
        self.label_question.setMinimumSize(QtCore.QSize(300, 0))
        self.label_question.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_question.setFont(font)
        self.label_question.setStyleSheet("color: black;")
        self.label_question.setTextFormat(QtCore.Qt.AutoText)
        self.label_question.setScaledContents(True)
        self.label_question.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_question.setWordWrap(True)
        self.label_question.setObjectName("label_question")
        self.verticalLayout_4.addWidget(self.label_question)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, -1, -1)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.answer_btn = QtWidgets.QPushButton(self.page_questions)
        self.answer_btn.setMinimumSize(QtCore.QSize(300, 60))
        self.answer_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.answer_btn.setFont(font)
        self.answer_btn.setObjectName("answer_btn")
        self.horizontalLayout_5.addWidget(self.answer_btn)
        self.next_question_btn = QtWidgets.QPushButton(self.page_questions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_question_btn.sizePolicy().hasHeightForWidth())
        self.next_question_btn.setSizePolicy(sizePolicy)
        self.next_question_btn.setMinimumSize(QtCore.QSize(300, 60))
        self.next_question_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.next_question_btn.setFont(font)
        self.next_question_btn.setObjectName("next_question_btn")
        self.horizontalLayout_5.addWidget(self.next_question_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem12)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.page_questions)
        self.page_result = QtWidgets.QWidget()
        self.page_result.setEnabled(True)
        self.page_result.setMinimumSize(QtCore.QSize(0, 0))
        self.page_result.setStyleSheet("QPushButton {\n"
"    background-color: #0A2A49;\n"
"    border-radius: 25px;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"     background-color: #0B263B;\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"     background-color: #0A2A49;\n"
" }\n"
"\n"
"QPushButton:disabled {\n"
"     background-color: #1F4971;\n"
"    color: grey;\n"
" }")
        self.page_result.setObjectName("page_result")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_result)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 50, -1, -1)
        self.verticalLayout_5.setSpacing(40)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.result_page_title = QtWidgets.QLabel(self.page_result)
        self.result_page_title.setMinimumSize(QtCore.QSize(900, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.result_page_title.setFont(font)
        self.result_page_title.setStyleSheet("background-color: yellow;\n"
"border-radius: 25px;")
        self.result_page_title.setAlignment(QtCore.Qt.AlignCenter)
        self.result_page_title.setObjectName("result_page_title")
        self.verticalLayout_5.addWidget(self.result_page_title)
        self.line = QtWidgets.QFrame(self.page_result)
        self.line.setStyleSheet("color: #031A2F;")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(10)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setContentsMargins(10, -1, 10, -1)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.res_test_name_title = QtWidgets.QLabel(self.page_result)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res_test_name_title.sizePolicy().hasHeightForWidth())
        self.res_test_name_title.setSizePolicy(sizePolicy)
        self.res_test_name_title.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.res_test_name_title.setFont(font)
        self.res_test_name_title.setObjectName("res_test_name_title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.res_test_name_title)
        self.res_test_name_value = QtWidgets.QLabel(self.page_result)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res_test_name_value.sizePolicy().hasHeightForWidth())
        self.res_test_name_value.setSizePolicy(sizePolicy)
        self.res_test_name_value.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.res_test_name_value.setFont(font)
        self.res_test_name_value.setStyleSheet("")
        self.res_test_name_value.setScaledContents(False)
        self.res_test_name_value.setWordWrap(True)
        self.res_test_name_value.setObjectName("res_test_name_value")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.res_test_name_value)
        self.res_razdel_title = QtWidgets.QLabel(self.page_result)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res_razdel_title.sizePolicy().hasHeightForWidth())
        self.res_razdel_title.setSizePolicy(sizePolicy)
        self.res_razdel_title.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.res_razdel_title.setFont(font)
        self.res_razdel_title.setObjectName("res_razdel_title")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.res_razdel_title)
        self.res_razdel_value = QtWidgets.QLabel(self.page_result)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res_razdel_value.sizePolicy().hasHeightForWidth())
        self.res_razdel_value.setSizePolicy(sizePolicy)
        self.res_razdel_value.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.res_razdel_value.setFont(font)
        self.res_razdel_value.setStyleSheet("")
        self.res_razdel_value.setWordWrap(True)
        self.res_razdel_value.setObjectName("res_razdel_value")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.res_razdel_value)
        self.res_test_count_title = QtWidgets.QLabel(self.page_result)
        self.res_test_count_title.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res_test_count_title.sizePolicy().hasHeightForWidth())
        self.res_test_count_title.setSizePolicy(sizePolicy)
        self.res_test_count_title.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.res_test_count_title.setFont(font)
        self.res_test_count_title.setObjectName("res_test_count_title")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.res_test_count_title)
        self.res_test_count_value = QtWidgets.QLabel(self.page_result)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res_test_count_value.sizePolicy().hasHeightForWidth())
        self.res_test_count_value.setSizePolicy(sizePolicy)
        self.res_test_count_value.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.res_test_count_value.setFont(font)
        self.res_test_count_value.setStyleSheet("")
        self.res_test_count_value.setObjectName("res_test_count_value")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.res_test_count_value)
        self.res_correct_answers_count_title = QtWidgets.QLabel(self.page_result)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res_correct_answers_count_title.sizePolicy().hasHeightForWidth())
        self.res_correct_answers_count_title.setSizePolicy(sizePolicy)
        self.res_correct_answers_count_title.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.res_correct_answers_count_title.setFont(font)
        self.res_correct_answers_count_title.setObjectName("res_correct_answers_count_title")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.res_correct_answers_count_title)
        self.res_correct_answers_count_value = QtWidgets.QLabel(self.page_result)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res_correct_answers_count_value.sizePolicy().hasHeightForWidth())
        self.res_correct_answers_count_value.setSizePolicy(sizePolicy)
        self.res_correct_answers_count_value.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.res_correct_answers_count_value.setFont(font)
        self.res_correct_answers_count_value.setStyleSheet("")
        self.res_correct_answers_count_value.setObjectName("res_correct_answers_count_value")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.res_correct_answers_count_value)
        self.res_percentage_of_correct_answers_title = QtWidgets.QLabel(self.page_result)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res_percentage_of_correct_answers_title.sizePolicy().hasHeightForWidth())
        self.res_percentage_of_correct_answers_title.setSizePolicy(sizePolicy)
        self.res_percentage_of_correct_answers_title.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.res_percentage_of_correct_answers_title.setFont(font)
        self.res_percentage_of_correct_answers_title.setObjectName("res_percentage_of_correct_answers_title")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.res_percentage_of_correct_answers_title)
        self.res_percentage_of_correct_answers_value = QtWidgets.QLabel(self.page_result)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res_percentage_of_correct_answers_value.sizePolicy().hasHeightForWidth())
        self.res_percentage_of_correct_answers_value.setSizePolicy(sizePolicy)
        self.res_percentage_of_correct_answers_value.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.res_percentage_of_correct_answers_value.setFont(font)
        self.res_percentage_of_correct_answers_value.setStyleSheet("")
        self.res_percentage_of_correct_answers_value.setObjectName("res_percentage_of_correct_answers_value")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.res_percentage_of_correct_answers_value)
        self.verticalLayout_5.addLayout(self.formLayout)
        self.line_2 = QtWidgets.QFrame(self.page_result)
        self.line_2.setStyleSheet("color: #031A2F;")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(10)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.test_window_close_btn = QtWidgets.QPushButton(self.page_result)
        self.test_window_close_btn.setMinimumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.test_window_close_btn.setFont(font)
        self.test_window_close_btn.setObjectName("test_window_close_btn")
        self.horizontalLayout_7.addWidget(self.test_window_close_btn)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem15)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem16)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem17)
        self.stackedWidget.addWidget(self.page_result)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem18)
        TestWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TestWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(TestWindow)

    def retranslateUi(self, TestWindow):
        _translate = QtCore.QCoreApplication.translate
        TestWindow.setWindowTitle(_translate("TestWindow", "Прохождение теста"))
        self.nav_to_page_user_btn.setText(_translate("TestWindow", "ДАЛЕЕ"))
        self.user_name_input.setPlaceholderText(_translate("TestWindow", "Введите ваше имя"))
        self.nav_to_page_choose_test.setText(_translate("TestWindow", "НАЗАД"))
        self.nav_to_page_questions.setText(_translate("TestWindow", "ДАЛЕЕ"))
        self.label_razdel.setText(_translate("TestWindow", "Раздел"))
        self.progress_label.setText(_translate("TestWindow", "Вопрос 1/100"))
        self.label_question.setText(_translate("TestWindow", "Текст вопроса"))
        self.answer_btn.setText(_translate("TestWindow", "ОТВЕТИТЬ"))
        self.next_question_btn.setText(_translate("TestWindow", "СЛЕДУЮЩИЙ"))
        self.result_page_title.setText(_translate("TestWindow", "ВАШ РЕЗУЛЬТАТ"))
        self.res_test_name_title.setText(_translate("TestWindow", "Наименование теста"))
        self.res_test_name_value.setText(_translate("TestWindow", "Lorem Ipsum"))
        self.res_razdel_title.setText(_translate("TestWindow", "Раздел теста"))
        self.res_razdel_value.setText(_translate("TestWindow", "Lorem Ipsum 1"))
        self.res_test_count_title.setText(_translate("TestWindow", "Количество вопросов"))
        self.res_test_count_value.setText(_translate("TestWindow", "0"))
        self.res_correct_answers_count_title.setText(_translate("TestWindow", "Правильные ответы"))
        self.res_correct_answers_count_value.setText(_translate("TestWindow", "0"))
        self.res_percentage_of_correct_answers_title.setText(_translate("TestWindow", "Процент правильных ответов"))
        self.res_percentage_of_correct_answers_value.setText(_translate("TestWindow", "53"))
        self.test_window_close_btn.setText(_translate("TestWindow", "ЗАКРЫТЬ"))