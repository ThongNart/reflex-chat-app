import reflex as rx
from datetime import datetime, timezone
from sqlmodel import Field, Relationship
import sqlalchemy
from typing  import List

def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)

class ChatSession(rx.Model, table=True):
    # id
    # title: str
    messages: List['ChatSessionMessageModel'] = Relationship(back_populates='session_chat')

    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs ={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    )

    updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs ={
            'onupdate': sqlalchemy.func.now(),
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    )

class ChatSessionMessageModel (rx.Model, table=True):
    # id
    # messages 
    session_id: int = Field(default=None, foreign_key='chatsession.id')
    session_chat: ChatSession = Relationship(back_populates="messages")
    content: str
    role: str
    
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs ={
            'server_default': sqlalchemy.func.now()
        },
        nullable=False,
    )