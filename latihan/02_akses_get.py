# Latihan 2: Mengakses Dictionary dengan get()

mahasiswa = {
    "A001": "Ayu",
    "A002": "Budi",
    "A003": "Citra"
}

# Mengakses key yang tersedia
print("Nama mahasiswa A001:", mahasiswa.get("A001"))

# Mengakses key yang tidak tersedia
print("Nama mahasiswa A004:", mahasiswa.get("A004"))

# Memberikan nilai pengganti jika key tidak tersedia
print("Nama mahasiswa A004:", mahasiswa.get("A004", "Data tidak ditemukan"))