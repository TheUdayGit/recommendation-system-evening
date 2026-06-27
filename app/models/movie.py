from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import (Column, Integer, String, Float, Date, Text, Boolean,
                        Index, JSON, ForeignKey, DateTime)
from sqlalchemy.orm import  Mapped, mapped_column, relationship

from app.database.base import Base

if TYPE_CHECKING:
    from collections import *
class Movie(Base):
    __tablename__ = "movie"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    imdb_id: Mapped[Optional[str]] = mapped_column(String(20), unique=True, nullable=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    original_title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    overview: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    tagline: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    original_language: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    homepage: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    release_date: Mapped[Optional[Date]] = mapped_column(Date, nullable=True, index=True)
    runtime: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, index=True)
    status: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, index=True)
    budget: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    revenue: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    popularity: Mapped[Optional[float]] = mapped_column(Float, nullable=True, index=True)
    vote_average: Mapped[Optional[float]] = mapped_column(Float, nullable=True, index=True)
    vote_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, index=True)
    adult: Mapped[bool] = mapped_column(Boolean, default=False)
    video: Mapped[Optional[int]] = mapped_column(Boolean, default=False)
    poster_path: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    backdrop_path: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    collection_id: Mapped[Optional[int]] = mapped_column(ForeignKey("collections.id"), nullable=True, index=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)


    # Relationships
    collection: Mapped[Optional["Collection"]]

