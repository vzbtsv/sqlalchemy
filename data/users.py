from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, orm, ForeignKey, Table
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase

association_table = Table(
    'association',
    SqlAlchemyBase.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('job_id', Integer, ForeignKey('jobs.id'))
)


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    position = Column(String, nullable=True)
    speciality = Column(String, nullable=True)
    address = Column(String, nullable=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    modified_date = Column(DateTime)

    # Relationships
    led_jobs = orm.relationship("Jobs", back_populates="team_leader")
    participated_jobs = orm.relationship(
        "Jobs",
        secondary=association_table,
        back_populates="participants"
    )

    def __repr__(self):
        return (f"{self.surname} {self.name} {self.age} "
                f"{self.position} {self.speciality}\n"
                f"{self.address} {self.email} {self.hashed_password}")

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
