import os
mevcutlar = os.listdir()
for a in mevcutlar:
    if a.endswith(".txt"):
        print(a)