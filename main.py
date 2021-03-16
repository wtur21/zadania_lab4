# zad. 1

import numpy as np

tab = np.arange(0, 15 * 3, 3)
print(tab)

# zad. 2

import numpy as np

tab1 = np.array([1.5, 2.2, 3.1, 4.3, 7.8])

tab2 = tab1.astype('int64')

# zad. 3

import numpy as np

def tablica(n):
    tab = np.arange(1, 1 + (n*n), 1)
    return tab

# zad. 4

import numpy as np

def tab_pot(a, b):
    tab = np.logspace(1, b, num=b, base=a)
    return tab

# zad. 5

import numpy as np

def wektor(dl):
    wek = np.arange(dl)
    wek = np.flip(wek)
    m_diag = np.diag([x for x in wek])
    print(wek)
    print(m_diag)

# zad. 6



# zad. 7



# zad. 8

import numpy as np

t = np.arange(18).reshape(3, 6)

def dziel(tab, kierunek):
     if kierunek == 'poziom' and tab.shape[0] % 2 == 0:
            pol = tab.shape[0] // 2
            return tab[:pol], tab[pol:]
     elif kierunek == 'pion' and tab.shape[1] % 2 == 0:
            pol = tab.shape[1] // 2
            return tab[:, :pol], tab[:, pol:]
     elif kierunek == 'poziom' and tab.shape[0] % 2 != 0:
         print("Nie można podzielić tej tablicy poziomo")
     elif kierunek == 'pion' and tab.shape[1] % 2 != 0:
         print("Nie można podzielić tej tablicy pionowo")

# zad. 9

import numpy as np

fibo = [0, 1]

for n in range(23):
    fibo.append(sum(fibo[-2:]))

fibo = np.array(fibo).reshape(5, 5)

print(fibo)