
def serialize(model_obj):
    return {c.name: str(getattr(model_obj, c.name)) for c in model_obj.__table__.columns}
