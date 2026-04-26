# UTS DevOps - Analisis Nilai Sederhana

## Deskripsi Proyek

Aplikasi ini merupakan program sederhana berbasis Python yang digunakan untuk melakukan analisis data berupa penjumlahan nilai. Data nilai diambil dari environment variable, kemudian diproses menggunakan library pandas, dan hasilnya disimpan dalam file CSV.

## Arsitektur Sistem

Aplikasi ini menggunakan Docker sebagai containerization dengan base image `python:3.9-slim` karena ringan, cepat, dan efisien untuk menjalankan aplikasi Python sederhana.

Sistem terdiri dari dua service, yaitu:

* **app**: menjalankan script Python (uts.py) untuk memproses data
* **db**: database PostgreSQL yang disiapkan sebagai bagian dari arsitektur (meskipun pada implementasi sederhana ini belum digunakan secara langsung)

Komunikasi antar container terjadi melalui Docker network, di mana setiap service dapat saling terhubung menggunakan nama servicenya (misalnya `db`).

## Cara Menjalankan (How to Run)

1. Clone repository:

   ```
   git clone <link-repo-anda>
   cd uts-devops
   ```

2. Jalankan aplikasi dengan Docker Compose:

   ```
   docker-compose up --build
   ```

3. Setelah berhasil, hasil akan tersimpan di:

   ```
   output/hasil.csv
   ```

## CI/CD

Proyek ini menggunakan GitHub Actions untuk melakukan proses Continuous Integration berupa pengecekan kualitas kode (linting) menggunakan flake8 setiap kali terjadi push ke repository.
