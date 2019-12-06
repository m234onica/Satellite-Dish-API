from flask import Flask, request, jsonify, json
from main import create_app, db
from sqlalchemy import or_
from models import Event, category_Enum
from datetime import date, timedelta, datetime
from config import db_category

app = create_app()


@app.route('/api/events/<category>/<int:year>/<int:month>/<int:day>', methods=['GET'])
def get_events(category, year, month, day):

  if category not in db_category:
    return 'Category is not found.', 404
  
  try:
    url_start_date = date(year, month, day)
  except ValueError as n:
    print(n)
    return 'The date is not correct.', 404
  result = []
  url_end_date = url_start_date + timedelta(days=7)
  events = Event.query.\
      filter_by(category=category).\
      filter(~(Event.end_date < url_start_date)).\
      filter(~(Event.start_date > url_end_date)).\
      all()

  if not events:
    return 'No data'
  
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

  if not all_banners:
    return 'No data'

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
   
  if category not in db_category:
    return 'Category is not found.', 404

  result = []
  event_banners = Event.query.filter_by(category=category).all()

  if not event_banners:
    return 'No data'

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

if __name__ == '__main__':
    app.run(port='5002', debug=True)
