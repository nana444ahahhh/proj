# посхалка активируется если много раз нажимать на подождать и возвращаться обратно на первой странице
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt

l = [[100, "меч"], [100, "сильный меч"]]
import sqlite3

con = sqlite3.connect("shop.sqlite3")
cur = con.cursor()
cur.execute(f"""DROP TABLE IF EXISTS shoap;""")
cur.execute(f"""CREATE TABLE shoap('cost', 'item')""")
for i in range(len(l)):
    cur.execute(f"""INSERT INTO shoap("cost","item") VALUES{tuple(l[i])}""")


class focuss(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.p2 = False
        self.p = 0
        self.c1 = 0
        self.hp = 3
        self.setGeometry(100, 200, 500, 500)
        self.pixmap = QPixmap('jail.jpeg')
        self.image = QLabel(self)
        self.image.resize(700, 700)
        self.image.setPixmap(self.pixmap)
        self.t = "Вы очнулись на грязном полу в темнице." + "\n" + "Вас кажется заточил сюда темный повелитель"
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.black)
        self.setPalette(palette)
        self.b = QLabel(self)
        self.b.setText(self.t)
        self.b.setStyleSheet('color: rgb(255, 255, 255);')
        self.b.move(30, 450)
        self.m = 0
        self.coins = QLabel(self)
        self.lives = QLabel(self)
        self.coins.setText(f'''<font color="red">монеты:{self.m} <Текст</font><br>''')
        self.lives.setText(f'''<font color="red">жизни:{self.hp} <Текст</font><br>''')
        self.lives.move(200, 0)

        self.coins.move(0, 0)
        self.weapon = QLabel(self)
        self.weapon.move(300, 0)
        self.w = "нет"
        self.weapon.setText(f'''<font color="red">оружие:{self.w} <Текст</font><br>''')

        self.bt = QPushButton("встать и оглядеться", self)
        self.bt.resize(200, 50)
        self.bt.move(60, 350)

        self.b2 = QPushButton(self)
        self.b2.resize(200, 50)
        self.b2.move(60, 400)
        self.b2.hide()

        self.b3 = QPushButton("подождать", self)
        self.b3.resize(200, 50)
        self.b3.move(60, 400)

        self.bt.clicked.connect(self.key)
        self.b3.clicked.connect(self.nt)
        self.hint = QLabel(self)
        self.h = "нет"
        self.hint.setText(f'''<font color="red">подсказка:{self.h} <Текст</font><br>''')
        self.hint.move(0, 50)

    def key(self):
        self.pixmap = QPixmap('Без имени-2.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, -100)
        self.b3.hide()
        self.b2.show()
        self.b.setText("поздравляю, вы нашли ключ от двери!")
        self.b.setStyleSheet('color: rgb(255, 255,255 );')
        self.bt.hide()
        self.b2.setText("попытаться открыть дверь")
        self.b2.resize(self.b2.sizeHint())
        self.b2.clicked.connect(self.door)
        self.b2.show()

    def door(self):
        self.bt.show()
        self.b2.show()
        self.pixmap = QPixmap('karitar.jpg')
        self.image.move(0, 0)
        self.image.setPixmap(self.pixmap)
        self.image.resize(500, 500)
        self.b.setText("Корридор.Темный.")
        self.b.setStyleSheet('color: rgb(200, 100,100 );')
        self.bt.show()
        self.bt.setText("оглядеться")
        self.bt.clicked.connect(self.osmotr)
        self.b2.setText("пройти вперед")
        self.b2.clicked.connect(self.ga)
        self.b2.resize(200, 50)

    def ga(self):
        self.pixmap = QPixmap('A4.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b.setText('''<font color="green">вы нашли записку!<Текст</font><br>''')
        self.bt.show()
        self.bt.setText("прочитать")
        self.bt.clicked.connect(self.read)
        self.b2.hide()

    def read(self):
        self.pixmap = QPixmap('message.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, -5)
        self.b.setText('''<font color="green">Вероятно вам её написало мудрое магическое древо<Текст</font><br>''')
        self.bt.show()
        self.bt.setText("продолжить путь ")

        self.bt.clicked.connect(self.forest)
        self.b2.hide()

    def forest(self):
        self.pixmap = QPixmap('forrest.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b2.show()
        self.b2.setText("осмотреться")
        self.bt.hide()
        self.b2.clicked.connect(self.osmotrhouse)

    def osmotrhouse(self):
        self.pixmap = QPixmap('dom.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b.setText('''<font color="green">в дереве стоит дом, следует туда зайти <Текст</font><br>''')
        self.bt.show()
        self.b2.hide()
        self.bt.setText("Зайти")
        self.bt.clicked.connect(self.trader)

    def trader(self):
        self.bt.show()
        self.b2.show()
        self.pixmap = QPixmap('torgash.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.coins.setText(f'''<font color="red">монеты:100 <Текст</font><br>''')
        self.coins.resize(self.coins.sizeHint())
        t2 = "По пути вы нашли 100 монет, в доме был торговец"
        self.b.setText(t2)
        self.b.setStyleSheet('color: rgb(255, 255, 255);')
        self.b2.setText("Купить меч(100)(1 урон)")
        self.bt.setText("уйти(0)")
        self.bt.resize(200, 50)
        self.bt.clicked.connect(self.goaway)
        self.b2.clicked.connect(self.sword)

    def sword(self):
        self.mc = 1
        self.w = cur.execute("""select * from shoap
        where item == "меч"  """).fetchall()
        self.w = list(*self.w)[1]
        self.pixmap = QPixmap('Mech_bronzovogo_veka.jpg')
        self.image.setPixmap(self.pixmap)
        self.coins.setText(f'''<font color="red">монеты:0 <Текст</font><br>''')
        self.b.setText('''<font color="white">хороший,увесистый меч!<Текст</font><br>''')
        self.b2.show()
        self.b2.setText("дальше")
        self.b2.clicked.connect(self.drevo)
        self.weapon.setText(f'''<font color="red">оружие:{self.w} <Текст</font><br>''')
        self.weapon.resize(self.weapon.sizeHint())

    def goaway(self):
        self.mc = 0
        self.pixmap = QPixmap('forrest.jpg')
        self.image.setPixmap(self.pixmap)
        self.bt.show()
        self.bt.setText("идти дальше")
        self.b2.hide()
        self.b.setText("вы вышли")
        self.bt.clicked.connect(self.drevo1)

    def drevo1(self):
        self.pixmap = QPixmap('drevo.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b2.show()
        self.b.setText('''<font color="white">Пред вами взошло мудрейшее древо!<Текст</font><br>''')
        self.bt.hide()
        self.b2.setText("попросить совета")
        self.b2.clicked.connect(self.ussr1)

    def drevo(self):
        self.pixmap = QPixmap('drevo.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b2.show()
        self.b.setText('''<font color="white">Пред вами взошло мудрейшее древо!<Текст</font><br>''')
        self.bt.hide()
        self.b2.setText("попросить совета")
        self.b2.clicked.connect(self.ussr)

    def ussr1(self):
        self.m = 100
        self.coins.setText(f'''<font color="red">монеты:{self.m} <Текст</font><br>''')
        self.w = "нет"
        self.weapon.setText(f'''<font color="red">оружие:{self.w} <Текст</font><br>''')

        self.pixmap = QPixmap('dark_chel.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b.setText(
            f'''<font color="white">Si kënnen eng Waff gläichzäiteg droen<Текст</font><br>''')
        self.h = "это люксембургский язык, попробуйте перевести!"

        self.hint.setText(f'''<font color="red">подсказка:{self.h} <Текст</font><br>''')
        self.hint.resize(self.hint.sizeHint())

        self.b2.setText("отправиться дальше")
        self.b2.clicked.connect(self.mmm)
        self.b2.show()
        self.bt.hide()

    def ussr(self):

        self.pixmap = QPixmap('dark_chel.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b.setText(
            f'''<font color="white">Si kënnen eng Waff gläichzäiteg droen<Текст</font><br>''')
        self.h = "это люксембургский язык, попробуйте перевести!"

        self.hint.setText(f'''<font color="red">подсказка:{self.h} <Текст</font><br>''')
        self.hint.resize(self.hint.sizeHint())

        self.b2.setText("отправиться дальше")
        self.b2.clicked.connect(self.mmm)
        self.b2.show()
        self.bt.hide()

    def mmm(self):
        self.h = "нет"
        self.hint.setText(f'''<font color="red">подсказка:{self.h} <Текст</font><br>''')
        self.hint.resize(self.hint.sizeHint())
        self.pixmap = QPixmap('monitor.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b.setText('''<font color="red">перед вами враждебное существо(1 урон 1 жизнь)<Текст</font><br>''')
        self.bt.show()
        self.bt.resize(200, 50)
        self.b2.show()
        if self.w != "нет":
            self.bt.setText("убить(меч сломается)")
            self.b2.setText("ничего не делать")
            self.b2.resize(200, 50)
            self.b2.clicked.connect(self.hitted)
            self.bt.clicked.connect(self.hit)
        else:
            self.bt.hide()
            self.b2.setText("ничего не делать")
            self.b2.resize(200, 50)
            self.b2.clicked.connect(self.hitted1)

    def hit(self):
        # вы ударили
        self.m = 0
        self.coins.setText(f'''<font color="red">монеты:{self.m} <Текст</font><br>''')
        self.pixmap = QPixmap('Monsters_Werewolf_Blood_Dead_Cadaver_Corpse_524013_2500x1786.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b.setText("вы убили существо")
        self.w = "нет"
        self.weapon.setText(f'''<font color="red">оружие:{self.w} <Текст</font><br>''')

        self.bt.show()
        self.b2.hide()
        self.bt.setText("продплжить путь")
        self.bt.clicked.connect(self.through)

    def hitted(self):
        # вас ударили когда вы с мечом
        self.w = cur.execute("""select * from shoap
               where item == "меч"  """).fetchall()
        self.w = list(*self.w)[1]
        self.weapon.setText(f'''<font color="red">оружие:{self.w} <Текст</font><br>''')
        self.pixmap = QPixmap('king_.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.hp = 2
        self.lives.setText(f'''<font color="red">жизни:{self.hp} <Текст</font><br>''')
        self.b.setText("существо вас ударило и ушло")
        self.bt.show()
        self.b2.hide()
        self.bt.setText("продплжить путь")
        self.bt.clicked.connect(self.through2)

    def hitted1(self):
        # вас ударили без меча
        self.h = "нет"
        self.hint.setText(f'''<font color="red">подсказка:{self.h} <Текст</font><br>''')
        self.hint.resize(self.hint.sizeHint())
        self.pixmap = QPixmap('king_.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.hp = 2
        self.lives.setText(f'''<font color="red">жизни:{self.hp} <Текст</font><br>''')
        self.b.setText("существо вас ударило и ушло")
        self.bt.show()
        self.b2.hide()
        self.bt.setText("продплжить путь")
        self.bt.clicked.connect(self.through1)

    def through(self):
        # после того как вы ударили
        self.m = 0
        self.coins.setText(f'''<font color="red">монеты:{self.m} <Текст</font><br>''')
        self.w = "нет"
        self.weapon.setText(f'''<font color="red">оружие:{self.w} <Текст</font><br>''')
        self.pixmap = QPixmap('main_trader.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.bt.show()
        self.b2.show()
        self.bt.setText("сильный меч(100)(3 урон)")
        self.b2.setText("уйти(0)")
        self.b.setText("это какой-то необычный торговец")
        self.bt.resize(200, 50)
        self.bt.clicked.connect(self.no_buy)
        self.b2.clicked.connect(self.goawaym)

    def goawaym(self):
        # после удара
        self.hp = 3
        self.lives.setText(f'''<font color="red">жизни:{self.hp} <Текст</font><br>''')
        self.m = 0
        self.coins.setText(f'''<font color="red">монеты:{self.m} <Текст</font><br>''')
        self.h = "нет"
        self.hint.setText(f'''<font color="red">подсказка:{self.h} <Текст</font><br>''')
        self.pixmap = QPixmap('1625629689_5-phonoteka-org-p-mag-art-krasivo-7.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b.setText(
            '''<font color="red">вы будете сражаться с повелителем!(2 жизней, 3 урона)<Текст</font><br>''')
        self.bt.setText("сдаться")
        if self.p2 == True:
            self.bt.clicked.connect(self.joke)

        else:
            self.bt.clicked.connect(self.bad)
        self.b2.hide()
        self.bt.show()

    def goawaym1(self):
        # после бездействия с мечом
        self.m = 0
        self.coins.setText(f'''<font color="red">монеты:{self.m} <Текст</font><br>''')
        self.hp = 2
        self.lives.setText(f'''<font color="red">жизни:{self.hp} <Текст</font><br>''')
        self.h = "нет"
        self.hint.setText(f'''<font color="red">подсказка:{self.h} <Текст</font><br>''')
        self.pixmap = QPixmap('1625629689_5-phonoteka-org-p-mag-art-krasivo-7.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b.setText(
            '''<font color="red">вы будете сражаться с повелителем!(2 жизней, 3 урона)<Текст</font><br>''')
        self.w = cur.execute("""select * from shoap
                      where item == "меч"  """).fetchall()
        self.w = list(*self.w)[1]
        self.weapon.setText(f'''<font color="red">оружие:{self.w} <Текст</font><br>''')
        self.bt.setText("ударить")
        self.b2.setText("сдаться")
        if self.p2 == True:
            self.bt.clicked.connect(self.joke)
            self.b2.clicked.connect(self.joke)
        else:
            self.b2.clicked.connect(self.surrender)
            self.bt.clicked.connect(self.bad)
        self.bt.show()

    def bad(self):
        self.pixmap = QPixmap('dead.jpg')
        self.image.setPixmap(self.pixmap)
        self.b.setText(
            '''<font color="white">вы были убиты повелителем<Текст</font><br>''')
        self.bt.hide()
        self.b2.hide()
        self.weapon.setText("")
        self.coins.setText("")
        self.hint.setText("")
        self.lives.setText("")

    def goawaym3(self):
        # после бездействия и покупки
        self.w = cur.execute("""select * from shoap
                      where item == "сильный меч"  """).fetchall()
        self.w = list(*self.w)[1]
        self.weapon.setText(f'''<font color="red">оружие:{self.w} <Текст</font><br>''')
        self.m = 0
        self.weapon.resize(self.weapon.sizeHint())
        self.coins.setText(f'''<font color="red">монеты:{self.m} <Текст</font><br>''')
        self.hp = 2
        self.lives.setText(f'''<font color="red">жизни:{self.hp} <Текст</font><br>''')
        self.h = "нет"
        self.hint.setText(f'''<font color="red">подсказка:{self.h} <Текст</font><br>''')
        self.pixmap = QPixmap('1625629689_5-phonoteka-org-p-mag-art-krasivo-7.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b.setText(
            '''<font color="red">вы будете сражаться с повелителем!(2 жизней, 3 урона)<Текст</font><br>''')
        self.bt.setText("ударить")
        self.bt.show()
        self.bt.clicked.connect(self.win)
        self.b2.setText("сдаться")
        if self.p2 == True:
            self.b2.clicked.connect(self.joke)
            self.bt.clicked.connect(self.joke)
        else:
            self.b2.clicked.connect(self.surrender)

    def win(self):
        self.pixmap = QPixmap('duty.jpg')
        self.image.setPixmap(self.pixmap)
        self.b.setText(
            '''<font color="white">вы выполнили свой долг и победили повелителя <Текст</font><br>''')
        self.bt.hide()
        self.b2.hide()
        self.weapon.setText("")
        self.coins.setText("")
        self.hint.setText("")
        self.lives.setText("")

    def goawaym4(self):

        # после бездействия и ухода
        self.m = 100
        self.coins.setText(f'''<font color="red">монеты:{self.m} <Текст</font><br>''')
        self.w = "нет"
        self.weapon.setText(f'''<font color="red">оружие:{self.w} <Текст</font><br>''')
        self.hp = 2
        self.lives.setText(f'''<font color="red">жизни:{self.hp} <Текст</font><br>''')
        self.h = "нет"
        self.hint.setText(f'''<font color="red">подсказка:{self.h} <Текст</font><br>''')
        self.pixmap = QPixmap('1625629689_5-phonoteka-org-p-mag-art-krasivo-7.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b.setText(
            '''<font color="red">вы будете сражаться с повелителем!(2 жизней, 3 урона)<Текст</font><br>''')
        self.bt.setText("сдаться")
        self.bt.show()
        self.b2.hide()
        if self.p2 == True:
            self.bt.clicked.connect(self.joke)
        else:
            self.bt.clicked.connect(self.surrender)

    def joke(self):
        self.pixmap = QPixmap('medding.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b.setText('''<font color="white">Повелитель превратился в мясо и вы его съели<Текст</font><br>''')
        self.bt.hide()
        self.b2.hide()
        self.weapon.hide()
        self.hint.hide()
        self.coins.hide()

    def surrender(self):
        self.pixmap = QPixmap('solod.jpg')
        self.image.setPixmap(self.pixmap)
        self.b.setText(
            '''<font color="white">вы стали рабом повелителя<Текст</font><br>''')
        self.bt.hide()
        self.b2.hide()
        self.weapon.setText("")
        self.coins.setText("")
        self.hint.setText("")
        self.lives.setText("")

    def through2(self):
        # после получения удара с мечом
        self.w = self.w = cur.execute("""select * from shoap
               where item == "меч"  """).fetchall()
        self.w = list(*self.w)[1]
        self.weapon.setText(f'''<font color="red">оружие:{self.w} <Текст</font><br>''')
        self.pixmap = QPixmap('main_trader.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.bt.show()
        self.b2.show()

        self.bt.setText("сильный меч(100)")
        self.b2.setText("уйти(0)")
        self.b.setText("это какой-то необычный торговец")
        self.bt.resize(200, 50)

        self.bt.clicked.connect(self.no_buy1)
        self.m = 0
        self.coins.setText(f'''<font color="red">монеты:{self.m} <Текст</font><br>''')
        self.b2.clicked.connect(self.goawaym1)

    def buy1(self):

        self.pixmap = QPixmap('main_trader.jpg')
        self.image.setPixmap(self.pixmap)
        self.b.setText('''<font color="green">куплено<Текст</font><br>''')

        self.w = self.w = cur.execute("""select * from shoap
               where item == "сильный меч"  """).fetchall()
        self.w = list(*self.w)[1]
        self.weapon.setText(f'''<font color="red">оружие:{self.w} <Текст</font><br>''')
        self.b.setText('''<font color="green">куплено<Текст</font><br>''')
        self.m = 0
        self.weapon.resize(self.weapon.sizeHint())
        self.coins.setText(f'''<font color="red">монеты:{self.m} <Текст</font><br>''')
        self.b2.hide()
        self.bt.clicked.connect(self.goawaym3)
        self.bt.show()

    def buy(self):

        self.pixmap = QPixmap('main_trader.jpg')
        self.image.setPixmap(self.pixmap)
        self.b.setText('''<font color="green">куплено<Текст</font><br>''')
        if self.m >= 100:
            self.w = self.w = cur.execute("""select * from shoap
               where item == "сильный меч"  """).fetchall()
            self.w = list(*self.w)[1]
            self.weapon.setText(f'''<font color="red">оружие:{self.w} <Текст</font><br>''')
            self.b.setText('''<font color="green">куплено<Текст</font><br>''')
            self.m = 0
            self.coins.setText(f'''<font color="red">монеты:{self.m} <Текст</font><br>''')
        else:
            self.b.setText('''<font color="red">не хватает денег<Текст</font><br>''')

        self.weapon.resize(self.weapon.sizeHint())
        self.bt.hide()
        self.b2.setText("уйти(0)")
        self.b2.clicked.connect(self.goawaym)

    def through1(self):
        # после безоружия
        self.pixmap = QPixmap('main_trader.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.move(0, 0)
        self.b.setText("это какой-то необычный торговец")
        self.bt.show()
        self.b2.show()
        self.bt.setText("сильный меч(100)(3урона)")
        self.bt.resize(200, 50)
        self.b2.setText("уйти(0)")
        self.bt.clicked.connect(self.buy1)
        self.b2.clicked.connect(self.goawaym4)

    def no_buy(self):
        # невозможность покупки из-за  монет
        self.pixmap = QPixmap('main_trader.jpg')
        self.image.setPixmap(self.pixmap)
        self.b.setText('''<font color="red">у вас нет денег(<Текст</font><br>''')
        self.bt.hide()
        self.b2.setText("уйти(0)")
        self.b2.clicked.connect(self.goawaym)

    def no_buy1(self):
        # неозможность покупки из-за меча и монет
        self.pixmap = QPixmap('main_trader.jpg')
        self.image.setPixmap(self.pixmap)
        self.w = self.w = cur.execute("""select * from shoap
                       where item == "меч"  """).fetchall()
        self.w = list(*self.w)[1]
        self.weapon.setText(f'''<font color="red">оружие:{self.w} <Текст</font><br>''')
        self.b.setText('''<font color="red">у вас уже есть оружие(<Текст</font><br>''')
        self.bt.hide()
        self.b2.setText("уйти(0)")
        self.b2.clicked.connect(self.goawaym1)

    def door2(self):
        self.pixmap = QPixmap('karitar.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.resize(500, 500)
        self.b.setText("Корридор.Темный.")
        self.b.setStyleSheet('color: rgb(200, 100,100 );')
        self.b2.setText("пройти вперед")
        self.b2.clicked.connect(self.ga)
        self.b2.resize(200, 50)
        self.bt.hide()

    def osmotr(self):
        self.pixmap = QPixmap('karitar.jpg')
        self.image.move(0, 0)
        self.image.setPixmap(self.pixmap)
        self.b.setText("тут холодно и страшно, кажется лучше не стоять на месте")
        self.b.resize(self.b.sizeHint())
        self.b.setStyleSheet('color: rgb(255, 100,100 );')
        self.b2.setText("обратно к путешествию")
        self.b2.resize(self.b2.sizeHint())
        self.b2.clicked.connect(self.door2)
        self.b2.resize(200, 50)
        self.c1 += 1

    def nt(self):
        if self.p < 10:
            self.p += 1
            self.bt.hide()
            self.b.setText(
                '''<font color="white">Хммм...Вы так и будете ждать?<Текст</font><br>''')
            self.b3.setText("Может все-таки начнем наши подвиги?")
            self.b3.resize(self.b3.sizeHint())
            self.b3.clicked.connect(self.back)
        else:
            self.pixmap = QPixmap('eggas.jpg')
            self.image.move(0, 0)
            self.image.setPixmap(self.pixmap)
            self.image.move(0, -100)
            self.b.setText('''<font color="red">Пасхалка! Но смысл откроется потом<Текст</font><br>''')
            self.b3.hide()
            self.p2 = True

    def back(self):
        if self.p2 != True:

            self.bt.show()
            self.b3.setText("подождать")
            self.b3.resize(200, 50)
            self.b3.clicked.connect(self.nt)
            self.b.setText(
                '''<font color="white">Вы ведь собираетесь попытаться выйти отсюда?<Текст</font><br>''')
        else:
            self.pixmap = QPixmap('eggas.jpg')
            self.image.move(0, 0)
            self.image.setPixmap(self.pixmap)
            self.image.move(0, -100)
            self.b.setText('''<font color="red">Пасхалка! Но смысл откроется потом<Текст</font><br>''')
            self.bt.show()
            self.b3.hide()
            self.p2 = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = focuss()
    ex.show()
    sys.exit(app.exec())
