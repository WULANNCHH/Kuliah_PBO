# Tugas praktikum modul 1
class PersegiPanjang:
    # constructor dengan parameter panjang dan lebar
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        
    # Method untuk menghitung luas
    def hitung_luas(self):
        return self.panjang * self.lebar
    
    # Method untuk menghitung keliling
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    
# Membuat object dari class persegi panjang
pp1 = PersegiPanjang(10, 5)
PP2 = PersegiPanjang(7, 3)
       
# Menghasilkan hasil perhitungan
print("persegi panjang 1")
print("panjang:", pp1.panjang)
print("lebar:", pp1.lebar) 
print("luas:", pp1.hitung_luas())
print("keliling:", pp1.hitung_keliling())

print("persegi panjang 2")
print("panjang:", PP2.panjang)
print("lebar:", PP2.lebar) 
print("luas:", PP2.hitung_luas())
print("keliling:", PP2.hitung_keliling())
