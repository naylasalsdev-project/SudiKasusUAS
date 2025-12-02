from superclass import User

class Perawat(User):
    def _init_(self):
        super()._init_()

    def insert(self, id, nama, umur, shift):
        super().insert(id, nama, umur)
        sql = "INSERT INTO perawat (id, shift) VALUES (%s, %s)"
        val = (id, shift)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("1 data perawat berhasil ditambahkan.")

    def display(self):
        sql = """
        SELECT user.id, user.nama, user.umur, perawat.shift
        FROM perawat
        JOIN user ON perawat.id = user.id
        """
        self.mycursor.execute(sql)
        hasil = self.mycursor.fetchall()
        for x in hasil:
            print(x)

    def update(self, id, nama_baru, umur_baru, shift_baru):
        super().update(id, nama_baru, umur_baru)
        sql = "UPDATE perawat SET shift = %s WHERE id = %s"
        val = (shift_baru, id)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("Data perawat berhasil diupdate.")

    def delete(self, id):
        super().delete(id)
        print("Data perawat berhasil dihapus dari sistem (termasuk user).")

    def bantu(self, pasien):
        print(f"Perawat sedang membantu pasien {pasien}.")