from flask import Flask, request, jsonify, render_template, current_app, url_for, redirect
from datetime import date, timedelta, datetime
from enum import Enum

from init import create_app, db
from config import CATEGORY_DB, ALLOWED_EXTENSIONS
from models import Event, category_Enum
from storage import decode_and_get_url

import json

app = create_app()


class Category(Enum):
    music = 0
    visual_art = 1
    market = 2
    theater = 3

@app.route('/')
def index():
  return redirect(url_for('event'))

@app.route('/event')
def event():

  all_events = Event.query.all()
  result = []

  for event in all_events:
    event_category = event.category
    data = {
      "index": event.id,
      "img": event.img,
      "title": event.title,
      "category": event_category.name,
      "region": event.region,
      "date": {
        "start": event.start_date.strftime("%Y-%m-%d"),
        "end": event.end_date.strftime("%Y-%m-%d"),
      },
        "display_date": event.display_date,
      "note": event.note,
      "address": event.location,
      "link": event.link,
      "desc": event.desc,
      "reporter": {
          "name": event.reporter_name,
          "email": event.reporter_email,
        "phone": event.reporter_phone
      },
        "status": event.status,
        "banner":{
          "home": event.home_banner,
          "category": event.category_banner,
        }
    }
    result.append(data)
  return render_template("event.html", result=result)


@app.route('/all_banner')
def get_all_banner():

  result = []
  all_banners = Event.query.filter_by(status=1).all()

  for banner in all_banners:
    data = {
        "index": banner.id,
        "img": banner.img,
        "title": banner.title,
        "display_date": banner.display_date,
        "address": banner.location,
        "desc": banner.desc
    }
    result.append(data)
  return render_template("all_banner.html", result=result)

@app.route('/home_banner', methods=['GET'])
def home_banner():
  result = []
  home_banners = Event.query.filter_by(
      status=1).filter_by(home_banner=1).all()

  for banner in home_banners:
    data = {
        "index": banner.id,
        "img": banner.img,
        "title": banner.title,
        "display_date": banner.display_date,
        "address": banner.location,
        "desc": banner.desc
    }
    result.append(data)
  return render_template("home_banner.html", result=result)


@app.route('/category_banner/<category>', methods=['GET'])
def category_banner(category):
  if category not in CATEGORY_DB:
    return 'Category is not found.', 400

  result = []
  category_banners = Event.query.filter_by(
      status=1).filter_by(category_banner=1).filter_by(category=category).all()

  for banner in category_banners:
    data = {
        "index": banner.id,
        "img": banner.img,
        "title": banner.title,
        "display_date": banner.display_date,
        "address": banner.location,
        "desc": banner.desc
    }
    result.append(data)
  if category == 'music':
    return render_template("music.html", result=result)
  if category == 'visual_art':
    return render_template("visual_art.html", result=result)
  if category == 'market':
    return render_template("market.html", result=result)
  if category == 'theater':
    return render_template("theater.html", result=result)

@app.route('/api/banner', methods=['GET'])
def banner():
  result = []
  all_banners = Event.query.all()

  for banner in all_banners:
    data = {
        "index": banner.id,
        "img": banner.img,
        "title": banner.title,
        "display_date": banner.display_date,
        "address": banner.location,
        "desc": banner.desc
    }
    result.append(data)
  return jsonify(result)

@app.route('/api/home_banner', methods=['GET'])
def get_home_banner():
  result = []
  home_banners = Event.query.filter_by(status=1).filter_by(home_banner=1).all()

  for banner in home_banners:
    data = {
        "index": banner.id,
        "img": banner.img,
        "title": banner.title,
        "display_date": banner.display_date,
        "address": banner.location,
        "desc": banner.desc
    }
    result.append(data)
  return jsonify(result)


@app.route('/api/category_banner/<category>', methods=['GET'])
def get_category_banner(category):
  if category not in CATEGORY_DB:
    return 'Category is not found.', 400

  result = []
  category_banners = Event.query.filter_by(
      status=1).filter_by(category_banner=1).filter_by(category=category).all()

  for banner in category_banners:
    data = {
        "index": banner.id,
        "img": banner.img,
        "title": banner.title,
        "display_date": banner.display_date,
        "address": banner.location,
        "desc": banner.desc
    }
    result.append(data)
  return jsonify(result)

