def cek_kondisi(nilai_akhir):
    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 75:
        grade = "B"
    elif nilai_akhir >= 65:
        grade = "C"
    elif nilai_akhir >= 50:
        grade = "D"
    else:
        grade = "E"
        
    if nilai_akhir >= 65:
        status = "LULUS"
    else:
        status = "TIDAK LULUS"
        
    return grade, status