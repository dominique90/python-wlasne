Twoje_ulubione_auta = ['Twoja ulubiona lista aut:']

print 'Hej'
imie = raw_input('Jak masz na imie? ')

print 'Witamy Cie,',imie 

for auto in range(3):
    auto = raw_input('Podaj nazwe Twojego ulubionego samochodu: ')
    if auto == 'Audi' or auto == 'audi':
        print 'To drogie auto'
    elif auto == 'Alfa Romeo' or auto == 'alfa romeo':
        print 'Tez lubie alfy...'
    else:
        print "Rozumiem Twoj wybor, ale czemu nie Alfa Romeo?"

    
    Twoje_ulubione_auta.append(auto)
print Twoje_ulubione_auta
    
