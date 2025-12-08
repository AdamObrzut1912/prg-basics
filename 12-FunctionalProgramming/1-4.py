speed = int(input("podaj prędkośc w m/s"))

v = 3.6

wzor = lambda x,y: x*y

wynik = wzor(speed,v)

print(f"prędkość w wkm/h to {wynik} km/hs")