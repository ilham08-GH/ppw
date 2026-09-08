# 🌐 Penambangan & Pencarian Web (PPW)

Dokumentasi dan repositori tugas praktikum mata kuliah **Penambangan & Pencarian Web (PPW)**, Program Studi Teknik Informatika, Universitas Trunojoyo Madura.

---

## 👤 Biodata Mahasiswa
- **Nama**: Muhammad Ilham Adila Almafaz
- **NPM / NIM**: 230411100113 (23-113)
- **Program Studi**: Teknik Informatika
- **Fakultas**: Fakultas Teknik
- **Universitas**: Universitas Trunojoyo Madura

---

## 📚 Struktur Repositori & Isi Tugas
Website dokumentasi ini dibuat menggunakan **Jupyter Book / MyST Markdown** dan dideploy secara otomatis menggunakan **GitHub Actions** ke **GitHub Pages**.

- **`Notebooks/`**: Berisi materi Jupyter Book dan notebook praktikum.
  - [`index.ipynb`](Notebooks/index.ipynb): Halaman beranda & profil mahasiswa.
  - [`WebMining_Tugas1.ipynb`](Notebooks/WebMining_Tugas1.ipynb): Tugas 1 - Crawling & Ekstraksi Teks Berita Olahraga dengan *Trafilatura*.
  - `_config.yml` & `_toc.yml`: Konfigurasi struktur dan navigasi buku Jupyter.
- **`mytugaswebmining/`**: Project web scraper berbasis framework Scrapy.
- **`.github/workflows/deploy.yml`**: Alur kerja CI/CD untuk otomatisasi build dan deployment Jupyter Book ke GitHub Pages.

---

## 🚀 Menjalankan Secara Lokal

1. **Clone repositori**:
   ```bash
   git clone https://github.com/ilham08-GH/ppw.git
   cd ppw
   ```

2. **Install dependensi**:
   ```bash
   pip install jupyter-book trafilatura pandas ipykernel
   ```

3. **Build dan buka Jupyter Book**:
   ```bash
   jupyter-book build Notebooks
   ```
   Buka file `Notebooks/_build/html/index.html` pada browser Anda.
