def hesapla(a,b,c):
   

    def topla(a,b):
        print('Toplam:', a+b)

    # def carp(a,b):
    # print("Carp", a*b)

    if c=="+": topla(a,b)   
    if c=="*": carp(a,b)
    if c not in ["+","*"] :
        print('Böyle bir işlem tanımlı değil')
        exit()
        print('----------')
# carp(8,6) 
hesapla(4,5,"+")