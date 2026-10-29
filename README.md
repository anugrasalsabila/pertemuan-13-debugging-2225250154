
# Pertemuan 13 - Debugging, Tracing, Testing, dan Test Case

Nama: Intan Anugra Salsabila
NIM: 2225250154
Kelas: 3F

## Tujuan
Mempelajari proses debugging, tracing, pengujian menggunakan test case, menemukan akar penyebab bug, memperbaiki program, dan melakukan pengujian ulang.

## Cara Menjalankan
Jalankan perintah berikut dari folder utama proyek:

```bash
py kasus/kasus_01_batas_kelulusan.py
py kasus/kasus_02_rata_rata.py
py kasus/kasus_03_file_nilai.py
py latihan/01_trace_loop.py
py latihan/02_trace_fungsi.py
py latihan/03_test_case.py
py latihan/04_debug_breakpoint.py
py pratik/praktik_4_debugging.py
```

## Hasil Pengujian Kasus

| File | Hasil Aktual | Status |
|---|---|---|
| kasus_01_batas_kelulusan.py | Menampilkan Tidak lulus dan Lulus | Berhasil dijalankan |
| kasus_02_rata_rata.py | Menampilkan 48.0 | Berhasil dijalankan, hasil perlu diperiksa |
| kasus_03_file_nilai.py | Terjadi FileNotFoundError karena data/nilai.txt tidak ditemukan | Belum berhasil |
| 02_trace_fungsi.py | Tidak menampilkan output | Perlu diperiksa |
| 03_test_case.py | Tidak menampilkan output | Perlu diperiksa |
| 04_debug_breakpoint.py | Tidak menampilkan output | Perlu diperiksa |
| praktik_4_debugging.py | Rata-rata 75.0, Status 60: Lulus, Tertinggi: 90, Rata-rata data kedua: 90.0, Status 59: Tidak lulus | Berhasil |

## Praktik 4: Investigasi dan Perbaikan Bug

Program awal memiliki tiga bug utama, yaitu pembagi rata-rata menggunakan angka tetap 5, kondisi kelulusan menggunakan operator lebih besar dari 60, dan pencarian nilai tertinggi menggunakan perbandingan yang salah.

### Bug Report

| Bug | Akar Penyebab | Perbaikan |
|---|---|---|
| Rata-rata tidak sesuai jumlah data | Pembagi menggunakan angka tetap 5 | Menggunakan len(nilai) |
| Nilai 60 dianggap tidak lulus | Kondisi menggunakan nilai > 60 | Menggunakan nilai >= 60 |
| Nilai tertinggi salah | Kondisi menggunakan x < tertinggi | Menggunakan x > tertinggi |

### Test Case dan Hasil Retest

| ID | Pengujian | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| T1 | Rata-rata [80, 60, 90, 70] | 75.0 | 75.0 | Berhasil |
| T2 | Rata-rata [100, 80] | 90.0 | 90.0 | Berhasil |
| T3 | Status nilai 60 | Lulus | Lulus | Berhasil |
| T4 | Status nilai 59 | Tidak lulus | Tidak lulus | Berhasil |
| T5 | Nilai tertinggi [80, 60, 90, 70] | 90 | 90 | Berhasil |

## Refleksi
Pada pertemuan ini, saya mempelajari cara menemukan dan memperbaiki kesalahan pada program menggunakan debugging, tracing, dan test case.

Pada Praktik 4 ditemukan tiga bug, yaitu kesalahan pembagi rata-rata, batas kelulusan, dan perbandingan nilai tertinggi. Setelah diperbaiki, program berhasil menghasilkan rata-rata 75.0, menyatakan nilai 60 sebagai lulus, dan menampilkan nilai tertinggi 90.

Pada kasus file nilai, program mengalami FileNotFoundError karena file data/nilai.txt tidak ditemukan. Hal ini menunjukkan pentingnya memastikan lokasi file dan menangani error agar program dapat berjalan dengan baik.