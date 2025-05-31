kahve_listesi = [
    {"ad": "Espresso", "fiyat": 30},
    {"ad": "Latte", "fiyat": 35},
    {"ad": "Cappuccino", "fiyat": 34},
    {"ad": "Türk Kahvesi", "fiyat": 28},
    {"ad": "Mocha", "fiyat": 38}
]

def kahve_menu():
    while True:
        print("\033[1;35;40m")  # Mor renk
        print("╔══════════════════════╗")
        print("║     KAHVE MENÜSÜ     ║")
        print("╚══════════════════════╝")

        for i, kahve in enumerate(kahve_listesi, start=1):
            print(f"{i}. {kahve['ad']} - {kahve['fiyat']}₺")

        print("\nBir kahve seçin (0 - Ana menü): ")
        secim = input(">> ").strip()  # ← boşlukları temizliyor

        if secim == '0':
            print("Ana menüye dönülüyor...")
            break

        try:
            index = int(secim) - 1
            if 0 <= index < len(kahve_listesi):
                secilen = kahve_listesi[index]
                print(f"\n☕ {secilen['ad']} hazırlanıyor...\n")
            else:
                print("Geçersiz kahve numarası.")
        except ValueError:
            print("Lütfen sayı girin.")

        print("-" * 30)