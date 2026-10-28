# Latihan 4: Iterasi Dictionary

mahasiswa = {
    "A001": "Ayu",
    "A002": "Budi",
    "A003": "Citra"
}

# Menampilkan semua key
print("Daftar NIM:")
for nim in mahasiswa.keys():
    print(nim)

# Menampilkan semua value
print("\nDaftar Nama Mahasiswa:")
for nama in mahasiswa.values():
    print(nama)

# Menampilkan key dan value
print("\nData Mahasiswa:")
for nim, nama in mahasiswa.items():
    print(f"{nim}: {nama}")