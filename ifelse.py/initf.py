class Ogrenci:
    print("\n\nÖğrenci sınıfı çalıştı")
    ad = "---"
    soyad = ""
    disiplinCezasi = 0
    def __init__(self,xx,yy):
        self.ad = xx
        self.soyad = yy
    def bilgiYaz(aa):
        print(f"\n\nÖğrenci bilgisi:{aa.ad} {aa.soyad} {aa.disiplinCezasi}")
    def disiplinCezasiVer(s):
        s.disiplinCezasi += 10

print("Ogrenci.ad:",Ogrenci.ad)
ogrenci1 = Ogrenci("Mercan","GÜL") # () __init__ parantezi
ogrenci2 = Ogrenci("Arda","KESKİN")

ogrenci1.bilgiYaz()
ogrenci2.disiplinCezasiVer()
ogrenci2.disiplinCezasiVer()

ogrenci2.bilgiYaz()
