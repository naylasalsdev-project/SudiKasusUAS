class Orang:
    def _init_(self, nama, umur):
        self._nama = nama
        self._umur = umur

    def tampil_info(self):
        print(f"Nama: {self._nama}, Umur: {self._umur} tahun")

class Dokter(Orang):
    _counter = 1

    def _init_(self, nama, umur, spesialis):
        super()._init_(nama, umur)
        self._id_dokter = f"D{Dokter._counter}"
        Dokter._counter += 1
        self._spesialis = spesialis

    def tampil_info(self):
        print(f"[{self._id_dokter}] Dokter {self._nama} ({self._umur} th) - Spesialis {self._spesialis}")

    def periksa(self, pasien):
        print(f"Dokter {self._nama} memeriksa pasien {pasien._nama}")


class Perawat(Orang):
    _counter = 1

    def _init_(self, nama, umur, shift):
        super()._init_(nama, umur)
        self._id_perawat = f"P{Perawat._counter}"
        Perawat._counter += 1
        self._shift = shift

    def tampil_info(self):
        print(f"[{self._id_perawat}] Perawat {self._nama} ({self._umur} th) - Shift {self._shift}")

    def bantu(self):
        print(f"Perawat {self._nama} membantu pemeriksaan")

class Pasien(Orang):
    _counter = 1

    def _init_(self, nama, umur, penyakit):
        super()._init_(nama, umur)
        self._id_pasien = f"S{Pasien._counter}"
        Pasien._counter += 1
        self._penyakit = penyakit

    def tampil_info(self):
        print(f"[{self._id_pasien}] Pasien {self._nama} ({self._umur} th) - Penyakit: {self._penyakit}")


class Pemeriksaan:
    _counter = 1

    def _init_(self, dokter, perawat, pasien):
        self._id_periksa = f"PR{Pemeriksaan._counter}"
        Pemeriksaan._counter += 1
        self._dokter = dokter
        self._perawat = perawat
        self._pasien = pasien

    def tampil_info(self):
        print(f"[{self._id_periksa}] Dokter: {self._dokter._nama}, Perawat: {self._perawat._nama}, Pasien: {self._pasien._nama}")


dokter_list = []
perawat_list = []
pasien_list = []
pemeriksaan_list = []

def tambah_dokter():
    nama = input("Nama dokter: ")
    umur = int(input("Umur: "))
    spesialis = input("Spesialis: ")
    dokter_list.append(Dokter(nama, umur, spesialis))
    print("Dokter ditambahkan.")

def lihat_dokter():
    if not dokter_list:
        print("Belum ada dokter.")
    else:
        for d in dokter_list:
            d.tampil_info()

def update_dokter():
    lihat_dokter()
    if not dokter_list: return
    id_dok = input("Masukkan ID Dokter: ")
    d = next((x for x in dokter_list if x._id_dokter == id_dok), None)
    if d:
        nama = input("Nama baru (enter lewati): ")
        umur = input("Umur baru (enter lewati): ")
        spesialis = input("Spesialis baru (enter lewati): ")

        if nama: d._nama = nama
        if umur: d._umur = int(umur)
        if spesialis: d._spesialis = spesialis
        print("Data dokter diperbarui.")
    else:
        print("ID tidak ditemukan.")

def hapus_dokter():
    lihat_dokter()
    if not dokter_list: return
    id_dok = input("Masukkan ID Dokter yang akan dihapus: ")
    for d in dokter_list:
        if d._id_dokter == id_dok:
            dokter_list.remove(d)
            print(f"Dokter '{d._nama}' dihapus.")
            return
    print("ID tidak ditemukan.")

def tambah_perawat():
    nama = input("Nama perawat: ")
    umur = int(input("Umur: "))
    shift = input("Shift: ")
    perawat_list.append(Perawat(nama, umur, shift))
    print("Perawat ditambahkan.")

def lihat_perawat():
    if not perawat_list:
        print("Belum ada perawat.")
    else:
        for p in perawat_list:
            p.tampil_info()

def update_perawat():
    lihat_perawat()
    if not perawat_list: return
    id_per = input("Masukkan ID Perawat: ")
    p = next((x for x in perawat_list if x._id_perawat == id_per), None)
    if p:
        nama = input("Nama baru (enter lewati): ")
        umur = input("Umur baru (enter lewati): ")
        shift = input("Shift baru (enter lewati): ")

        if nama: p._nama = nama
        if umur: p._umur = int(umur)
        if shift: p._shift = shift
        print("Data perawat diperbarui.")
    else:
        print("ID tidak ditemukan.")

