class AreaRepository:
    @staticmethod
    def insert(cur, name):
        cur.execute("INSERT INTO area (name) VALUES (?)", (name,))
        return cur.lastrowid

    @staticmethod
    def update(cur, pk, name):
        cur.execute("UPDATE area SET name = ? WHERE id = ?", (name, pk))

    @staticmethod
    def delete(cur, pk):
        cur.execute("DELETE FROM area WHERE id = ?", (pk,))

    @staticmethod
    def get_by_id(cur, pk):
        cur.execute("SELECT * FROM area WHERE id = ?", (pk,))
        row = cur.fetchone()
        return dict(row) if row else None

    @staticmethod
    def get_all(cur):
        cur.execute("SELECT * FROM area")
        return [dict(row) for row in cur.fetchall()]


class SchoolRepository:
    @staticmethod
    def insert(cur, name, area_id=None):
        cur.execute("INSERT INTO school (name, area_id) VALUES (?, ?)", (name, area_id))
        return cur.lastrowid

    @staticmethod
    def update(cur, pk, name, area_id=None):
        cur.execute("UPDATE school SET name = ?, area_id = ? WHERE id = ?", (name, area_id, pk))

    @staticmethod
    def delete(cur, pk):
        cur.execute("DELETE FROM school WHERE id = ?", (pk,))

    @staticmethod
    def get_by_id(cur, pk):
        cur.execute("SELECT * FROM school WHERE id = ?", (pk,))
        row = cur.fetchone()
        return dict(row) if row else None

    @staticmethod
    def get_all(cur):
        cur.execute("SELECT * FROM school")
        return [dict(row) for row in cur.fetchall()]

    @staticmethod
    def filter_by_area(cur, area_id):
        cur.execute("SELECT * FROM school WHERE area_id = ?", (area_id,))
        return [dict(row) for row in cur.fetchall()]


class ClassroomRepository:
    @staticmethod
    def insert(cur, name, school_id=None):
        cur.execute("INSERT INTO classroom (name, school_id) VALUES (?, ?)", (name, school_id))
        return cur.lastrowid

    @staticmethod
    def update(cur, pk, name, school_id=None):
        cur.execute("UPDATE classroom SET name = ?, school_id = ? WHERE id = ?", (name, school_id, pk))

    @staticmethod
    def delete(cur, pk):
        cur.execute("DELETE FROM classroom WHERE id = ?", (pk,))

    @staticmethod
    def get_by_id(cur, pk):
        cur.execute("SELECT * FROM classroom WHERE id = ?", (pk,))
        row = cur.fetchone()
        return dict(row) if row else None

    @staticmethod
    def get_all(cur):
        cur.execute("SELECT * FROM classroom")
        return [dict(row) for row in cur.fetchall()]

    @staticmethod
    def filter_by_school(cur, school_id):
        cur.execute("SELECT * FROM classroom WHERE school_id = ?", (school_id,))
        return [dict(row) for row in cur.fetchall()]


class StudentRepository:
    @staticmethod
    def insert(cur, name, classroom_id=None):
        cur.execute("INSERT INTO student (name, classroom_id) VALUES (?, ?)", (name, classroom_id))
        return cur.lastrowid

    @staticmethod
    def update(cur, pk, name, classroom_id=None):
        cur.execute("UPDATE student SET name = ?, classroom_id = ? WHERE id = ?", (name, classroom_id, pk))

    @staticmethod
    def delete(cur, pk):
        cur.execute("DELETE FROM student WHERE id = ?", (pk,))

    @staticmethod
    def get_by_id(cur, pk):
        cur.execute("SELECT * FROM student WHERE id = ?", (pk,))
        row = cur.fetchone()
        return dict(row) if row else None

    @staticmethod
    def get_all(cur):
        cur.execute("SELECT * FROM student")
        return [dict(row) for row in cur.fetchall()]

    @staticmethod
    def filter_by_classroom(cur, classroom_id):
        cur.execute("SELECT * FROM student WHERE classroom_id = ?", (classroom_id,))
        return [dict(row) for row in cur.fetchall()]


class GradeRepository:
    @staticmethod
    def insert(cur, student_id, subject_id, score):
        cur.execute("INSERT INTO grade (student_id, subject_id, score) VALUES (?, ?, ?)",
                    (student_id, subject_id, score))
        return cur.lastrowid

    @staticmethod
    def update(cur, pk, score):
        cur.execute("UPDATE grade SET score = ? WHERE id = ?", (score, pk))

    @staticmethod
    def delete(cur, pk):
        cur.execute("DELETE FROM grade WHERE id = ?", (pk,))

    @staticmethod
    def get_by_id(cur, pk):
        cur.execute("SELECT * FROM grade WHERE id = ?", (pk,))
        row = cur.fetchone()
        return dict(row) if row else None

    @staticmethod
    def get_all(cur):
        cur.execute("SELECT * FROM grade")
        return [dict(row) for row in cur.fetchall()]

    @staticmethod
    def filter_by_student(cur, student_id):
        cur.execute("SELECT * FROM grade WHERE student_id = ?", (student_id,))
        return [dict(row) for row in cur.fetchall()]

    @staticmethod
    def filter_by_subject(cur, subject_id):
        cur.execute("SELECT * FROM grade WHERE subject_id = ?", (subject_id,))
        return [dict(row) for row in cur.fetchall()]


class SubjectRepository:
    @staticmethod
    def insert(cur, name):
        cur.execute("INSERT INTO subject (name) VALUES (?)", (name,))
        return cur.lastrowid

    @staticmethod
    def update(cur, pk, name):
        cur.execute("UPDATE subject SET name = ? WHERE id = ?", (name, pk))

    @staticmethod
    def delete(cur, pk):
        cur.execute("DELETE FROM subject WHERE id = ?", (pk,))

    @staticmethod
    def get_by_id(cur, pk):
        cur.execute("SELECT * FROM subject WHERE id = ?", (pk,))
        row = cur.fetchone()
        return dict(row) if row else None

    @staticmethod
    def get_all(cur):
        cur.execute("SELECT * FROM subject")
        return [dict(row) for row in cur.fetchall()]
