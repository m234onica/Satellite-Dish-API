from flask import Flask, request, jsonify, render_template, current_app
from datetime import date, timedelta, datetime

from init import create_app, db
from config import CATEGORY_DB, ALLOWED_EXTENSIONS
from models import Event, category_Enum, File
from storage import decode_and_get_url

app = create_app()


@app.route('/')
def index():
    return render_template('event_list.html')

@app.route('/api/<int:id>')
def get_each_event(id):
  event = Event.query.filter_by(id=id).first()

  result = []
  data = {
      "index": event.id,
      "img": event.img,
      "title": event.title,
      # "category": event.category,
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
      }
  }
  result.append(data)
  return jsonify(result)

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


@app.route('/api/banner', methods=['GET'])
def get_all_banner():
  
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
      )
    
    db.session.add(new_event)
    db.session.commit()
    
    if new_event.img == "":
      event_img = decode_and_get_url(
          request.json['img'], new_event.id)

      new_event = Event.query.filter_by(id=new_event.id).first()
      new_event.img = event_img
      db.session.commit()

    return 'Saved to the database!'

  if request.method == 'GET':
    all_events = Event.query.all()
    result = []
    for event in all_events:
      data = {
        "index": event.id,
        "img": event.img,
        "title": event.title,
        # "category": event.category,
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
        }
      }
      result.append(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002', debug=True)
