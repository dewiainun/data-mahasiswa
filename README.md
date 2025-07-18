# data-mahasiswa

Aplikasi web sederhana untuk manajemen data mahasiswa dan mata kuliah menggunakan Flask, MySQL, dan Bootstrap.

## Fitur

- **Login:** Halaman login sederhana untuk masuk ke aplikasi.
- **Manajemen Mahasiswa:**  
  - Melihat daftar mahasiswa.
  - Menambah data mahasiswa baru.
  - Mengedit data mahasiswa.
  - Menghapus data mahasiswa.
- **Manajemen Mata Kuliah:**  
  - Melihat daftar mata kuliah.
  - Menambah data mata kuliah baru.
  - Mengedit data mata kuliah.
  - Menghapus data mata kuliah.
- **Logout:** Untuk keluar dari sesi aplikasi.

## Struktur Proyek

- `app.py` — File utama aplikasi Flask.
- `templates/` — Berisi template HTML (login, mahasiswa, matakuliah, dll).
- `static/bootstrap.min.css` — File CSS Bootstrap untuk styling.
- `README.md` — Dokumentasi ini.
- `LICENSE` — Lisensi MIT.

## Instalasi & Menjalankan Aplikasi

1. **Buat virtual environment (opsional namun direkomendasikan):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. **Install dependencies:**
   ```bash
   pip install flask flask-mysqldb
   ```

3. **Konfigurasi Database MySQL:**
   - Buat database dengan nama `database_new`.
   - Buat tabel `mahasiswa`:
     ```sql
     CREATE TABLE mahasiswa (
       nama VARCHAR(100),
       npm INT PRIMARY KEY,
       jurusan VARCHAR(100)
     );
     ```
   - Buat tabel `matakuliah`:
     ```sql
     CREATE TABLE matakuliah (
       kode_matkul VARCHAR(20) PRIMARY KEY,
       nama_mk VARCHAR(100),
       fakultas VARCHAR(100),
       sks INT
     );
     ```
   - Pastikan konfigurasi database di `app.py` sesuai:
     ```python
     app.config['MYSQL_HOST'] = 'localhost'
     app.config['MYSQL_USER'] = 'root'
     app.config['MYSQL_PASSWORD'] = ''
     app.config['MYSQL_DB'] = 'database_new'
     ```

4. **Jalankan aplikasi:**
   ```bash
   python app.py
   ```
   Aplikasi akan berjalan di `http://localhost:5000`

## Penggunaan

- Buka browser dan akses `http://localhost:5000`
- Login menggunakan data (belum ada autentikasi user sungguhan, hanya tombol login saja)
- Setelah login, akan diarahkan ke halaman mahasiswa.
- Gunakan tombol **Tambah Mahasiswa** atau **Tambah Mata Kuliah** sesuai kebutuhan.
- Edit/hapus data mahasiswa/matakuliah melalui tombol di tabel.

## Lisensi

Aplikasi ini menggunakan lisensi MIT. Silakan lihat file `LICENSE` untuk detailnya.

---
