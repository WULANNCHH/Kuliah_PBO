class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama          # atribut public
        self.__saldo = saldo      # atribut private (tidak bisa diakses langsung di luar class)

    # method untuk menampilkan saldo
    def lihat_saldo(self):
        print(f"Saldo {self.nama}: Rp{self.__saldo}")

    # method untuk mengubah saldo (misalnya setor atau tarik uang)
    def ubah_saldo(self, jumlah):
        if self.__saldo + jumlah < 0:
            print("ERROR: Saldo tidak boleh negatif!")
        else:
            self.__saldo += jumlah
            print(f"Saldo {self.nama} berhasil diubah menjadi Rp{self.__saldo}")


# Membuat objek akun
akun_budi = RekeningBank("Budi", 1000000)

# Menampilkan saldo awal
akun_budi.lihat_saldo()

# Mencoba ubah saldo dengan benar
akun_budi.ubah_saldo(-500000)
akun_budi.lihat_saldo()

# Mencoba akses saldo langsung dari luar class (akan error)
try:
    print(akun_budi.__saldo)
except AttributeError:
    print("ERROR: saldo tidak bisa diakses langsung dari luar class!")
