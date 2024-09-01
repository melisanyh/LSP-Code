class Costumer:
    def masuk(self):
        print("Costumer masuk ke sistem")

    def keluar(self):
        print("Costumer keluar dari sistem")

class Admin(Costumer):
    def masuk(self):
        print("Admin masuk dengan level akses khusus")

    def Hapus_Costumer(self, Costumer):
        print("Costumer dihapus oleh Admin")

def Autentikasi_Costumer(Costumer):
    Costumer.masuk()
    Costumer.keluar()

Costumer = Admin()
Autentikasi_Costumer(Costumer) 