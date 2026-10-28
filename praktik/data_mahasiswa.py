# Praktik: Sistem Data Mahasiswa
# Pertemuan 11 - Dictionary/Map

def cari_mahasiswa(data, nim):
    return data.get(nim)


def rata_rata_nilai(data):
    if len(data) == 0:
        return 0

    total = 0
    for info in data.values():
        total += info["nilai"]

    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# Pencarian mahasiswa
print("=== PENCARIAN MAHASISWA ===")
nim_cari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)

if hasil is not None:
    print(f"NIM: {nim_cari}")
    print(f"Nama: {hasil['nama']}")
    print(f"Kelas: {hasil['kelas']}")
    print(f"Nilai: {hasil['nilai']}")
else:
    print("Data tidak ditemukan")

# Pencarian NIM yang tidak tersedia
print("\n=== PENCARIAN NIM A999 ===")
hasil = cari_mahasiswa(data_mahasiswa, "A999")

if hasil is not None:
    print(hasil)
else:
    print("Data tidak ditemukan")

# Menambahkan mahasiswa baru
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

# Memperbarui nilai mahasiswa A002
data_mahasiswa["A002"]["nilai"] = 82

# Menampilkan seluruh data mahasiswa
print("\n=== REKAP DATA MAHASISWA ===")
for nim, info in data_mahasiswa.items():
    print(
        f"{nim}: {info['nama']}, "
        f"Kelas {info['kelas']}, Nilai {info['nilai']}"
    )

# Menghitung rata-rata nilai
print("\n=== RATA-RATA NILAI ===")
print(f"Rata-rata nilai mahasiswa: {rata_rata_nilai(data_mahasiswa):.2f}")