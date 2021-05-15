from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

engine = create_engine('sqlite:///db.sqlite')

Base = declarative_base()

class Question(Base):
  __tablename__ = 'questions'

  id = Column(Integer, primary_key=True)
  text = Column(String, nullable=False)

class Answer(Base):
  __tablename__ = 'answers'

  id = Column(Integer, primary_key=True)
  text = Column(String, nullable=False)

  question_id = Column(Integer, ForeignKey('questions.id'))

  question = relationship("Question", backref=backref('answers'))

class Result(Base):
  __tablename__ = 'results'

  id = Column(Integer, primary_key=True)
  respondent_id = Column(String)

  question_id = Column(Integer, ForeignKey('questions.id'))
  answer_id = Column(Integer, ForeignKey('answers.id'))

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine) 
