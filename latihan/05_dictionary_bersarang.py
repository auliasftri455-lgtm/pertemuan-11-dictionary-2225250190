# Latihan 5: Dictionary Bersarang

mahasiswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78},
    "A003": {"nama": "Citra", "nilai": 92}
}

print("Data mahasiswa A001:")
print("Nama:", mahasiswa["A001"]["nama"])
print("Nilai:", mahasiswa["A001"]["nilai"])

print("\nSeluruh data mahasiswa:")
for nim, data in mahasiswa.items():
    print(f"{nim}: {data['nama']}, nilai {data['nilai']}")