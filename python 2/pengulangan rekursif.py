import os
os.system('cls')

def tampilangka (batas, i):
    print(f'Perulangan ke {i}')
    if (i > batas):
        tampilangka(batas, i - 1)
        
tampilangka(0,10)