#Class and Inheritance
class Kendaraan:
  def __init__(self,jenis,banyakRoda,bahanBakar):
    self.jenis = jenis
    self.banyakRoda = banyakRoda
    self.bahanBakar = bahanBakar

  def henlo(self):
    print("Ini adalah " + self.jenis)

#Inheritance
class Mobil(Kendaraan):
  def __init__(self,jenis,banyakRoda,bahanBakar,warna):
    super().__init__(jenis,banyakRoda,bahanBakar)
    self.warna = warna

  def dataMobil(self):
    print("Jenis Mobil ini adalah " + self.jenis + " berwarna " + self.warna)

x = Mobil("Daihatsu",4,"premium","biru")
x.dataMobil()