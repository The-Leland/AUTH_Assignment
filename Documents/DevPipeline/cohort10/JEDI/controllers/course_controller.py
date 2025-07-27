


from db import db
from models.course import Course
from models.padawan_course import PadawanCourse

def create_course(data):
    course = Course(**data)
    db.session.add(course)
    db.session.commit()
    return course

def get_courses_by_difficulty(difficulty):
    return Course.query.filter_by(difficulty=difficulty).all()

def update_course(course_id, updates):
    course = db.session.get(Course, course_id)
    if not course:
        return None
    for key, value in updates.items():
        setattr(course, key, value)
    db.session.commit()
    return course

def delete_course(course_id):
    PadawanCourse.query.filter_by(course_id=course_id).delete()
    course = db.session.get(Course, course_id)
    if course:
        db.session.delete(course)
        db.session.commit()
        return True
    return False

