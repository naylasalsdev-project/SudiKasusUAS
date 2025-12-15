from connection import get_connection

class Level:
    def __init__(self):
        self

    @staticmethod
    def select_data():
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT id_level, nama_level FROM level ORDER BY id_level ASC")
        return cursor.fetchall()


    def insert_data(val1):
        db = get_connection()
        cursor = db.cursor()
        sql = "INSERT INTO nama_level (level) VALUES (%s)"
        val = (val1)
        cursor.execute(sql, val)
        db.commit()
        print(cursor.rowcount, "Data berhasil ditambahkan...")
    
    @classmethod
    def get_admin_kasir_levels(cls):
        """Mengambil hanya level Admin dan Kasir langsung dari database."""
        conn = get_connection()
        cursor = conn.cursor()
        
        # Menggunakan nama level yang ditemukan di dropdown Anda ('admin', 'kasir')
        query = """
            SELECT id_level, nama_level 
            FROM level 
            WHERE nama_level IN ('admin', 'kasir') 
            ORDER BY id_level ASC
        """
        
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results

    