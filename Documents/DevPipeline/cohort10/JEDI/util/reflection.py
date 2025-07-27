

from db import db

def reflect_table_schema(model_class):
    return {column.name: str(column.type) for column in model_class.__table__.columns}
