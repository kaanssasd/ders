import gorevler
import oyunlar
import hesapmakinesi
import kahveler 

def menu1():

    while True:
        print("\033[1;32;40m")
        print("╔═════════════════════╗")
        print("║\033[1;31;40m   VEKTOREL APP    \033[1;32;40m  ║")
        print("║                     ║")
        print("║  1 - Görevler       ║")
        print("║  2 - Oyunlar        ║")
        print("║  3 - Hesap Makinesi ║")
        print("║  4 - Kahveler       ║")
        print("║  5 - Çıkış          ║")
        print("╚═════════════════════╝")

        secim = input(">> ").strip()

        if secim == '1':
            gorevler.gmenu()  
        elif secim == '2':
            oyunlar.oyun_menu()
        elif secim == '3':
            hesapmakinesi.main()  
        elif secim == '4':
                kahveler.kahve_menu()
        elif secim == '5':
            print("Çıkılıyor...")
            break
        else:
            print("❌ Geçersiz seçim! Tekrar deneyin.")

menu1()