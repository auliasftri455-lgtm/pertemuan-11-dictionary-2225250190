# Pertemuan 11 - Dictionary/Map

Nama: Aulia Safitri  
NIM: 2225250190  
Kelas: 3B

## Tujuan

Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data

Program menggunakan dictionary dengan NIM sebagai key utama. Setiap value berupa dictionary yang berisi nama, kelas, dan nilai mahasiswa.

## Cara Menjalankan

Jalankan program utama menggunakan perintah:

```bash
python praktik/data_mahasiswa.py
```

File latihan dapat dijalankan secara terpisah dari folder latihan.

## Test Case

| Kasus | Input/Aksi | Hasil yang Diharapkan |
|---|---|---|
| Pencarian tersedia | A003 | Data Citra ditampilkan |
| Pencarian tidak tersedia | A999 | Data tidak ditemukan |
| Pembaruan nilai | A002 menjadi 82 | Nilai A002 berubah menjadi 82 |
| Penambahan data | A006 | Data Fajar berhasil ditambahkan |
| Rekap | `items()` | Semua data mahasiswa ditampilkan |
| Rata-rata | Seluruh nilai mahasiswa | Rata-rata dihitung dengan benar |

## Refleksi

Kesalahan akses key dapat terjadi ketika program mencari NIM yang tidak tersedia. Untuk mengatasinya, fungsi `get()` digunakan agar pencarian tidak langsung menyebabkan KeyError.
