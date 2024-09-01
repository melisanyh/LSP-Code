class Costumer:
    def masuk(self):
        print("Costumer masuk ke sistem")

    def keluar(self):
        print("Costumer keluar dari sistem")

class Admin:
    def __init__(self, Costumer):
        self.Costumer = Costumer

    def Login_as_Admin(self):
        print("Admin masuk dengan level akses khusus")

    def Hapus_Costumer (self, Costumer):
        print("Costumer dihapus oleh Admin")

    def masuk(self):
        self.Costumer.masuk()

    def keluar(self):
        self.Costumer.keluar()

# Pengguna dan Admin
Costumer_biasa = Costumer()
admin = Admin(Costumer_biasa)

# Menggunakan metode Admin
admin.masuk()                # Ini akan menunjukkan "Pengguna masuk ke sistem"
admin.Login_as_Admin()  # Ini akan menunjukkan "Admin masuk dengan level akses khusus"
admin.keluar()               # Ini akan menunjukkan "Pengguna keluar dari sistem"
