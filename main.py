
# Nama  : Yudhistira Adhiaraka
# Nim   : 230103182
# Kelas : TI23A5
# Keterangan: Latihan membuat kelas Dosen, Ruang, dan KelasKuliah dengan validasi sederhana

# Kelas Dosen
class Dosen:
    def __init__(self, nidn, nama):
       
        if len(nidn) != 10:
            print("NIDN harus terdiri dari 10 digit angka.")
        elif not nidn.isdigit():
            print("NIDN hanya boleh angka.")
        else:
            self.nidn = nidn

        self.nama = nama  

    def info(self):
        
        print("Dosen:", self.nama, "-", getattr(self, 'nidn', 'NIDN tidak valid'))



# Kelas Ruang
class Ruang:
    def __init__(self, kode, kapasitas):
        self.kode = kode
        self.kapasitas = kapasitas  



# Kelas KelasKuliah
class KelasKuliah:
    def __init__(self, kode_kelas, ruang):
        self.kode_kelas = kode_kelas
        self.ruang = ruang
        self.daftar_mhs = []  

    def tambah_mahasiswa(self, nama):
        
        if len(self.daftar_mhs) >= self.ruang.kapasitas:
            print("Kelas", self.kode_kelas, "sudah penuh! Tidak bisa menambah:", nama)
        else:
            self.daftar_mhs.append(nama)
            print("Mahasiswa", nama, "berhasil ditambahkan ke kelas", self.kode_kelas)

    def tampilkan_semua(self):
        print("\n--- Daftar Mahasiswa di kelas", self.kode_kelas, "---")
        if len(self.daftar_mhs) == 0:
            print("Belum ada mahasiswa yang terdaftar.")
        else:
            for i in range(len(self.daftar_mhs)):
                print(f"{i+1}. {self.daftar_mhs[i]}")

    def tampilkan_huruf_DE(self):
        print("\nMahasiswa dengan huruf awal D atau E:")
        for nama in self.daftar_mhs:
            if nama[0].upper() == "D" or nama[0].upper() == "E":
                print("-", nama)



# Bagian utama program

print("=== Data Dosen ===")
d1 = Dosen("2301111111", "Roberto")
d2 = Dosen("2302222222", "Antonio")
d3 = Dosen("2303333333", "Alberto")
d4 = Dosen("2304444444", "Nacho")

d1.info()
d2.info()
d3.info()
d4.info()

print("\n=== Data Ruang dan Kelas ===")
ruangA = Ruang("R101", 10)
kelas_ti = KelasKuliah("TI-23A5", ruangA)


# Daftar nama mahasiswa baru
list_mhs = [
    "JA", "Saul", "Delo", "Hector", "Fring", "Walter", "Emilio", "Gelo",
    "Lamelo", "Kyre"
]


list_mhs.append("Celi")
list_mhs.append("Shela")



for nama in list_mhs:
    kelas_ti.tambah_mahasiswa(nama)


kelas_ti.tampilkan_semua()
kelas_ti.tampilkan_huruf_DE()
