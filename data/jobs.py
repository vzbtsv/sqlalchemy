from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, Text, Boolean, ForeignKey
from db_session import SqlAlchemyBase


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


    team_leader = SqlAlchemyBase.orm.relationship("users", back_populates="led_jobs")


    def __repr__(self):
        return (f"{self.team_leader_id} {self.job} {self.work_size} "
                f"{self.collaborators} {self.start_date}\n"
                f"{self.end_date} {self.is_finished}")
