from superclass import User

class Pasien(User):
    def _init_(self):
        super()._init_()

    def insert(self, id, nama, umur, penyakit):
        super().insert(id, nama, umur)
        sql = "INSERT INTO pasien (id, penyakit) VALUES (%s, %s)"
        val = (id, penyakit)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("1 data pasien berhasil ditambahkan.")

    def display(self):
        sql = """
        SELECT user.id, user.nama, user.umur, pasien.penyakit
        FROM pasien
        JOIN user ON pasien.id = user.id
        """
        self.mycursor.execute(sql)
        hasil = self.mycursor.fetchall()
        for x in hasil:
            print(x)

    def update(self, id, nama_baru, umur_baru, penyakit_baru):
        super().update(id, nama_baru, umur_baru)
        sql = "UPDATE pasien SET penyakit = %s WHERE id = %s"
        val = (penyakit_baru, id)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("Data pasien berhasil diupdate.")

    def delete(self, id):
        super().delete(id)
        print("Data pasien berhasil dihapus dari sistem (termasuk user).")