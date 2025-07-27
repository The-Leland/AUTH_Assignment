

from db import db
from models.species import Species

def create_species(data):
    species = Species(**data)
    db.session.add(species)
    db.session.commit()
    return species
