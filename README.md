# PacFlix & PacCommerce

Simulasi aplikasi **streaming video (PacFlix)** dan **e-commerce membership (PacCommerce)** berbasis Python, dijalankan melalui Command Line Interface (CLI).

Project ini dibuat sebagai latihan penerapan konsep Object-Oriented Programming (OOP) di Python, meliputi class, method, dan pengelolaan data sederhana tanpa database.

## Fitur

### PacFlix (Streaming)
- Login sebagai pengguna terdaftar
- Melihat semua plan yang tersedia (Basic, Standard, Premium)
- Melihat detail plan yang sedang aktif
- Daftar sebagai pengguna baru, lengkap dengan kode referral

### PacCommerce (Belanja/Membership)
- Melihat benefit tiap tier membership (Platinum, Gold, Silver)
- Melihat requirement/syarat tiap tier membership
- Prediksi tier membership berdasarkan monthly expense & income (menggunakan perhitungan Euclidean Distance)
- Hitung total belanja setelah diskon sesuai tier membership

## Struktur Project

```
PACFLIX/
├── data/
│   ├── commerce/
│   │   └── membership_data.py     # Data benefit & requirement tiap tier
│   └── streaming/
│       └── data.py                # Data user terdaftar
├── models/
│   ├── commerce/
│   │   └── membership.py          # Class Membership (prediksi tier)
│   └── streaming/
│       ├── new_user.py            # Class NewUser (registrasi user baru)
│       └── user.py                # Class User (cek plan & benefit)
└── main.py                        # Entry point aplikasi
```

## Cara Menjalankan

1. Clone repository ini:
   ```
   git clone https://github.com/Darwisakbari/pacflix-paccommerce.git
   ```

2. Masuk ke folder project:
   ```
   cd pacflix-paccommerce
   ```

3. Install dependency yang dibutuhkan:
   ```
   pip install tabulate
   ```

4. Jalankan aplikasi:
   ```
   python main.py
   ```

## Teknologi yang Digunakan

- Python 3
- Library [tabulate](https://pypi.org/project/tabulate/) untuk menampilkan tabel di terminal

## Konsep yang Diterapkan

- Object-Oriented Programming (Class, Method, Constructor)
- Struktur data (Dictionary, List)
- Perhitungan matematis (Euclidean Distance untuk prediksi membership tier)
- Modularisasi kode (pemisahan folder data & models)

## Catatan

Data pada project ini bersifat sementara (in-memory), artinya data akan kembali ke kondisi awal setiap kali program dijalankan ulang, karena belum menggunakan database.

---

Project ini dibuat oleh Darwis Akbari sebagai bagian dari portofolio pembelajaran Python.
