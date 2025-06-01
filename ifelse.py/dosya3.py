with open("rehber.txt", "r") as d:
    print("╔", "═"*10, "╣   ARAMA YAP     ╠", "═"*10, "╗", sep="")
    aranan = input("Aranan : ")

    # Satır satır arama yapıyoruz
    for sn, a in enumerate(d, 1):
        if aranan.lower() in a.lower():
            print(f"{sn}.satırda bulundu:\nAdı:\
{a.strip().split("#")[0]}, Numarası: {a.strip().split("#")[1]}")