import string
import math
i = int(input())
tablica = []
result = 0

for index in range(0,i):
  element=input().replace('\r', '').replace('\n', '').split(" ")
  for i in range (0,len(element)):
    element[i] = float(element[i])
  tablica.append(element)

for wymiar in tablica:
  if len(wymiar) == 1:
    wynik = math.pi*(wymiar[0])**2
    result += wynik
  elif len(wymiar) == 2:
    wynik = wymiar[0]*wymiar[1]
    result += wynik
  elif len(wymiar) == 3:
    s=sum(wymiar)/2
    a=wymiar[0]
    b=wymiar[1]
    c=wymiar[2]
    pole = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    result += pole
  elif len(wymiar) > 3:
    print("Błąd: można podać maksymalnie 3 liczby")
    break
  else:
    print("Nic nie zostało podane")
    break

print(round(result,2))