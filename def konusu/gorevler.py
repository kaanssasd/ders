gorev_listesi = []

def listele():
    if not gorev_listesi:
        print("Görev listeniz boş.")
    else:
        print("\n=== Görev Listesi ===")
        for i, gorev in enumerate(gorev_listesi, start=1):
            print(f"{i}. {gorev}")
    print()

def ekle():
    yeni_gorev = input("Yeni görev girin: ").strip()
    if yeni_gorev:
        gorev_listesi.append(yeni_gorev)
        print(f"'{yeni_gorev}' görevi eklendi.")
    else:
        print("Boş görev eklenemez.")

def sil():
    listele()
    try:
        no = int(input("Silmek istediğiniz görevin numarası: "))
        if 1 <= no <= len(gorev_listesi):
            silinen = gorev_listesi.pop(no-1)
            print(f"'{silinen}' görevi silindi.")
        else:
            print("Geçersiz numara.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

def gmenu():
    while True:
        print("\n=== GÖREVLER MENÜSÜ ===")
        print("1. Görevleri Listele")
        print("2. Görev Ekle")
        print("3. Görev Sil")
        print("4. Ana Menüye Dön")

        secim = input("Seçiminiz: ").strip()

        if secim == '1':
            listele()
        elif secim == '2':
            ekle()
        elif secim == '3':
            sil()
        elif secim == '4':
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")