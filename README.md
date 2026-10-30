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

## Kuis Formatif Pertemuan 11 — Dictionary/Map

1. Apa perbedaan utama list dan dictionary?

List menyimpan data berdasarkan indeks, sedangkan dictionary menyimpan data dalam pasangan key dan value.

2. Apa fungsi key dalam dictionary?

Key digunakan sebagai identitas untuk mengakses value tertentu di dalam dictionary.

3. Apa yang terjadi jika "data['kelas']" dipanggil saat key "'kelas'" tidak ada?

Python akan menghasilkan "KeyError" karena key "'kelas'" tidak ditemukan.

4. Apa perbedaan "data['kelas']" dengan "data.get('kelas')"?

"data['kelas']" menghasilkan "KeyError" jika key tidak tersedia, sedangkan "data.get('kelas')" mengembalikan "None" jika key tidak tersedia secara default.

5. Bagaimana memeriksa apakah suatu key tersedia?

Dengan menggunakan operator "in", misalnya "'kelas' in data".

6. Apa fungsi "items()"?

"items()" digunakan untuk mengambil pasangan key dan value sehingga keduanya dapat ditelusuri, misalnya menggunakan perulangan "for".

7. Bagaimana menambahkan pasangan key-value baru?

Dengan menuliskan key baru beserta valuenya, misalnya "data['A006'] = 'Fajar'".

8. Bagaimana mengubah value dari key yang sudah ada?

Dengan memberikan value baru pada key tersebut, misalnya "data['A002'] = 'Budi Santoso'".

9. Dalam data pendidikan, mengapa NIM cocok digunakan sebagai key?

Karena NIM merupakan identitas unik mahasiswa sehingga data setiap mahasiswa lebih mudah dicari dan dibedakan.

10. Perintah apa yang digunakan untuk mengirim commit ke GitHub?

Perintah "git push" digunakan untuk mengirim commit lokal ke repository GitHub yang sudah terhubung.
