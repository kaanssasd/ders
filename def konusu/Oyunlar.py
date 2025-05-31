import random

def sayi_tahmin_oyunu():
    print("\n🎯 SAYI TAHMİN OYUNU 🎯")
    hedef = random.randint(1, 100)
    tahmin_sayisi = 0

    while True:
        try:
            tahmin = int(input("1-100 arasında bir sayı tahmin et: "))
        except ValueError:
            print("Lütfen geçerli bir sayı gir!")
            continue

        tahmin_sayisi += 1

        if tahmin < hedef:
            print("Daha büyük bir sayı söyle.")
        elif tahmin > hedef:
            print("Daha küçük bir sayı söyle.")
        else:
            print(f"Tebrikler! {tahmin_sayisi}. denemede doğru sayıyı buldun: {hedef}")
            break

def oyun_menu():
    while True:
        print("\n=== OYUNLAR MENÜSÜ ===")
        print("1. Sayı Tahmin Oyunu")
        print("2. Ana Menüye Dön")

        secim = input("Seçiminiz: ").strip()

        if secim == '1':
            sayi_tahmin_oyunu()
        elif secim == '2':
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")