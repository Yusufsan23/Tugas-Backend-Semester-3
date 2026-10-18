class StudentService:
    def __init__(self, repo):
        self.repo = repo

    def fetch_students(self, major_query=None):
        students = self.repo.get_all()
        if major_query:
            students = [
                s for s in students if s["major"].lower() == major_query.lower()
            ]
        return {"status": "success", "total": len(students), "data": students}, 200

    def get_student_details(self, student_id):
        student = self.repo.get_by_id(student_id)
        if not student:
            return {"status": "fail", "message": "Mahasiswa tidak ditemukan"}, 404
        return {"status": "success", "data": student}, 200

    def add_new_student(self, data):
        if not data:
            return {
                "status": "error",
                "message": "Payload harus berformat application/json",
            }, 400

        # Validasi kelengkapan field
        required_fields = ["nim", "name", "major", "gpa"]
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return {
                "status": "error",
                "message": f"Field wajib diisi: {', '.join(missing_fields)}",
            }, 400

        # Aturan Bisnis 1: NIM harus unik
        if self.repo.get_by_nim(data["nim"]):
            return {
                "status": "fail",
                "message": "NIM sudah terdaftar (harus unik)",
            }, 400

        # Aturan Bisnis 2: IPK antara 0.00 - 4.00
        try:
            gpa_val = float(data["gpa"])
            if not (0.00 <= gpa_val <= 4.00):
                return {
                    "status": "fail",
                    "message": "IPK harus berada di antara 0.00 - 4.00",
                }, 400
        except ValueError:
            return {"status": "fail", "message": "Format IPK tidak valid"}, 400

        # Jika lolos semua validasi, kirim ke repository untuk disimpan
        new_student = self.repo.create(data)
        return {
            "status": "success",
            "message": "Mahasiswa berhasil ditambahkan",
            "data": new_student,
        }, 201

    def update_student(self, student_id, data):
        student = self.repo.get_by_id(student_id)
        if not student:
            return {"status": "fail", "message": "Mahasiswa tidak ditemukan"}, 404

        # Aturan Bisnis 1: NIM harus unik
        new_nim = data.get("nim")
        if new_nim and new_nim != student["nim"]:
            if self.repo.get_by_nim(new_nim):
                return {
                    "status": "fail",
                    "message": "NIM sudah terdaftar (harus unik)",
                }, 400

        # Aturan Bisnis 2: IPK antara 0.00 - 4.00
        new_gpa = data.get("gpa")
        if new_gpa is not None:
            try:
                gpa_val = float(new_gpa)
                if not (0.00 <= gpa_val <= 4.00):
                    return {
                        "status": "fail",
                        "message": "IPK harus berada di antara 0.00 - 4.00",
                    }, 400
            except ValueError:
                return {"status": "fail", "message": "Format IPK tidak valid"}, 400

        updated_data = {
            "nim": new_nim or student["nim"],
            "name": data.get("name", student["name"]),
            "major": data.get("major", student["major"]),
            "gpa": float(new_gpa) if new_gpa is not None else student["gpa"],
        }

        updated_student = self.repo.update(student_id, updated_data)
        return {
            "status": "success",
            "message": "Data berhasil diperbarui",
            "data": updated_student,
        }, 200

    def delete_student(self, student_id):
        success = self.repo.delete(student_id)
        if not success:
            return {"status": "fail", "message": "Mahasiswa tidak ditemukan"}, 404
        return {"status": "success", "message": "Data mahasiswa berhasil dihapus"}, 200
