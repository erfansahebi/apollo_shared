import uuid
from os import getenv
from sqlalchemy import Column, DateTime, UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import registry

mapper_registry = registry()

Base = declarative_base()
metadata = Base.metadata


def get_db_url() -> str:
    return 'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'.format(
        db_user=getenv('DB_USER', 'postgres'),
        db_password=getenv('DB_PASSWORD', 'password'),
        db_host=getenv('DB_HOST', 'postgresql'),
        db_port=getenv('DB_PORT', '5432'),
        db_name=getenv('DB_NAME', 'auth'),
    )


def uuid_primary_key_column() -> Column:
    return Column(
        name='id',
        type_=UUID(as_uuid=True),
        primary_key=True,
        default=lambda: uuid.uuid4(),
    )


def created_at_column() -> Column:
    return Column(
        name='created_at',
        type_=DateTime(timezone=True),
        default=func.now(),
    )


def updated_at_column() -> Column:
    return Column(
        name='updated_at',
        type_=DateTime(timezone=True),
        default=func.now(),
        onupdate=func.now(),
    )
