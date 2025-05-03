print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
def menu1(): #definition/fonksiyon
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   VEKTOREL APP    \033[1;32;40m  ║")
    print("║                     ║")
    print("║  1-Görevler         ║")
    print("║  2-Oyunlar          ║")
    print("║  3-Hesap Makinesi   ║")
    print("║  4-Kahveler         ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")
# 201 ╔ # 205 ═ # 187 ╗ # 186 ║ # 200 ╚ # 188 ╝
# ASCII karakterleri ile yapabilirsiniz. ascii karakterlerini klavyedeki ALT tuşu basılı iken numerik alandan ascii değerlerini yazabilirsiniz.
# https://www.commfront.com/pages/ascii-chart 
# https://www.ascii-code.com/  
 

    seçim = input()
    if seçim == '1' :
        print('Görevleri seçtiniz')
        import Görevler
        menu1()
    if seçim == '2' :
        print('Oyunları Seçtiniz')
        menu1()
    if seçim == '3' :
        print('Hesap Makinesini seçtiniz')
        menu1()
    if seçim == '4' :
        print('Kahveleri seçtiniz')
        menu1()

menu1()