def main():
    while True:
        print("\033[1;33;40m")  
        print("=== HESAP MAKİNESİ ===")
        print("1. Toplama")
        print("2. Çıkarma")
        print("3. Çarpma")
        print("4. Bölme")
        print("5. Ana menüye dön")

        secim = input("İşlem seçin (1-5): ")

        if secim == '5':
            break

        try:
            x = float(input("1. Sayı: "))
            y = float(input("2. Sayı: "))
        except ValueError:
            print("Geçersiz sayı girdiniz!")
            continue

        if secim == '1':
            print("Sonuç:", x + y)
        elif secim == '2':
            print("Sonuç:", x - y)
        elif secim == '3':
            print("Sonuç:", x * y)
        elif secim == '4':
            if y == 0:
                print("Sıfıra bölünemez!")
            else:
                print("Sonuç:", x / y)
        else:
            print("Geçersiz işlem!")

        print("\n--------------------------\n")