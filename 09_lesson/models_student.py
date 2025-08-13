from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    tablename = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)  # Для реализации soft delete

    def repr(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"
