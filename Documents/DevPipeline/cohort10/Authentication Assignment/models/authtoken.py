


import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from db import db

class AuthToken(db.Model):
    __tablename__ = 'authtokens'

    auth_token = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'), nullable=False)
    expiration = Column(DateTime, default=lambda: datetime.utcnow() + timedelta(hours=1))

    user = relationship("User", back_populates="tokens")
