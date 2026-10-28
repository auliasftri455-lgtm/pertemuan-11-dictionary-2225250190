# Latihan 1: Dasar Dictionary

mahasiswa = {
    "A001": "Ayu",
    "A002": "Budi",
    "A003": "Citra"
}

print("Data Mahasiswa:")
print(mahasiswa)

print("\nNama mahasiswa dengan NIM A002:")
print(mahasiswa["A002"])

print("\nApakah NIM A004 tersedia?")
print("A004" in mahasiswa)

print("\nJumlah mahasiswa:")
print(len(mahasiswa))