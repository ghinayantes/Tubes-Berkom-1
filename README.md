# 🛗 Elevator Simulation (Simulasi Lift)

Sebuah program simulasi logika lift sederhana berbasis terminal yang ditulis menggunakan **Python**. Program ini mensimulasikan pergerakan lift berdasarkan permintaan penumpang, kapasitas berat, dan optimasi arah (naik/turun).



## 🚀 Fitur Utama

* **Manajemen Kapasitas:** Menghitung berat total penumpang untuk mencegah kelebihan beban (overload) sesuai limit yang ditentukan.
* **Logika Pergerakan Dinamis:** Lift akan bergerak naik atau turun secara cerdas berdasarkan lokasi penjemputan dan tujuan penumpang.
* **Antrean Penumpang:** Mendukung input penumpang awal (di dalam lift) dan penumpang yang menunggu di berbagai lantai.
* **Otomatisasi Idle:** Setelah semua tugas selesai, lift secara otomatis kembali ke Lantai 1 (Ground Floor).
* **Visualisasi Terminal:** Output langkah-demi-langkah yang informatif disertai dengan emoji dan jeda waktu (*real-time feel*).

## 🛠️ Cara Penggunaan

1.  **Persyaratan:** Pastikan kamu sudah menginstal [Python 3.x](https://www.python.org/).
2.  **Clone Repositori:**
    ```bash
    git clone [https://github.com/username-kamu/simulasi-lift.git](https://github.com/username-kamu/simulasi-lift.git)
    cd simulasi-lift
    ```
3.  **Jalankan Program:**
    ```bash
    python nama_file_kamu.py
    ```

## 🎮 Alur Simulasi

1.  **Setup Awal:** Tentukan jumlah lantai, posisi awal lift, dan kapasitas berat maksimal (kg).
2.  **Input Penumpang:**
    * Masukkan jumlah penumpang yang sudah ada di dalam lift beserta tujuannya.
    * Input data orang yang mengantre di setiap lantai (jika ada).
3.  **Eksekusi:** Program akan menjalankan loop simulasi hingga semua penumpang sampai di tujuan.
4.  **Logika Arah:** Lift menggunakan algoritma sederhana untuk menyelesaikan semua tujuan ke satu arah sebelum berbalik arah.

## 📋 Contoh Tampilan Output
```text
───────────── LANGKAH #3 ─────────────
⬆️  Lift naik ke lantai 3
🚪 Pintu terbuka di lantai 3
  1 orang turun, 2 orang naik di lantai 3
  Berat lift sekarang: 130 kg
