
def baca_nilai(nama_file):
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            if not baris:
                continue
            print(float(baris))


baca_nilai("data/nilai.txt")