kahve_listesi = [
    {"ad": "Espresso", "fiyat": 100},
    {"ad": "Latte", "fiyat": 120},
    {"ad": "Cappuccino", "fiyat": 130},
    {"ad": "Türk Kahvesi", "fiyat": 150},
    {"ad": "Mocha", "fiyat": 140}
]

def kahve_menu():
    while True:
        print("\033[1;35;40m")  
        print("╔══════════════════════╗")
        print("║     KAHVE MENÜSÜ     ║")
        print("╚══════════════════════╝")

        for i, kahve in enumerate(kahve_listesi, start=1):
            print(f"{i}. {kahve['ad']} - {kahve['fiyat']}₺")

        print("\nBir kahve seçin (0 - Ana menü): ")
        secim = input(">> ").strip()  

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