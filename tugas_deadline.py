from models.tugas import Tugas

class TugasDeadline(Tugas):
    """
    Class untuk tugas yang memiliki deadline spesifik.
    Mewarisi dari class Tugas. (Inheritance)
    """
    TIPE = "tugas_deadline"

    def __init__(self, deskripsi, deadline, selesai=False):
        super().__init__(deskripsi)
        self.deadline = deadline
        self.selesai = selesai

    def tampilkan_info(self):
        """Implementasi spesifik untuk menampilkan info tugas deadline. (Polymorphism)"""
        return f"[Tugas Deadline] {self.deskripsi} - Deadline: {self.deadline} (Status: {self.get_status()})"

    def to_dict(self):
        """Mengubah objek TugasDeadline menjadi dictionary."""
        return {
            "tipe": self.TIPE,
            "deskripsi": self.deskripsi,
            "deadline": self.deadline,
            "selesai": self.selesai
        }