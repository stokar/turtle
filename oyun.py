import turtle
import random

# Ayarlar
SURE = 30
HIZ = 10
GENISLIK = 800
YUKSEKLIK = 800

# Ekran
ekran = turtle.Screen()
ekran.title("Kaplumbağayı Yakala!")
ekran.bgcolor("lightblue")
ekran.setup(GENISLIK, YUKSEKLIK)
ekran.tracer(0)

# Oyun değişkenleri
skor = 0
kalan_sure = SURE
oyun_bitti = False

# Hedef kaplumbağa
kaplumbaga = turtle.Turtle()
kaplumbaga.shape("turtle")
kaplumbaga.color("darkgreen")
kaplumbaga.shapesize(2, 2)
kaplumbaga.penup()

# Yazı yazan kaplumbağa (skor ve süre)
yazici = turtle.Turtle()
yazici.hideturtle()
yazici.penup()

# Çıkış butonu
buton = turtle.Turtle()
buton.shape("square")
buton.shapesize(2, 5) 
buton.color("black", "red")
buton.penup()
BUTON_X = GENISLIK / 2 - 70
BUTON_Y = -YUKSEKLIK / 2 + 40
buton.goto(BUTON_X, BUTON_Y)

buton_yazi = turtle.Turtle()
buton_yazi.hideturtle()
buton_yazi.penup()
buton_yazi.color("white")
buton_yazi.goto(BUTON_X, BUTON_Y - 10)
buton_yazi.write("ÇIKIŞ", align="center", font=("Arial", 14, "bold"))


def yazilari_guncelle():
    yazici.clear()
    yazici.goto(-GENISLIK / 2 + 20, YUKSEKLIK / 2 - 50)
    yazici.color("black")
    yazici.write(f"Yakalanan: {skor}", font=("Arial", 18, "bold"))
    yazici.goto(GENISLIK / 2 - 20, YUKSEKLIK / 2 - 50)
    yazici.write(f"Süre: {kalan_sure}", align="right", font=("Arial", 18, "bold"))


def rastgele_yon():
    kaplumbaga.setheading(random.randint(0, 359))


def hareket_et():
    if oyun_bitti:
        return
    kaplumbaga.forward(HIZ)

    # Duvara çarparsa geri dön
    sinir_x = GENISLIK / 2 - 30
    sinir_y = YUKSEKLIK / 2 - 80
    if abs(kaplumbaga.xcor()) > sinir_x or abs(kaplumbaga.ycor()) > sinir_y:
        kaplumbaga.goto(
            max(-sinir_x, min(sinir_x, kaplumbaga.xcor())),
            max(-sinir_y, min(sinir_y, kaplumbaga.ycor())),
        )
        kaplumbaga.setheading(kaplumbaga.heading() + 180 + random.randint(-60, 60))

    # Ara sıra yön değiştir
    if random.random() < 0.1:
        rastgele_yon()

    ekran.update()
    ekran.ontimer(hareket_et, 40)


def sure_say():
    global kalan_sure
    if oyun_bitti:
        return
    kalan_sure -= 1
    yazilari_guncelle()
    if kalan_sure <= 0:
        oyunu_bitir()
    else:
        ekran.ontimer(sure_say, 1000)


def oyunu_bitir():
    global oyun_bitti
    oyun_bitti = True
    kaplumbaga.hideturtle()
    yazici.goto(0, 0)
    yazici.color("darkred")
    yazici.write(f"OYUN BİTTİ!\nSkorun: {skor}", align="center",
                 font=("Arial", 28, "bold"))
    ekran.update()


def yakala(x, y):
    global skor
    if oyun_bitti:
        return
    skor += 1
    yazilari_guncelle()
    # Yakalanınca rastgele yere ışınlan
    kaplumbaga.goto(random.randint(-250, 250), random.randint(-200, 200))
    rastgele_yon()


def cikis(x, y):
    ekran.bye()


# Başlat
yazilari_guncelle()
rastgele_yon()
kaplumbaga.onclick(yakala)
buton.onclick(cikis)
ekran.update()

hareket_et()
ekran.ontimer(sure_say, 1000)

ekran.mainloop()
