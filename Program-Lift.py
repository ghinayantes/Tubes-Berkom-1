print("=== SIMULASI LIFT ===")
import os
import time


# INITIALISASI / INPUT SET UP
max_lantai = int(input("Masukkan jumlah lantai (>=2): "))
posisi = int(input("Masukkan posisi awal lift: "))
if posisi < 1:
    posisi = 1
    print("Lantai lift diset menjadi 1.")
if posisi > max_lantai:
    posisi = max_lantai
    print(f"Lift lantai diset menjadi {max_lantai}.")


kapasitas_berat = int(input("Masukkan kapasitas berat lift (kg): "))
berat_orang = 65  # berat rata-rata per orang (kg)
berat_sekarang = 0


print("\n(*Arah awal ditentukan dari tujuan pertama penumpang*)")


# VARIABLES
MAX_ORANG = 200
asal = [0] * MAX_ORANG
tujuan = [0] * MAX_ORANG
sudah_naik = [False] * MAX_ORANG
sudah_turun = [False] * MAX_ORANG
n_orang = 0
arah_ditentukan = False
is_naik = True #sesuaikan


# PENUMPANG AWAL YG DALAM LIFT
valid_awal = False
while not valid_awal:
    banyak_awal = int(input("\nMasukkan banyak penumpang awal di dalam lift: "))
    if banyak_awal*berat_orang >  kapasitas_berat:
        print(" Penumpang melebihi kapasitas berat!")
    else:
        valid_awal = True


i = 0
while i < banyak_awal and n_orang < MAX_ORANG:
    d = int(input(f"  Penumpang awal ingin ke lantai: "))
    if 1 <= d <= max_lantai and d != posisi:
        asal[n_orang] = posisi
        tujuan[n_orang] = d
        sudah_naik[n_orang] = True
        n_orang += 1
        berat_sekarang += berat_orang
        if not arah_ditentukan:
            is_naik = (d > posisi)
            arah_ditentukan = True
        i += 1
    else:
        print("lantai tidak valid atau sama dengan posisi sekarang !")


# PENUMPANG STAND BY
print("\n=== INPUT PENUMPANG YANG MENUNGGU DI SETIAP LANTAI ===")
for i in range(max_lantai):
    jawab = input(f"Ada yang mau naik lift di lantai {i+1}? (y/n): ")
    if jawab.lower() == "y":
        banyak = int(input("  Berapa orang di lantai ini? "))
        j = 0
        while j < banyak and n_orang < MAX_ORANG:
            d = int(input(f"    ➜ Tujuan orang ke-{j+1}: "))
            if 1 <= d <= max_lantai and d != i+1:
                asal[n_orang] = i+1
                tujuan[n_orang] = d
                sudah_naik[n_orang] = False
                sudah_turun[n_orang] = False
                n_orang += 1
                if not arah_ditentukan:
                    is_naik = (d > i+1)
                    arah_ditentukan = True
                j += 1
            else:
                print("    -> Abaikan (lantai tidak valid / sama).")




# SIMULASI MULAI
print("\n=== MULAI SIMULASI ===")
print(f"Posisi awal: Lantai {posisi}")
print(f"Kapasitas berat: {kapasitas_berat} kg")
if is_naik:
    print("Arah awal: Naik ⬆️")
else:
    print("Arah awal: Turun ⬇️")
print(f"Berat awal: {berat_sekarang} kg")


step = 1
kelar = False
while not kelar:
    print(f"\n───────────── LANGKAH #{step} ─────────────")
    step += 1


    # cek apakah masih ada penumpang aktif
    aktif = False
    for i in range(n_orang):
        if not sudah_turun[i]:
            aktif = True
    if not aktif:
        if posisi > 1:
            while posisi > 1:
                posisi -= 1
                print(f"⬇️  Lift turun ke lantai {posisi}")
        print("✅ Semua penumpang selesai. Lift idle di lantai 1.")
        kelar = True


    if not kelar:
          #NAIK
        if is_naik:
            ada_tujuan = False
            i = 0
            for i in range(n_orang):
                if (not sudah_turun[i]) and ((not sudah_naik[i] and asal[i] >= posisi) or (sudah_naik[i] and tujuan[i] > posisi)):
                    ada_tujuan = True


            if not ada_tujuan:
                print("↩️  Tidak ada tujuan di atas, arah diubah ke TURUN")
                is_naik = False


            if posisi < max_lantai:
                posisi += 1
                print(f"⬆️  Lift naik ke lantai {posisi}")


        # TURUN
        else:
            ada_tujuan = False
            for i in range(n_orang):
                if (not sudah_turun[i]) and ((not sudah_naik[i] and asal[i] <= posisi) or(sudah_naik[i] and tujuan[i] < posisi)):
                    ada_tujuan = True


            if not ada_tujuan:
                print("↩️  Tidak ada tujuan di bawah, arah diubah ke NAIK")
                is_naik = True


            if posisi > 1:
                posisi -= 1
                print(f"⬇️  Lift turun ke lantai {posisi}")


        # NYAMPE DI LANTAI
        stop = False
        turun_count = 0
        naik_count = 0


        # turunin penumpang
        for i in range(n_orang):
            if sudah_naik[i] and not sudah_turun[i] and tujuan[i] == posisi:
                if not stop:
                    print(f"🚪 Pintu terbuka di lantai {posisi}")
                    stop = True
                sudah_turun[i] = True
                turun_count += 1
                berat_sekarang -= berat_orang


        # penumpang masukkin
        for i in range(n_orang):
            if (not sudah_naik[i]) and (asal[i] == posisi):
                berat_baru = berat_sekarang + berat_orang
                if berat_baru <= kapasitas_berat:
                    if not stop:
                        print(f"🚪 Pintu terbuka di lantai {posisi}")
                        stop = True
                    sudah_naik[i] = True
                    naik_count += 1
                    berat_sekarang = berat_baru
                else:
                    print(f"❌ Penumpang di lantai {posisi} tidak bisa naik (kapasitas berat terlampaui)")




        if stop:
            print(f"  {turun_count} orang turun, {naik_count} orang naik di lantai {posisi}")
            print(f"  Berat lift sekarang: {berat_sekarang} kg")


        time.sleep(0.8)
