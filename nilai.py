def input_nilai():
    tugas = float(input("Masukkan nilai Tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    
    nilai_akhir = (tugas + uts + uas) / 3
    return nilai_akhir  # <-- SUDAH BENAR: Diberi indentasi sejajar