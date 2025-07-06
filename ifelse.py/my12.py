import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
    )
    print("Bağlantı Tamam")
    print(mydb)
except Exception as hata:
    print("Veri Tabanına Bağlanırken Hata Oluştu")