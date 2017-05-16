#!/usr/bin/env python

def silniaiteracja(x):

    zmienna_pomocnicza = 1

    if x<2:
        return 1
    else:
         for a in range(2,x+1):
             zmienna_pomocnicza = zmienna_pomocnicza * a
         return zmienna_pomocnicza

print silniaiteracja(5)
