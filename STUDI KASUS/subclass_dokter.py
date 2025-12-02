from superclass import User

class Dokter(User):
    def _init_(self):
        super()._init_()

    def insert(self, id, nama, umur, spesialis):
        # Tambahkan ke tabel user dulu
        super().insert(id, nama, umur)
        # Lalu ke tabel dokter
        sql = "INSERT INTO dokter (id, spesialis) VALUES (%s, %s)"
        val = (id, spesialis)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("1 data dokter berhasil ditambahkan.")

    def display(self):
        sql = """
        SELECT user.id, user.nama, user.umur, dokter.spesialis
        FROM dokter
        JOIN user ON dokter.id = user.id
        """
        self.mycursor.execute(sql)
        hasil = self.mycursor.fetchall()
        for x in hasil:
            print(x)

    def update(self, id, nama_baru, umur_baru, spesialis_baru):
        super().update(id, nama_baru, umur_baru)
        sql = "UPDATE dokter SET spesialis = %s WHERE id = %s"
        val = (spesialis_baru, id)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("Data dokter berhasil diupdate.")

    def delete(self, id):
        super().delete(id)
        print("Data dokter berhasil dihapus dari sistem (termasuk user).")

    def periksa(self, pasien):
        print(f"Dokter sedang memeriksa pasien {pasien}.")