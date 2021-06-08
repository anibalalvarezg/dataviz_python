from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

nobel_winners = [{'category': 'Physics', 'name': 'Albert Einstein', 'nationality': 'Swiss', 'sex': 'male', 'year': 1921},
{'category': 'Physics', 'name': 'Paul Dirac', 'nationality': 'British', 'sex': 'male', 'year': 1933},
{'category': 'Chemistry', 'name': 'Marie Curie', 'nationality': 'Polish', 'sex': 'female','year': 1911}]

engine = create_engine('sqlite:///data/nobel_prize.db', echo=True)


Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
class Winner(Base):
    __tablename__ = 'winners'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    year = Column(Integer)
    nationality = Column(String)
    sex = Column(Enum('male', 'female'))
    
    def __repr__(self):
        return "<Winner(name='%s', category='%s', year='%s')>"\
        %(self.name, self.category, self.year)

Base.metadata.create_all(engine)

albert = Winner(**nobel_winners[0])
session.add(albert)
session.new


session.expunge(albert)
session.new

winner_rows = [Winner(**w) for w in nobel_winners]
session.add_all(winner_rows)
session.commit()

session.query(Winner).count()

result = session.query(Winner).filter_by(nationality='Swiss')
print(list(result))

result = session.query(Winner).filter(\
Winner.category == 'Physics', \
Winner.nationality != 'Swiss')
print(list(result))

result = session.query(Winner).get(3)
print(result)

res = session.query(Winner).order_by('year')
print(list(res))

def inst_to_dict(inst, delete_id=True):
    dat = {}
    for column in inst.__table__.columns:
        dat[column.name] = getattr(inst, column.name)
    if delete_id:
        dat.pop('id')
    return dat

winner_rows = session.query(Winner)
nobel_winners = [inst_to_dict(w) for w in winner_rows]
print(nobel_winners)

marie = session.query(Winner).get(3)
marie.nationality = 'French'
session.dirty

session.commit()

print(session.query(Winner).get(3))


session.query(Winner).filter_by(name='Albert Einstein').delete()
print(list(session.query(Winner)))

Winner.__table__.drop(engine)
print(list(session.query(Winner)))
