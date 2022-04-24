import string
import math
i = int(input())
tablica = []
result = []

for index in range(0,i):
  element=input().replace('\r', '').replace('\n', '').split(" ")
  for i in range (0,len(element)):
    element[i] = float(element[i])
  tablica.append(element)

for index in range(0,i+1):
  if len(tablica[index]) == 1:
    wynik = math.pi*(tablica[index][0])**2
    result.append(wynik)
    #result_wynik=math.pi*tablica[index]**2
    #result.append(result_wynik)
  elif len(tablica[index]) == 2:
    wynik = tablica[index][0]*tablica[index][1]
    result.append(wynik)
    #result_wynik=math.prod(tablica[index])
    #result.append(result_wynik)
  elif len(tablica[index]) == 3:
    s=sum(tablica[index])/2
    a=tablica[index][0]
    b=tablica[index][1]
    c=tablica[index][2]
    pole = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    #pozycja = len(tablica[index])
    #for i in range(pozycja):
    #  a=pozycja[0]
    #  b=pozycja[1]
    #  c=pozycja[2]
    #pole = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    result.append(pole)
  elif len(tablica[index]) > 3:
    print("Błąd: można podać maksymalnie 3 liczby")
    break
  else:
    print("Nic nie zostało podane")
    break

print(round(sum(result),2))