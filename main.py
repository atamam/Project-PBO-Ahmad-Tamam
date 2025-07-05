# main.py

import json
import os
from models.jadwal_kerja import JadwalKerja
from models.tugas_deadline import TugasDeadline

class ManajerJadwal:
    """Class untuk mengelola daftar tugas, termasuk memuat dan menyimpan data."""
    def __init__(self, file_path='data/jadwal.json'):
        self.file_path = file_path
        self.daftar_tugas = []
        self._pastikan_folder_data_ada()
        self.muat_data()

    def _pastikan_folder_data_ada(self):
        """Memastikan direktori 'data' ada, jika tidak maka akan dibuat."""
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def tambah_tugas(self, tugas):
        """Menambahkan tugas baru ke dalam daftar."""
        self.daftar_tugas.append(tugas)
        print("--- Tugas berhasil ditambahkan! ---")

    def tampilkan_semua_tugas(self):
        """Menampilkan semua tugas yang ada di daftar."""
        if not self.daftar_tugas:
            print("--- Tidak ada tugas yang tersimpan. ---")
            return

        print("\n--- Daftar Semua Pekerjaan ---")
        for i, tugas in enumerate(self.daftar_tugas):
            # Ini adalah contoh polymorphism. Metode tampilkan_info() yang dipanggil
            # akan sesuai dengan objek aslinya (JadwalKerja atau TugasDeadline).
            print(f"{i + 1}. {tugas.tampilkan_info()}")
        print("------------------------------")
    
    def tandai_tugas_selesai(self, nomor_tugas):
        """Menandai tugas tertentu sebagai selesai berdasarkan nomor urut."""
        if 0 < nomor_tugas <= len(self.daftar_tugas):
            self.daftar_tugas[nomor_tugas - 1].tandai_selesai()
            print(f"--- Tugas nomor {nomor_tugas} telah ditandai selesai. ---")
        else:
            print("--- Nomor tugas tidak valid. ---")

    def simpan_data(self):
        """Menyimpan semua data tugas ke dalam file JSON."""
        # Mengubah setiap objek tugas menjadi dictionary menggunakan metode to_dict()
        data_untuk_disimpan = [tugas.to_dict() for tugas in self.daftar_tugas]
        with open(self.file_path, 'w') as f:
            json.dump(data_untuk_disimpan, f, indent=4)
        print("--- Data berhasil disimpan. Sampai jumpa! ---")

    def muat_data(self):
        """Memuat data tugas dari file JSON saat aplikasi dimulai."""
        try:
            with open(self.file_path, 'r') as f:
                data_dari_file = json.load(f)
                for data_tugas in data_dari_file:
                    # Deserialisasi: Membuat objek yang sesuai berdasarkan 'tipe'
                    if data_tugas['tipe'] == JadwalKerja.TIPE:
                        tugas = JadwalKerja(data_tugas['deskripsi'], data_tugas['hari'], data_tugas['jam'], data_tugas['selesai'])
                    elif data_tugas['tipe'] == TugasDeadline.TIPE:
                        tugas = TugasDeadline(data_tugas['deskripsi'], data_tugas['deadline'], data_tugas['selesai'])
                    else:
                        continue # Lewati jika tipe tidak dikenal
                    self.daftar_tugas.append(tugas)
        except FileNotFoundError:
            # Jika file tidak ada, tidak apa-apa. Daftar tugas akan kosong.
            pass
        except json.JSONDecodeError:
            print("--- Peringatan: File data rusak atau kosong. Memulai dengan daftar kosong. ---")


def tampilkan_menu():
    """Menampilkan menu utama aplikasi."""
    print("\n===== Aplikasi Manajemen Pekerjaan =====")
    print("1. Tambah Jadwal Kerja Rutin")
    print("2. Tambah Tugas dengan Deadline")
    print("3. Lihat Semua Pekerjaan")
    print("4. Tandai Pekerjaan Selesai")
    print("5. Simpan dan Keluar")
    return input("Pilih menu (1-5): ")

def main():
    """Fungsi utama untuk menjalankan aplikasi CLI."""
    manajer = ManajerJadwal()

    while True:
        pilihan = tampilkan_menu()

        if pilihan == '1':
            deskripsi = input("Masukkan deskripsi jadwal: ")
            hari = input("Masukkan hari (e.g., Senin): ")
            jam = input("Masukkan jam (e.g., 09:00): ")
            tugas_baru = JadwalKerja(deskripsi, hari, jam)
            manajer.tambah_tugas(tugas_baru)

        elif pilihan == '2':
            deskripsi = input("Masukkan deskripsi tugas: ")
            deadline = input("Masukkan deadline (e.g., 25-12-2023 23:59): ")
            tugas_baru = TugasDeadline(deskripsi, deadline)
            manajer.tambah_tugas(tugas_baru)

        elif pilihan == '3':
            manajer.tampilkan_semua_tugas()

        elif pilihan == '4':
            manajer.tampilkan_semua_tugas()
            if manajer.daftar_tugas:
                try:
                    nomor = int(input("Masukkan nomor pekerjaan yang ingin ditandai selesai: "))
                    manajer.tandai_tugas_selesai(nomor)
                except ValueError:
                    print("--- Masukan harus berupa angka. ---")

        elif pilihan == '5':
            manajer.simpan_data()
            break
            
        else:
            print("--- Pilihan tidak valid. Silakan coba lagi. ---")

# Entry point aplikasi
if __name__ == "__main__":
    main()