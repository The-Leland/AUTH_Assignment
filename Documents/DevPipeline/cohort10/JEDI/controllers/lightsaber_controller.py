


from db import db
from models.lightsaber import Lightsaber

def create_saber(data):
    saber = Lightsaber(**data)
    db.session.add(saber)
    db.session.commit()
    return saber

def update_saber(saber_id, updates):
    saber = db.session.get(Lightsaber, saber_id)
    if not saber:
        return None
    for key, value in updates.items():
        setattr(saber, key, value)
    db.session.commit()
    return saber

def delete_saber(saber_id):
    saber = db.session.get(Lightsaber, saber_id)
    if saber:
        db.session.delete(saber)
        db.session.commit()
        return True
    return False
