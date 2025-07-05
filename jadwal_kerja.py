from models.tugas import Tugas

class JadwalKerja(Tugas):
    """
    Class untuk jadwal kerja rutin yang memiliki hari dan jam.
    Mewarisi dari class Tugas. (Inheritance)
    """
    TIPE = "jadwal_kerja"

    def __init__(self, deskripsi, hari, jam, selesai=False):
        super().__init__(deskripsi)
        self.hari = hari
        self.jam = jam
        self.selesai = selesai

    def tampilkan_info(self):
        """Implementasi spesifik untuk menampilkan info jadwal kerja. (Polymorphism)"""
        return f"[Jadwal Rutin] {self.deskripsi} - Hari: {self.hari}, Jam: {self.jam} (Status: {self.get_status()})"

    def to_dict(self):
        """Mengubah objek JadwalKerja menjadi dictionary."""
        return {
            "tipe": self.TIPE,
            "deskripsi": self.deskripsi,
            "hari": self.hari,
            "jam": self.jam,
            "selesai": self.selesai
        }