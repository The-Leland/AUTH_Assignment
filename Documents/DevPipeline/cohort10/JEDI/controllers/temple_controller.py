


from db import db
from models.temple import Temple

def create_temple(data):
    temple = Temple(**data)
    db.session.add(temple)
    db.session.commit()
    return temple

def get_temple(temple_id):
    return db.session.get(Temple, temple_id)

def update_temple(temple_id, updates):
    temple = get_temple(temple_id)
    if not temple:
        return None
    for key, value in updates.items():
        setattr(temple, key, value)
    db.session.commit()
    return temple

def delete_temple(temple_id):
    temple = get_temple(temple_id)
    if not temple:
        return False
    temple.is_active = False
    db.session.commit()
    return True


