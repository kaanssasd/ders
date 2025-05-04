not1 = int(input("Ortalaman Kaç"))

if not1<=100 and not1>0:
    if not1>90 : print("Süper")
    elif not1>85 : print("5 aldın")
    elif not1>70 : print("4 aldın")
    elif not1>=50 : print("3 aldın")
    if not1<50:   print("kaldın" )
else:
    print("Doğru not değeri girmediniz")