# Latihan 6: Fungsi Dictionary

def tampilkan_mahasiswa(data):
    print("Daftar Mahasiswa:")
    for nim, nama in data.items():
        print(f"{nim}: {nama}")


def tambah_mahasiswa(data, nim, nama):
    data[nim] = nama


mahasiswa = {
    "A001": "Ayu",
    "A002": "Budi",
    "A003": "Citra"
}

tampilkan_mahasiswa(mahasiswa)

print("\nSetelah menambahkan mahasiswa:")
tambah_mahasiswa(mahasiswa, "A004", "Dina")
tampilkan_mahasiswa(mahasiswa)