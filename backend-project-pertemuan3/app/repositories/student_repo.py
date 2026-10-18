class StudentRepository:
    def __init__(self):
        self.students = [
            {
                "id": 1,
                "nim": "202611001",
                "name": "Ahmad Fauzi",
                "major": "Teknik Informatika",
                "gpa": 3.75,
            },
            {
                "id": 2,
                "nim": "202611002",
                "name": "Budi Santoso",
                "major": "Sistem Informasi",
                "gpa": 3.40,
            },
            {
                "id": 3,
                "nim": "202611003",
                "name": "Citra Lestari",
                "major": "Teknik Informatika",
                "gpa": 3.90,
            },
            {
                "id": 4,
                "nim": "202611004",
                "name": "Kusuma Wijaya",
                "major": "Sistem Informasi",
                "gpa": 3.60,
            },
        ]

    def create(self, data):
        new_id = 1 if not self.students else max(s["id"] for s in self.students) + 1

        new_student = {
            "id": new_id,
            "nim": data["nim"],
            "name": data["name"],
            "major": data["major"],
            "gpa": float(data["gpa"]),
        }
        self.students.append(new_student)
        return new_student

    def get_all(self):
        return self.students

    def get_by_id(self, student_id):
        return next((s for s in self.students if s["id"] == student_id), None)

    def get_by_nim(self, nim):
        return next((s for s in self.students if s["nim"] == nim), None)

    def update(self, student_id, updated_data):
        student = self.get_by_id(student_id)
        if student:
            student.update(updated_data)
        return student

    def delete(self, student_id):
        student = self.get_by_id(student_id)
        if student:
            self.students = [s for s in self.students if s["id"] != student_id]
            return True
        return False
