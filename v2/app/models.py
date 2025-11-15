
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, SmallInteger, UniqueConstraint, Index, func

Base = declarative_base()

class Device(Base):
    __tablename__ = "device"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type: Mapped[str] = mapped_column(String(30), nullable=False)
    model: Mapped[str] = mapped_column(String(30), nullable=False)
    ip: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    sn: Mapped[str | None] = mapped_column(String(30), nullable=True)
    active: Mapped[int] = mapped_column(SmallInteger, nullable=False, default=0)
    live: Mapped[int] = mapped_column(SmallInteger, nullable=False, default=0)
    moniter: Mapped[int] = mapped_column(SmallInteger, nullable=False, default=0)
    row_pos: Mapped[int | None] = mapped_column(Integer, nullable=True)
    rack: Mapped[int | None] = mapped_column(Integer, nullable=True)
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)
    lastcheck: Mapped[DateTime | None] = mapped_column(DateTime, nullable=True)
    created_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=func.current_timestamp())

    __table_args__ = (
        UniqueConstraint("ip", name="uq_device_ip"),
        Index("idx_device_type", "type"),
        Index("idx_device_model", "model"),
        Index("idx_device_location", "location"),
        Index("idx_lastcheck", "lastcheck"),
    )

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    email: Mapped[str | None] = mapped_column(String(255), nullable=True, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[int] = mapped_column(SmallInteger, nullable=False, default=1)
    is_admin: Mapped[int] = mapped_column(SmallInteger, nullable=False, default=0)
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
