def gmenu():
    print('Görevler ekranı')

    print("\033[1;32;40m")

    
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   VEKTOREL APP    \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Web Sitesi kur   ║")
    print("║  2-Oyun Yap         ║")
    print("║  3-Kendini Geliştir ║")
    print("║  4-...              ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    seçim = input()
    if seçim == '1' :
        print('Web sitesi kurmak kolay iş değil ama aklına koyduğun her şeyi yapabilirsin')
    seçim = input()
    if seçim == '2' :
        print('Oyun yapmak web sitesi yapmaktan da zor olsa çok keyiflidir')