from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so

class CSC(db.Model):
    id : so.Mapped[int] = so.mapped_column(primary_key=True)
    city : so.Mapped[str] = so.mapped_column(sa.String(100), index = False , unique = False)
    country : so.Mapped[str] = so.mapped_column(sa.String(100), index = False , unique = False)
    state : so.Mapped[str] = so.mapped_column(sa.String(100), index = False , unique = False)
    stateCode : so.Mapped[str] = so.mapped_column(sa.String(100), index = False , unique = False)

    def __repr__(self):
        return '<CSC {}>'.format(self.city)