def hapus_perawat():
    lihat_perawat()
    if not perawat_list: return
    id_per = input("Masukkan ID Perawat yang akan dihapus: ")
    for p in perawat_list:
        if p._id_perawat == id_per:
            perawat_list.remove(p)
            print(f"Perawat '{p._nama}' dihapus.")
            return
    print("ID tidak ditemukan.")

def tambah_pasien():
    nama = input("Nama pasien: ")
    umur = int(input("Umur: "))
    penyakit = input("Penyakit: ")
    pasien_list.append(Pasien(nama, umur, penyakit))
    print("Pasien ditambahkan.")

def lihat_pasien():
    if not pasien_list:
        print("Belum ada pasien.")
    else:
        for ps in pasien_list:
            ps.tampil_info()

def update_pasien():
    lihat_pasien()
    if not pasien_list: return
    id_pas = input("Masukkan ID Pasien: ")
    ps = next((x for x in pasien_list if x._id_pasien == id_pas), None)
    if ps:
        nama = input("Nama baru (enter lewati): ")
        umur = input("Umur baru (enter lewati): ")
        penyakit = input("Penyakit baru (enter lewati): ")

        if nama: ps._nama = nama
        if umur: ps._umur = int(umur)
        if penyakit: ps._penyakit = penyakit
        print("Data pasien diperbarui.")
    else:
        print("ID tidak ditemukan.")

def hapus_pasien():
    lihat_pasien()
    if not pasien_list: return
    id_pas = input("Masukkan ID Pasien yang akan dihapus: ")
    for ps in pasien_list:
        if ps._id_pasien == id_pas:
            pasien_list.remove(ps)
            print(f"Pasien '{ps._nama}' dihapus.")
            return
    print("ID tidak ditemukan.")

def pemeriksaan():
    if not dokter_list or not perawat_list or not pasien_list:
        print("Data belum lengkap.")
        return

    print("\nPilih Dokter:")
    lihat_dokter()
    id_dok = input("ID Dokter: ")
    dokter = next((x for x in dokter_list if x._id_dokter == id_dok), None)

    print("\nPilih Perawat:")
    lihat_perawat()
    id_per = input("ID Perawat: ")
    perawat = next((x for x in perawat_list if x._id_perawat == id_per), None)

    print("\nPilih Pasien:")
    lihat_pasien()
    id_pas = input("ID Pasien: ")
    pasien = next((x for x in pasien_list if x._id_pasien == id_pas), None)

    if dokter and perawat and pasien:
        periksa_baru = Pemeriksaan(dokter, perawat, pasien)
        pemeriksaan_list.append(periksa_baru)
        print("Pemeriksaan berhasil dibuat.")
        periksa_baru.tampil_info()
    else:
        print("ID tidak valid.")

def menu_crud(title, create, read, update, delete):
    while True:
        print(f"\n--- {title.upper()} ---")
        print("1. Tambah")
        print("2. Lihat")
        print("3. Update")
        print("4. Hapus")
        print("0. Kembali")
        c = input("Pilih: ")
        if c == "1": create()
        elif c == "2": read()
        elif c == "3": update()
        elif c == "4": delete()
        elif c == "0": break
        else: print("Pilihan tidak valid.")


def main_menu():
    while True:
        print("\n=== SISTEM RUMAH SAKIT ===")
        print("1. Dokter")
        print("2. Perawat")
        print("3. Pasien")
        print("4. Pemeriksaan")
        print("5. Lihat Semua Pemeriksaan")
        print("0. Keluar")
        c = input("Pilih menu: ")
        if c == "1": menu_crud("Dokter", tambah_dokter, lihat_dokter, update_dokter, hapus_dokter)
        elif c == "2": menu_crud("Perawat", tambah_perawat, lihat_perawat, update_perawat, hapus_perawat)
        elif c == "3": menu_crud("Pasien", tambah_pasien, lihat_pasien, update_pasien, hapus_pasien)
        elif c == "4": pemeriksaan()
        elif c == "5":
            if not pemeriksaan_list:
                print("Belum ada pemeriksaan.")
            else:
                for p in pemeriksaan_list:
                    p.tampil_info()
        elif c == "0":
            print("Terima kasih")
            break
        else: print("Pilihan tidak valid.")

main_menu()