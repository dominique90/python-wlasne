# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Nazwa pliku: parzyste.py

print "Witaj w programie, który sprawdzi, czy wpisana przez Ciebie liczba jest parzysta, czy nieparzysta!"
imie = raw_input("Jak masz na imie? ")
for liczba in range(3):
    liczba = input("Podaj Twoja liczbe: ")
    if liczba%2 == 0:
        print imie,"Twoja liczba jest parzysta!"
    else:
        print imie,"Twoja liczba jest nieparzysta"
    
