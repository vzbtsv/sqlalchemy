from datetime import datetime, time
from sqlalchemy import Column, String, Integer, DateTime, Text, Boolean, orm, Table, ForeignKey
from .db_session import SqlAlchemyBase
from data.users import association_table


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    job = Column(Text, nullable=True)
    work_size = Column(Integer, nullable=True)
    collaborators = Column(String, nullable=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, default=datetime.now, nullable=True)
    is_finished = Column(Boolean, nullable=True)

    team_leader = orm.relationship("User", back_populates="led_jobs")
    participants = orm.relationship(
        "User",
        secondary=association_table,
        back_populates="participated_jobs"
    )

    def __repr__(self):
        return (f"{self.team_leader_id} {self.job} {self.work_size} "
                f"{self.collaborators} {self.start_date}\n"
                f"{self.end_date} {self.is_finished}")
