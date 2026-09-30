
from data_mahasiswa import input_mahasiswa
from nilai import input_nilai
from kondisi import cek_kondisi

def main():
    print("=== INPUT DATA MAHASISWA ===")
    npm = input("Masukkan NPM: ")
    nama = input("Masukkan Nama: ")
    umur = input("Masukkan Umur: ")
    tinggi = input("Masukkan Tinggi: ")
    prodi = input("Masukkan Prodi: ")
    
    print("\n=== DATA MAHASISWA ===")
    input_mahasiswa(npm, nama, umur, tinggi, prodi)
    
    print("\n=== INPUT NILAI MAHASISWA ===")
    nilai_akhir = input_nilai()
    
    grade, status = cek_kondisi(nilai_akhir)
    
    print(f"Nilai Akhir : {nilai_akhir:.2f}")
    print(f"Grade       : {grade}")
    print(f"Status      : {status}")

if __name__ == "__main__":
    main()