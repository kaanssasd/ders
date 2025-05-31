def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Hata: Sıfıra bölünemez!"
    return x / y

def hesap_makinesi():
    print("=== HESAP MAKİNESİ ===")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Çıkış")

    while True:
        secim = input("İşlem seçin (1/2/3/4/5): ")

        if secim == '5':
            print("Çıkılıyor...")
            break

        try:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")
            continue

        if secim == '1':
            print("Sonuç:", toplama(sayi1, sayi2))
        elif secim == '2':
            print("Sonuç:", cikarma(sayi1, sayi2))
        elif secim == '3':
            print("Sonuç:", carpma(sayi1, sayi2))
        elif secim == '4':
            print("Sonuç:", bolme(sayi1, sayi2))
        else:
            print("Geçersiz seçim!")

        print("\n----------------------\n")

# Programı başlat
hesap_makinesi()