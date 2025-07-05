from PyQt6.QtWidgets import *
class StokMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STOK MODÜLÜ")
        # self.setFixedSize(500,300)


        gicerik = QVBoxLayout()  
       
        dicerik1 = QVBoxLayout()


        yicerik3 = QHBoxLayout()
        yicerik3.addWidget(QLabel("Stok menşei:"))
        yicerik3.addWidget(QLineEdit())


        yicerik4 = QHBoxLayout()
        yicerik4.addWidget(QLabel("Stok cinsi:"))
        yicerik4.addWidget(QLineEdit())


        yicerik5 = QHBoxLayout()
        yicerik5.addWidget(QLabel("Stok durumu:"))
        yicerik5.addWidget(QLineEdit())


        dicerik1.addLayout(yicerik3)
        dicerik1.addLayout(yicerik4)
        dicerik1.addLayout(yicerik5)
        # dicerik1.addWidget(QLabel("dicerik LAbel2"))
        # dicerik1.addWidget(QLabel("dicerik LAbel3"))
     
        yicerik1 = QHBoxLayout()
        yicerik1.addWidget(QLabel("Ürün stok no"))
        yicerik1.addWidget(QLabel("Stok adı"))
        yicerik1.addWidget(QLabel("Stok miktarı"))


        dugmeler = QHBoxLayout()
        tamamd = QPushButton("Kaydet")
        tamamd.clicked.connect(self.tamamDugmesi)
        iptald = QPushButton("İptal")
        cikisd = QPushButton("Çıkış")
        cikisd.clicked.connect(self.cikisDugmesi)
        dugmeler.addWidget(tamamd)
        dugmeler.addWidget(iptald)
        dugmeler.addWidget(cikisd)
       
        yicerik2 = QHBoxLayout()
        sn = QLineEdit("Stok no girin")
        yicerik2.addWidget(sn)
        sa = QLineEdit("Stok adı")
        yicerik2.addWidget(sa)
        sm = QLineEdit()
        yicerik2.addWidget(sm)




        gicerik.addLayout(yicerik1)
        gicerik.addLayout(yicerik2)
        gicerik.addLayout(dicerik1)
        gicerik.addLayout(dugmeler)
        araclar = QWidget()
        araclar.setLayout(gicerik)
        self.setCentralWidget(araclar)


    def dugmeBasma(self):
        print(self.baslikkk," başlıklı pencerede düğmeye bastın")


    def tamamDugmesi(self):
        print("Tamam düğmesine basıldı")
   
    def cikisDugmesi(self):
        print("Çıkışa basıldı basıldı")
        self.close()




class AnaMenu(QMainWindow):


    def __init__(self,baslik="Uygulama penceresi",e=500,b=300):
        super().__init__()
        self.setWindowTitle(baslik)
        # self.setFixedSize(e,b)
        self.baslikkk = baslik


        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("ANA MENU"))


        dugme1 = QPushButton("STOK MODÜLÜ")
        dugme1.clicked.connect(self.dugme1Basma)
        icerik.addWidget(dugme1)
       
        dugme2 = QPushButton("FATURA MODÜLÜ")
        dugme2.clicked.connect(self.dugme2Basma)
        icerik.addWidget(dugme2)


        dugme3 = QPushButton("CARİ MODÜLÜ")
        dugme3.clicked.connect(self.dugme3Basma)
        icerik.addWidget(dugme3)


        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)


    def dugme1Basma(self):
        print("Düğme1 basıldı")
        self.close()  # Login penceresini kapat
        self.stok_penceresi = StokMenu()
        self.stok_penceresi.show()


    def dugme2Basma(self):
        QMessageBox.information(self, "Başarılı", "Fatura modülü!\nKullanıma hazır değil.")


    def dugme3Basma(self):
        print("Cari Modülü Kullanıma Hazır Değil")


uygulama = QApplication([])
pencere = AnaMenu("Program ana menüsü")
pencere.show()
uygulama.exec()