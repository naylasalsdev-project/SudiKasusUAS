import mysql.connector

class User:
    def _init_(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sistem_rumah_sakit"
        )
        self.mycursor = self.mydb.cursor()

    def insert(self, id, nama, umur):
        sql = "INSERT INTO user (id, nama, umur) VALUES (%s, %s, %s)"
        val = (id, nama, umur)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("1 data user berhasil ditambahkan.")

    def display(self):
        self.mycursor.execute("SELECT * FROM user")
        hasil = self.mycursor.fetchall()
        for x in hasil:
            print(x)

    def update(self, id, nama_baru, umur_baru):
        sql = "UPDATE user SET nama = %s, umur = %s WHERE id = %s"
        val = (nama_baru, umur_baru, id)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "data user berhasil diupdate.")

    def delete(self, id):
        sql = "DELETE FROM user WHERE id = %s"
        val = (id,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "data user berhasil dihapus.")