from subclass_dokter import Dokter
from subclass_perawat import Perawat
from subclass_pasien import Pasien

dokter = Dokter()
perawat = Perawat()
pasien = Pasien()

def menu_utama():
    print("\n=== SISTEM RUMAH SAKIT ===")
    print("1. Kelola Data Dokter")
    print("2. Kelola Data Perawat")
    print("3. Kelola Data Pasien")
    print("0. Keluar")

def menu_crud(nama):
    print(f"\n=== MENU {nama.upper()} ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("0. Kembali")

while True:
    menu_utama()
    pilih = input("Pilih menu: ")

    # =====================
    #  MENU DOKTER
    # =====================
    if pilih == "1":
        while True:
            menu_crud("Dokter")
            aksi = input("Pilih aksi: ")

            if aksi == "1":
                print("\n=== TAMBAH DATA DOKTER ===")
                id = input("Masukkan ID Dokter: ")
                nama = input("Masukkan Nama Dokter: ")
                umur = int(input("Masukkan Umur Dokter: "))
                spesialis = input("Masukkan Spesialis: ")
                dokter.insert(id, nama, umur, spesialis)

            elif aksi == "2":
                print("\n=== DATA DOKTER ===")
                dokter.display()

            elif aksi == "3":
                print("\n=== UPDATE DATA DOKTER ===")
                id = input("Masukkan ID Dokter: ")
                nama_baru = input("Masukkan Nama Baru: ")
                umur_baru = int(input("Masukkan Umur Baru: "))
                spesialis_baru = input("Masukkan Spesialis Baru: ")
                dokter.update(id, nama_baru, umur_baru, spesialis_baru)

            elif aksi == "4":
                print("\n=== HAPUS DATA DOKTER ===")
                id = input("Masukkan ID Dokter: ")
                dokter.delete(id)

            elif aksi == "0":
                break
            else:
                print("Pilihan tidak valid.")

    # =====================
    #  MENU PERAWAT
    # =====================
    elif pilih == "2":
        while True:
            menu_crud("Perawat")
            aksi = input("Pilih aksi: ")

            if aksi == "1":
                print("\n=== TAMBAH DATA PERAWAT ===")
                id = input("Masukkan ID Perawat: ")
                nama = input("Masukkan Nama Perawat: ")
                umur = int(input("Masukkan Umur Perawat: "))
                shift = input("Masukkan Shift (Pagi/Siang/Malam): ")
                perawat.insert(id, nama, umur, shift)

            elif aksi == "2":
                print("\n=== DATA PERAWAT ===")
                perawat.display()

            elif aksi == "3":
                print("\n=== UPDATE DATA PERAWAT ===")
                id = input("Masukkan ID Perawat: ")
                nama_baru = input("Masukkan Nama Baru: ")
                umur_baru = int(input("Masukkan Umur Baru: "))
                shift_baru = input("Masukkan Shift Baru: ")
                perawat.update(id, nama_baru, umur_baru, shift_baru)

            elif aksi == "4":
                print("\n=== HAPUS DATA PERAWAT ===")
                id = input("Masukkan ID Perawat: ")
                perawat.delete(id)

            elif aksi == "0":
                break
            else:
                print("Pilihan tidak valid.")

    # =====================
    #  MENU PASIEN
    # =====================
    elif pilih == "3":
        while True:
            menu_crud("Pasien")
            aksi = input("Pilih aksi: ")

            if aksi == "1":
                print("\n=== TAMBAH DATA PASIEN ===")
                id = input("Masukkan ID Pasien: ")
                nama = input("Masukkan Nama Pasien: ")
                umur = int(input("Masukkan Umur Pasien: "))
                penyakit = input("Masukkan Penyakit: ")
                pasien.insert(id, nama, umur, penyakit)

            elif aksi == "2":
                print("\n=== DATA PASIEN ===")
                pasien.display()

            elif aksi == "3":
                print("\n=== UPDATE DATA PASIEN ===")
                id = input("Masukkan ID Pasien: ")
                nama_baru = input("Masukkan Nama Baru: ")
                umur_baru = int(input("Masukkan Umur Baru: "))
                penyakit_baru = input("Masukkan Penyakit Baru: ")
                pasien.update(id, nama_baru, umur_baru, penyakit_baru)

            elif aksi == "4":
                print("\n=== HAPUS DATA PASIEN ===")
                id = input("Masukkan ID Pasien: ")
                pasien.delete(id)

            elif aksi == "0":
                break
            else:
                print("Pilihan tidak valid.")

    elif pilih == "0":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")