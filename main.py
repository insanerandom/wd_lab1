import math
import string

print("Zad1")
a = 0
a1 = 3
a2 = 4
b1 = "hello"
b2 = "world"
c1 = 3.14
c2 = 1.618
d1 = 3 + 2j
d2 = 6 + 3j
print("integers: %(a1)d, %(a2)d" % {'a1': a1, 'a2': a2})
print("strings: " + b1 + " " + b2)
print("floats: ", c1, c2)
print("complex: ", d1, d2)
# print("\nZad2")
# a = input("podaj liczbe a: ")
# b = input("podaj liczbe b: ")
# a = float(a)
# b = float(b)
# print("1 - dodawanie")
# print("2 - odejmowanie")
# print("3 - mnozenie")
# print("4 - dzielenie")
# print("5 - dzielenie calkowite")
# print("6 - reszta")
# print("7 - potega")
# print("8 - potega")
# sel = input("wybierz operacje: ")
# sel = int(sel)
# if sel == 1:
#     wynik = a + b
#     wynik = float(wynik)
#     print("wynik: %(wynik)f" % {'wynik': wynik})
# elif sel == 2:
#     wynik = a + b
#     wynik = float(wynik)
#     print("wynik: %(wynik)f" % {'wynik': wynik})
# elif sel == 3:
#     wynik = a * b
#     wynik = float(wynik)
#     print("wynik: %(wynik)f" % {'wynik': wynik})
# elif sel == 4:
#     wynik = a / b
#     wynik = float(wynik)
#     print("wynik: %(wynik)f" % {'wynik': wynik})
# elif sel == 5:
#     wynik = a // b
#     wynik = float(wynik)
#     print("wynik: %(wynik)f" % {'wynik': wynik})
# elif sel == 6:
#     wynik = a % b
#     wynik = float(wynik)
#     print("wynik: %(wynik)f" % {'wynik': wynik})
# elif sel == 7:
#     wynik = a ** b
#     wynik = float(wynik)
#     print("wynik: %(wynik)f" % {'wynik': wynik})
# elif sel == 8:
#     wynik = pow(a, b)
#     wynik = float(wynik)
#     print("wynik: %(wynik)f" % {'wynik': wynik})
# else:
#     print("blad")
# print("\nZad3")
# a = input("podaj liczbe: ")
# a = float(a)
# a += 1
# a -= 1
# a *= 2
# a /= 2
# a **= 2
# a %= 2
# print(a)
print("\nZad4")
#a = math.e
#print(a)
for i in range(0, 9, 1):
    a *= math.e
print("e^10 = %(a)f" % {'a': a})
print(pow(math.log(5 + (pow(math.sin(8), 2))), (1/6)))
print(math.floor(3.55))
print(math.ceil(4.8))
print("\nZad5")
string = "przemyslaw"
capString = string.capitalize()
string = "sZymanowski"
capString_ = string.capitalize()
print(capString + " " + capString_)
print("\nZad6")
string_ = "Tonight's the night we're gonna make it happen Tonight we'll put all other things aside Get in this time and show me some affection We're going for those pleasures in the night I want to love you, feel you Wrap myself around you I want to squeeze you, please you I just can't get enough And if you move real slow I'll let it go I'm so excited and I just can't hide it I'm about to lose control and I think I like it I'm so excited and I just can't hide it And I know, I know, I know, I know I know I want you We shouldn't even think about tomorrow Sweet memories will last for long, long time We'll have a good time, baby Don't do worry And if we're still playing around boy That's just fine Let's get excited We just can't hide it I'm about to lose control and I think I like it I'm so excited and I just can't hide it I know, I know, I know, I know I know I want you, I want you I want to love you, Feel you, wrap myself around you I want to squeeze you, please you No, I just can't get enough And if you move real slow I'll let it go I'm so excited I just can't hide it I'm about to lose control And I think I like it I'm so excited And I just can't hide it I know, I know, I know, I know I know I want you, Want you Look what you do to me You've got me burning up How did you get to me I've got to give it up Baby, I'm so excited I just can't hide it I'm about to lose control And I think I like it I'm so excited I can't deny, no, no I know, I know I want you"
x = string_.count("excited")
print("wystapienia slowa 'excited': %(x)d" % {'x': x})
print("\nZad7")
string = "Przemyslaw"
print(len(string))
print("Druga litera stringu: %(x)s" % {'x': string[1]})
print("Ostatnia litera stringu: %(x)s" % {'x': string[len(string) - 1]})
print("\nZad8")
x = string_.split("I")
print(x)
print("wyraz pierwszy: '%(x)s'" % {'x': x[0]})
print("wyraz drugi: '%(x)s'" % {'x': x[1]})
print("wyraz trzeci: '%(x)s'" % {'x': x[2]})
print("\nZad9")
string = "tekst"
n1 = 1.6180339887
n1 = float(n1)
n2 = 143
n2 = hex(n2)
print(string)
print(n1)
print(n2)
