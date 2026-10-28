# Latihan 3: Manipulasi Dictionary

mahasiswa = {
    "A001": "Ayu",
    "A002": "Budi",
    "A003": "Citra"
}

# Menambah data mahasiswa
mahasiswa["A004"] = "Dina"
print("Setelah menambah data:")
print(mahasiswa)

# Mengubah data mahasiswa
mahasiswa["A002"] = "Budi Santoso"
print("\nSetelah mengubah data:")
print(mahasiswa)

# Menghapus data mahasiswa
mahasiswa.pop("A003")
print("\nSetelah menghapus data:")
print(mahasiswa)