from connection import get_connection
from superclass import User

class Perawat(User):
    def __init__(self, id, nama, umur, shift=None, id_level=None):
        # Jika id_level tidak diberikan, tetapkan berdasarkan shift (opsional)
        if id_level is None:
            shift_lower = (shift or "").lower()
            if "malam" in shift_lower:
                id_level = 6
            else:
                id_level = 5
        super().__init__(id, nama, umur, id_level)
        self.__shift = shift

    def insert(self):
        super().insert()  # insert ke tabel user dulu
        db = get_connection()
        cursor = db.cursor()
        sql = "INSERT INTO perawat (id_perawat) VALUES (%s)"  # hanya id_perawat
        cursor.execute(sql, (self.get_id(),))
        db.commit()
        cursor.close()
        db.close()
        print("Perawat berhasil ditambahkan!")

    @staticmethod
    def display():
        db = get_connection()
        cursor = db.cursor()
        # Query tanpa kolom 'shift' karena tidak ada di tabel perawat
        cursor.execute(
            """SELECT perawat.id_perawat, user.nama, user.umur
               FROM perawat JOIN user ON perawat.id_perawat=user.id"""
        )
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        db.close()

    def update(self, nama, umur):
        # Update USER saja
        self.set_nama(nama)
        self.set_umur(umur)
        super().update()
        print("Perawat berhasil diupdate!")

    def delete(self):
        # Pastikan juga hapus data di tabel perawat jika DB tidak auto cascade
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM perawat WHERE id_perawat=%s", (self.get_id(),))
        db.commit()
        cursor.close()
        db.close()

        # Hapus di tabel user
        super().delete(self.get_id())

    @staticmethod
    def select_by_id(id_perawat):
        db = get_connection()
        cursor = db.cursor()
        # Query tanpa kolom 'shift'
        sql = """SELECT perawat.id_perawat, user.nama, user.umur
                 FROM perawat
                 JOIN user ON perawat.id_perawat = user.id
                 WHERE perawat.id_perawat=%s"""
        cursor.execute(sql, (id_perawat,))
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return data
