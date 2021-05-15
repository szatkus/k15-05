import flask
from db import session, Question, Result
from sqlalchemy.orm import joinedload
from uuid import uuid4

app = flask.Flask(__name__)

@app.get('/')
def root():
  questions = session.query(Question)\
    .options(joinedload(Question.answers))\
    .all()
  return flask.render_template('index.html', questions=questions)

@app.post('/submit')
def submit():
  for key in flask.request.form:
    question_id = int(key[key.find('-') + 1:])
    answer_id = int(flask.request.form[key])
    respondent_id = str(uuid4())
    result = Result()
    result.respondent_id = respondent_id
    result.question_id = question_id
    result.answer_id = answer_id
    session.add(result)
  session.commit()
  return flask.render_template('strona.html')

app.run(threaded=False)
