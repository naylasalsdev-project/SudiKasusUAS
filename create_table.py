import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sistem_rumah_sakit"
)

cursor = mydb.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS user (id VARCHAR(10) PRIMARY KEY, nama VARCHAR(100),umur INT)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS dokter (id VARCHAR(10), spesialis VARCHAR(100), FOREIGN KEY (id) REFERENCES user(id) ON UPDATE CASCADE ON DELETE CASCADE)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS perawat (id VARCHAR(10), shift VARCHAR(50), FOREIGN KEY (id) REFERENCES user(id) ON UPDATE CASCADE ON DELETE CASCADE)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS pasien (id VARCHAR(10), penyakit VARCHAR(100), FOREIGN KEY (id) REFERENCES user(id) ON UPDATE CASCADE ON DELETE CASCADE)""")