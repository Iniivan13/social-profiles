# OSINT Social Profiles Tool

## Deskripsi

OSINT Social Profiles Tool adalah alat berbasis Python yang membantu pengguna mencari profil media sosial berdasarkan nama pengguna. Tool ini memanfaatkan mesin pencari untuk menemukan akun yang relevan di berbagai platform media sosial.

## Fitur

- **Rotasi User-Agent:** Menggunakan berbagai User-Agent untuk mencegah pemblokiran oleh mesin pencari.
- **Dukungan Multi Mesin Pencari:** Mendukung 10+ mesin pencari seperti Google, Bing, DuckDuckGo, dan lainnya.
- **Pencarian Media Sosial:** Mendukung lebih dari 30 domain media sosial populer, termasuk Facebook, Instagram, LinkedIn, dan Twitter.
- **Output:** Menampilkan hasil di terminal dan menyimpannya di folder khusus.

## Instalasi

1. **Kloning Repository**

   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. **Install Dependencies**

   Pastikan Anda memiliki Python 3.x terinstal di sistem Anda. Install library yang diperlukan dengan menjalankan:

   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Program**

   ```bash
   python main.py
   ```

## Cara Menggunakan

1. Pilih opsi dari menu utama:
   - Pilih opsi `1` untuk mencari profil media sosial.
   - Pilih opsi `2` untuk keluar dari program.

2. Masukkan nama pengguna yang ingin Anda cari, lalu tekan Enter. Tool akan mencari profil yang relevan dan menampilkan hasilnya di terminal.

3. Hasil pencarian akan disimpan secara otomatis di folder `output` dalam file bernama `results_<username>.txt`.

## Struktur Direktori

```
.
├── main.py              # File utama program
├── requirements.txt     # Daftar dependensi
├── output/              # Folder untuk menyimpan hasil pencarian
└── README.md            # File panduan
```

## Output

Hasil pencarian ditampilkan di terminal dan disimpan di folder `output` dengan format berikut:

```text
Profil Media Sosial yang Ditemukan:
1. Platform: INSTAGRAM, URL: https://www.instagram.com/example/
2. Platform: FACEBOOK, URL: https://www.facebook.com/example/
```

## Kontribusi

Kontribusi sangat dihargai! Silakan buat pull request atau buka issue jika Anda memiliki ide atau menemukan bug.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE)

## Kontak

Untuk informasi lebih lanjut, kunjungi halaman Instagram kami: [@lampungcysec](https://www.instagram.com/lampungcysec/)