@app.route('/api/event/<int:id>', methods=['GET', 'PUT'])
def each_event(id):
  event = Event.query.filter_by(id=id).first()
  if request.method == 'GET':

    result = []
    event_category = event.category
    data = {
        "index": event.id,
        "img": event.img,
        "title": event.title,
        "category": event_category.name,
        "region": event.region,
        "date": {
            "start": event.start_date.strftime("%Y-%m-%d"),
            "end": event.end_date.strftime("%Y-%m-%d"),
        },
        "display_date": event.display_date,
        "note": event.note,
        "address": event.location,
        "link": event.link,
        "desc": event.desc,
        "reporter": {
            "name": event.reporter_name,
            "email": event.reporter_email,
            "phone": event.reporter_phone,
        },
        "status": event.status,
        "banner":{
          "home": event.home_banner,
          "category": event.category_banner,
        }
    }
    result.append(data)
    return jsonify(result)

  if request.method == 'PUT':
    event.title=request.json['title']
    event.category=request.json['category']
    event.link=request.json['link']
    event.desc = request.json['desc']
    event.region = request.json['region']
    event.start_date = request.json['start_date']
    event.end_date = request.json['end_date']
    event.display_date = request.json['display_date']
    event.location = request.json['location']
    event.note=request.json['note']
    event.status = request.json['status']
    event.home_banner = request.json['home_banner']
    event.category_banner = request.json['category_banner']

    db.session.commit()
    return 'database is update success.'

@app.route('/api/events/<category>/<int:year>/<int:month>/<int:day>', methods=['GET'])
def get_events(category, year, month, day):

  if category not in CATEGORY_DB:
    return 'Category is not found.', 400
  
  try:
    url_start_date = date(year, month, day)
  except ValueError as n:
    print(n)
    return 'The date is not correct.', 400

  result = []
  url_end_date = url_start_date + timedelta(days=7)
  events = Event.query.\
      filter_by(category=category).\
      filter(Event.end_date >= url_start_date).\
      filter(Event.start_date <= url_end_date).\
      all()
  
  for event in events:
    data = {
      "img": event.img,
      "title": event.title,
      "region": event.region,
      "date": {
          "start": event.start_date.strftime("%Y-%m-%d"),
          "end": event.end_date.strftime("%Y-%m-%d"),
      },
      "display_date": event.display_date,
      "address": event.location,
      "link": event.link,
      "desc": event.desc
    }
    result.append(data)
  return jsonify(result)

@app.route('/api/<category>/banner', methods=['GET'])
def get_banner(category):
   
  if category not in CATEGORY_DB:
    return 'Category is not found.', 400

  result = []
  event_banners = Event.query.filter_by(category=category).all()

  for banner in event_banners:
    data = {
      "index": banner.id,
      "img": banner.img,
      "title": banner.title,
      "display_date": banner.display_date,
      "address": banner.location,
      "desc": banner.desc
    }
    result.append(data)
  return jsonify(result)

@app.route('/api/event', methods=['GET', 'POST'])
def create_event():

  if request.method == 'POST':
    new_event = Event(
      title=request.json['title'],
      category=request.json['category'],
      img="",
      link=request.json['link'],
      created_at=datetime.now(),
      desc=request.json['desc'], 
      region=request.json['region'],
      start_date=request.json['start_date'], 
      end_date=request.json['end_date'],
      display_date=request.json['display_date'], 
      location=request.json['location'],
      note=request.json['note'], 
      reporter_name=request.json['reporter_name'],
      reporter_email=request.json['reporter_email'],
      reporter_phone=request.json['reporter_phone'],
      status=None,
      home_banner=None,
      category_banner=None
      )
    
    db.session.add(new_event)
    db.session.commit()
    
    if new_event.img == "":
      new_event = Event.query.filter_by(id=new_event.id).first()
      new_event.img = decode_and_get_url(
          request.json['img'], new_event.id)
      db.session.commit()

    return 'Saved to the database!'

  if request.method == 'GET':
    all_events = Event.query.all()
    result = []

    for event in all_events:
      event_category = event.category
      data = {
        "index": event.id,
        "img": event.img,
        "title": event.title,
        "category": event_category.name,
        "region": event.region,
        "date": {
          "start": event.start_date.strftime("%Y-%m-%d"),
          "end": event.end_date.strftime("%Y-%m-%d"),
        },
        "display_date": event.display_date,
        "note": event.note,
        "address": event.location,
        "link": event.link,
        "desc": event.desc,
        "reporter": {
          "name": event.reporter_name,
          "email": event.reporter_email,
          "phone": event.reporter_phone
        },
        "status": event.status,
        "banner":{
          "home": event.home_banner,
          "category": event.category_banner,
        }
      }
      result.append(data)
    return jsonify(result)      

if __name__ == '__main__':
    app.run(port='5002', debug=True)
