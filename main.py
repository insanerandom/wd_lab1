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
