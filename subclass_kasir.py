from superclass import User
from connection import get_connection

class Kasir(User):
    def __init__(self, id, nama, umur, id_level, id_kasir, username, password):
        super().__init__(id, nama, umur, id_level)
        self._id_kasir = id_kasir
        self._username = username
        self._password = password
        self.table_name = "kasir"

    def Hitung_harga_total(self, pemeriksaan_id):
        print(f"Kasir {self._username} sedang menghitung total harga untuk Pemeriksaan ID: {pemeriksaan_id}...")
        return 150000
    
    def create(self):
        super().create()
        conn = get_connection()
        cursor = conn.cursor()
        query = f"""
            INSERT INTO {self.table_name} (id_kasir, username, password)
            VALUES (%s, %s, %s)
        """
        data = (self._id_kasir, self._username, self._password)
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        print(f"-> Detail Kasir '{self._username}' berhasil ditambahkan.")

    @classmethod
    def display(cls):
        conn = get_connection()
        cursor = conn.cursor()
        query = f"SELECT id_kasir, username FROM {cls().table_name}"
        cursor.execute(query)
        results = cursor.fetchall()
        print("\n--- Data Kasir (Detail) ---")
        for row in results:
            print(f"ID Kasir: {row[0]}, Username: {row[1]}")
        conn.close()
        return results

    def update(self):
        super().update()
        conn = get_connection()
        cursor = conn.cursor()
        query = f"""
            UPDATE {self.table_name}
            SET username = %s, password = %s
            WHERE id_kasir = %s
        """
        data = (self._username, self._password, self._id_kasir)
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        print(f"-> Detail Kasir ID '{self._id_kasir}' berhasil diperbarui.")
    
    def delete(self):
        super().delete()
        conn = get_connection()
        cursor = conn.cursor()
        query = f"DELETE FROM {self.table_name} WHERE id_kasir = %s"
        data = (self._id_kasir,)
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        print(f"-> Detail Kasir ID '{self._id_kasir}' berhasil dihapus.")
    
    @staticmethod
    def cek_login(username, password):
        from connection import get_connection
        db = get_connection()
        cursor = db.cursor()

        sql = """SELECT kasir.id_kasir, user.nama
                 FROM kasir
                 JOIN user ON kasir.id_kasir = user.id
                 WHERE kasir.username=%s AND kasir.password=%s"""
        
        cursor.execute(sql, (username, password))
        hasil = cursor.fetchone()

        cursor.close()
        db.close()
        return hasil

    @classmethod
    def select_by_id(cls, kasir_id):
        conn = get_connection()
        cursor = conn.cursor()
        query = f"SELECT id_kasir, username FROM {cls().table_name} WHERE id_kasir = %s"
        cursor.execute(query, (kasir_id,))
        result = cursor.fetchone()
        
        conn.close()
        
        if result:
            print(f"-> Kasir ditemukan: ID {result[0]}, Username {result[1]}")
        else:
            print(f"-> Kasir dengan ID '{kasir_id}' tidak ditemukan.")
            
        return result