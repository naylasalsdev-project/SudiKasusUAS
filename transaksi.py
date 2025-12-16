# transaksi.py
from connection import get_connection
from PyQt5 import QtCore, QtGui, QtWidgets

class Transaksi:
    def __init__(self, id_transaksi=None, id_pemeriksaan=None, tanggal=None, total_bayar=None):
        self.id_transaksi = id_transaksi
        self.id_pemeriksaan = id_pemeriksaan
        self.tanggal = tanggal
        self.total_bayar = total_bayar

    # ================= INSERT =================
    def insert(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO transaksi (id_pemeriksaan, tanggal, total_bayar)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (
            self.id_pemeriksaan,
            self.tanggal,
            self.total_bayar
        ))
        conn.commit()

        # ambil id_transaksi terakhir (penting buat detail_transaksi)
        self.id_transaksi = cursor.lastrowid

        conn.close()
        return self.id_transaksi

    # ================= DISPLAY =================
    @staticmethod
    def display():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                t.id_transaksi,
                p.id_pemeriksaan,
                d.nama_dokter,
                pr.nama_perawat,
                ps.nama_pasien,
                t.tanggal,
                t.total_bayar
            FROM transaksi t
            JOIN pemeriksaan p ON t.id_pemeriksaan = p.id_pemeriksaan
            JOIN dokter d ON p.id_dokter = d.id_dokter
            JOIN perawat pr ON p.id_perawat = pr.id_perawat
            JOIN pasien ps ON p.id_pasien = ps.id_pasien
        """)
        data = cursor.fetchall()
        conn.close()
        return data

    # ================= DELETE =================
    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM transaksi WHERE id_transaksi = %s",
            (self.id_transaksi,)
        )
        conn.commit()
        conn.close()

    # ================= CEK SUDAH TRANSAKSI =================
    @staticmethod
    def cek_transaksi(id_pemeriksaan):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM transaksi WHERE id_pemeriksaan = %s",
            (id_pemeriksaan,)
        )
        data = cursor.fetchone()
        conn.close()
        return data

    # ================= CARI BY PEMERIKSAAN =================
    @staticmethod
    def cari_by_pemeriksaan(id_pemeriksaan):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT 
                d.nama_dokter,
                pr.nama_perawat,
                ps.nama_pasien,
                ps.penyakit,
                p.tgl_pemeriksaan,
                t.total_bayar,
                l.nama_layanan
            FROM transaksi t
            JOIN pemeriksaan p ON t.id_pemeriksaan = p.id_pemeriksaan
            JOIN dokter d ON p.id_dokter = d.id_dokter
            JOIN perawat pr ON p.id_perawat = pr.id_perawat
            JOIN pasien ps ON p.id_pasien = ps.id_pasien
            JOIN detail_transaksi dt ON t.id_transaksi = dt.id_transaksi
            JOIN layanan l ON dt.id_layanan = l.id_layanan
            WHERE t.id_pemeriksaan = %s
        """, (id_pemeriksaan,))

        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return None

        nama_dokter = rows[0][0]
        nama_perawat = rows[0][1]
        nama_pasien = rows[0][2]
        penyakit = rows[0][3]
        tgl_pemeriksaan = rows[0][4]
        total_bayar = rows[0][5]

        layanan = [row[6] for row in rows]

        return (
            nama_dokter,
            nama_perawat,
            nama_pasien,
            penyakit,
            tgl_pemeriksaan,
            total_bayar,
            layanan
        )

    # ================= DELETE BY PEMERIKSAAN =================
    @staticmethod
    def delete_by_pemeriksaan(id_pemeriksaan):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM transaksi WHERE id_pemeriksaan = %s",
            (id_pemeriksaan,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def riwayat(id_transaksi=None):
        conn = get_connection()
        cursor = conn.cursor()

        if id_transaksi:
            cursor.execute("""
                SELECT 
                    t.id_transaksi,
                    p.id_pemeriksaan,
                    ps.nama_pasien,
                    ps.penyakit,
                    t.tanggal,
                    t.total_bayar
                FROM transaksi t
                JOIN pemeriksaan p ON t.id_pemeriksaan = p.id_pemeriksaan
                JOIN pasien ps ON p.id_pasien = ps.id_pasien
                WHERE t.id_transaksi = %s
            """, (id_transaksi,))
        else:
            cursor.execute("""
                SELECT 
                    t.id_transaksi,
                    p.id_pemeriksaan,
                    ps.nama_pasien,
                    ps.penyakit,
                    t.tanggal,
                    t.total_bayar
                FROM transaksi t
                JOIN pemeriksaan p ON t.id_pemeriksaan = p.id_pemeriksaan
                JOIN pasien ps ON p.id_pasien = ps.id_pasien
                ORDER BY t.tanggal DESC
            """)

        data = cursor.fetchall()
        conn.close()
        return data

    def tampilkan_data(self, data):
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(data):
            self.tableWidget.insertRow(row_number)

            for column_number, value in enumerate(row_data):

                # kalau tipe tanggal
                if hasattr(value, "strftime"):
                    value = value.strftime("%d-%m-%Y")

                self.tableWidget.setItem(
                    row_number,
                    column_number,
                    QtWidgets.QTableWidgetItem(str(value)))

