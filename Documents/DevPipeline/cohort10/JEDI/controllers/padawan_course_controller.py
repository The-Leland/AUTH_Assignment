


from db import db
from models.padawan_course import PadawanCourse

def enroll_padawan(data):
    enrollment = PadawanCourse(**data)
    db.session.add(enrollment)
    db.session.commit()
    return enrollment

def remove_enrollment(padawan_id, course_id):
    enrollment = PadawanCourse.query.filter_by(padawan_id=padawan_id, course_id=course_id).first()
    if enrollment:
        db.session.delete(enrollment)
        db.session.commit()
        return True
    return False

