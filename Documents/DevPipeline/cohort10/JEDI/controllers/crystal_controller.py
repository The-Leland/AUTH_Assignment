


from db import db
from models.crystal import Crystal

def create_crystal(data):
    crystal = Crystal(**data)
    db.session.add(crystal)
    db.session.commit()
    return crystal

def get_crystals_by_rarity(rarity_level):
    return Crystal.query.filter_by(rarity_level=rarity_level).all()

