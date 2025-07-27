


from db import db
from models.master import Master

def create_master(data):
    master = Master(**data)
    db.session.add(master)
    db.session.commit()
    return master

def get_masters():
    return Master.query.all()

def update_master(master_id, updates):
    master = db.session.get(Master, master_id)
    if not master:
        return None
    for key, value in updates.items():
        setattr(master, key, value)
    db.session.commit()
    return master

def delete_master(master_id):
    master = db.session.get(Master, master_id)
    if master:
        db.session.delete(master)
        db.session.commit()
        return True
    return False



