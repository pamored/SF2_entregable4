#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bottle
import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from sqlalchemy import Table, Column, Integer, String, Float
from bottle import Bottle, run, HTTPResponse, static_file, redirect, error, template, request

# Modelos

Base = declarative_base()

class Score(Base):
    __tablename__ = 'scores'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)

# Rutas REST

app = bottle.app()

@app.route('/')
def index():
    return 'hola desde el servidor'

@app.route('/score/list', method="GET")
def score_list():
    # db
    engine = create_engine('sqlite:///game.db')
    session_db = sessionmaker()
    session_db.configure(bind=engine)
    session = session_db()
    conn = engine.connect()
    # list
    stmt = select([Score])
    rs = conn.execute(stmt)
    rpta = [dict(r) for r in conn.execute(stmt)]
    return HTTPResponse(body = json.dumps(rpta))

@app.route('/score/add', method="POST")
def score_create():
    # db
    engine = create_engine('sqlite:///game.db')
    session_db = sessionmaker()
    session_db.configure(bind=engine)
    session = session_db()
    # form data
    name = request.forms.get('name')
    score = request.forms.get('score')
    # save
    s = Score(
        name=name,
        score=score,
    )
    session.add(s)
    session.commit()
    generated_id = str(s.id)
    return HTTPResponse(body = generated_id)

@app.route('/score/edit', method="POST")
def score_update():
    # db
    engine = create_engine('sqlite:///game.db')
    session_db = sessionmaker()
    session_db.configure(bind=engine)
    session = session_db()
    # form data
    id = request.forms.get('id')
    name = request.forms.get('name')
    score = request.forms.get('score')
    # save
    session.query(Score).filter_by(id = id).update({
        'name': name,
        'score': score,
    })
    session.commit()
    return HTTPResponse(body = 'score actualizado')


@app.route('/score/delete', method="POST")
def score_delete():
    # db
    engine = create_engine('sqlite:///game.db')
    session_db = sessionmaker()
    session_db.configure(bind=engine)
    session = session_db()
    # form data
    id = request.forms.get('id')
    # save
    session.query(Score).filter_by(id = id).delete()
    session.commit()
    return HTTPResponse(body = 'score Eliminado')

# Main

if __name__ == '__main__':
    bottle.run(app = app, host='localhost', port=4000, debug=True, reloader=True)
