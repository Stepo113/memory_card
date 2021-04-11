from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import (QApplication,QWidget,
QHBoxLayout,QVBoxLayout,
QGroupBox,QRadioButton,
QPushButton,QLabel,QButtonGroup)

app = QApplication([])

window = QWidget()

window.setWindowTitle('mem card')

btn_ok = QPushButton('ответить')
lb_Question = QLabel('тестовый вопрос')
lb_Result = QLabel('прав\неправ')
lb_Correct = QLabel('здесь будет правильный ответ')
radioGroupBox = QGroupBox('варианты ответа')
ansGroupBox = QGroupBox('результат:')
rbtn1 = QRadioButton('вариант 1')
rbtn2 = QRadioButton('вариант 2')
rbtn3 = QRadioButton('вариант 3')
rbtn4 = QRadioButton('вариант 4')

l_a1 = QHBoxLayout()
l_a2 = QVBoxLayout()
l_a3 = QVBoxLayout()

l_a2.addWidget(rbtn1)
l_a2.addWidget(rbtn2)
l_a3.addWidget(rbtn3)
l_a3.addWidget(rbtn4)
l_a1.addLayout(l_a2)
l_a1.addLayout(l_a3)
radioGroupBox.setLayout(l_a1)

res_l = QVBoxLayout()
res_l.addWidget(lb_Result,Qt.AlignLeft|Qt.AlignTop)
res_l.addWidget(lb_Correct,Qt.AlignHCenter)
ansGroupBox.setLayout(res_l)

ansGroupBox.hide()

line_1 = QHBoxLayout()
line_2 = QHBoxLayout()
line_3 = QHBoxLayout()

line_1.addWidget(lb_Question, \
    alignment=(Qt.AlignHCenter|Qt.AlignVCenter))
line_2.addWidget(radioGroupBox)
line_2.addWidget(ansGroupBox)
line_3.addWidget(btn_ok)

l_main = QVBoxLayout()

l_main.addLayout(line_1)
l_main.addLayout(line_2)
l_main.addLayout(line_3)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

class Question():

    def __init__(self,quest,right_ans,w1,w2,w3):
        self.question = quest
        self.right_ans = right_ans
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3

def show_quest():
    ansGroupBox.hide()
    radioGroupBox.show()
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
    btn_ok.setText('Ответить')

def show_result():
    ansGroupBox.show()
    radioGroupBox.hide()
    btn_ok.setText('Следующий вопрос')

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.w1)
    answers[2].setText(q.w2)
    answers[3].setText(q.w3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_ans)
    show_quest()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_ans():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        show_correct('Неверно!')

def next_quest():
    global cur_quest
    cur_quest += 1
    if cur_quest >= len(question_list):
        cur_quest = 0
    q = question_list[cur_quest]
    ask(q)

question_list = []
cur_quest = 0
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
question_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
question_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))

def click_ok():
    if btn_ok.text() == 'Ответить':
        check_ans()
    else:
        next_quest()

ask(question_list[cur_quest])
window.setLayout(l_main)
window.show()

btn_ok.clicked.connect(click_ok)

app.exec()

