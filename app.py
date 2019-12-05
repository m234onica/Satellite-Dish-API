from flask import Flask, request, jsonify, json
from main import create_app, db_session
from sqlalchemy import or_
from models import event
from datetime import date, timedelta, time
import ast

app = create_app()

@app.route('/api/events/<categories>/<years>/<months>/<days>', methods=['GET'])
def get_events(categories, years, months, days):
  
  urlDate = date(int(years), int(months), int(days))
  searchEndDate = urlDate - timedelta(days=-7)
  
  event_data = event.query.filter_by(category=categories).\
      filter(~(or_(event.end_date < urlDate, event.start_date > searchEndDate))).\
      with_entities(
        event.img, 
        event.link, 
        event.title, 
        event.start_date, 
        event.end_date, 
        event.location, 
        event.desc, 
        event.display_date).\
      all()
  # print(event_data)
  
  if not event_data:
    return 'No data'

  list = [dict(zip(result.keys(), result)) for result in event_data]
  return jsonify(list)

@app.route('/api/banner', methods=['GET'])
def get_all_banner():
  all_banner = event.query.with_entities(
      event.img,
      event.id,
      event.title,
      event.location,
      event.desc,
      event.display_date).all()
  print(all_banner)
  list = [dict(zip(result.keys(), result)) for result in all_banner]
  return jsonify(list)
  

@app.route('/api/<categories>/banner', methods=['GET'])
def get_banner(categories):
  event_banner = event.query.filter_by(category=categories).with_entities(
      event.img,
      event.id,
      event.title,
      event.location,
      event.desc,
      event.display_date).all()
  print(event_banner)
  list = [dict(zip(result.keys(), result)) for result in event_banner]
  return jsonify(list)
  
if __name__ == '__main__':
    app.run(port='5002', debug=True)
