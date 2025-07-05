from abc import ABC, abstractmethod

class Tugas(ABC):
    """
    Abstract Base Class untuk semua jenis tugas.
    Setiap tugas memiliki deskripsi dan status selesai.
    """
    def __init__(self, deskripsi):
        self.deskripsi = deskripsi
        self.selesai = False

    def tandai_selesai(self):
        """Mengubah status tugas menjadi selesai."""
        self.selesai = True

    def get_status(self):
        """Mengembalikan status tugas dalam bentuk string."""
        return "Selesai" if self.selesai else "Belum Selesai"

    @abstractmethod
    def tampilkan_info(self):
        """
        Metode abstract untuk menampilkan informasi detail dari tugas.
        Harus diimplementasikan oleh subclass. (Polymorphism)
        """
        pass

    @abstractmethod
    def to_dict(self):
        """
        Metode abstract untuk mengubah objek menjadi dictionary.
        Berguna untuk serialisasi ke JSON.
        """
        pass