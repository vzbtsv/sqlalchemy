from datetime import datetime, time
from sqlalchemy import Column, String, Integer, DateTime, Text, Boolean, orm, Table, ForeignKey
from .db_session import SqlAlchemyBase
from data.users import job_participants


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader_id = Column(Integer, ForeignKey('users.id'))
    job = Column(Text, unique=True)
    work_size = Column(Integer)
    collaborators = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime, default=datetime.now)
    is_finished = Column(Boolean, default=False)

    # Связи:
    team_leader = orm.relationship("User", back_populates="jobs_led")
    participants = orm.relationship(
        "User",
        secondary=job_participants,
        back_populates="jobs_participated"
    )

    def __repr__(self):
        return (f"{self.team_leader_id} {self.job} {self.work_size} "
                f"{self.collaborators} {self.start_date}\n"
                f"{self.end_date} {self.is_finished}")
