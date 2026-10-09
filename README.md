# Pertemuan 06 - Nested Loop Python

Nama: Aditya Setianugroho  
NIM: 2225250172  
Kelas: 3F

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan untuk menyelesaikan permasalahan perhitungan tabel perkalian dan statistik angka genap.

## Cara Menjalankan
```bash
python tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas
1. Minta pengguna memasukkan bilangan bulat positif `n`.
2. Jika `n <= 0`, ulangi pemintaan input hingga nilai yang dimasukkan valid.
3. Inisialisasi `total_semua = 0` sebagai akumulator total keseluruhan dan `count_genap = 0` sebagai penghitung jumlah hasil yang genap.
4. Gunakan loop luar `for i in range(1, n + 1)` untuk memproses setiap baris.
5. Di dalam loop luar, inisialisasi `total_baris = 0` agar akumulasi baris selalu dimulai dari nol.
6. Gunakan loop dalam `for j in range(1, n + 1)` untuk memproses setiap kolom.
7. Hitung `hasil = i * j` di dalam loop dalam.
8. Cetak hasil dengan format yang rapi menggunakan `end=""` agar tidak berpindah baris.
9. Tambahkan `hasil` ke `total_baris` dan `total_semua`.
10. Jika `hasil % 2 == 0`, tambahkan 1 ke `count_genap`.
11. Setelah loop dalam selesai, cetak total per baris.
12. Setelah seluruh loop selesai, tampilkan `total_semua` dan `count_genap`.

## Hasil Pengujian
- Test Case 1: Input `n = 1`  
  Diharapkan: Total semua = 1, Banyak hasil genap = 0  
  Aktual: Total semua = 1, Banyak hasil genap = 0  
  Status: Berhasil

- Test Case 2: Input `n = 2`  
  Diharapkan: Total semua = 9, Banyak hasil genap = 3  
  Aktual: Total semua = 9, Banyak hasil genap = 3  
  Status: Berhasil

- Test Case 3: Input `n = 3`  
  Diharapkan: Total semua = 36, Banyak hasil genap = 5  
  Aktual: Total semua = 36, Banyak hasil genap = 5  
  Status: Berhasil

## Analisis Efisiensi
Jika program menerima input `n`, maka loop luar akan dieksekusi `n` kali. Pada setiap iterasi loop luar, loop dalam akan berjalan sebanyak `n` kali. Dengan demikian, operasi perkalian `hasil = i * j` akan dilakukan sebanyak `n x n` kali. Misalnya, jika `n = 3`, maka badan loop dalam dieksekusi 9 kali.

## Refleksi
Salah satu kesalahan umum dalam penggunaan nested loop pada proses akumulasi adalah meletakkan inisialisasi variabel total keseluruhan, seperti `total_semua = 0`, di dalam loop. Akibatnya, nilai tersebut akan selalu reset setiap iterasi dan hasil akhirnya hanya mencerminkan data pada iterasi terakhir. Solusinya adalah melakukan inisialisasi di luar perulangan bersarang agar nilai akumulasi tetap terjaga dari awal hingga akhir program.