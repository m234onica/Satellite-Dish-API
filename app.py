from flask import Flask, request, jsonify, render_template, current_app
from datetime import date, timedelta, datetime

from models import Event, category_Enum, File
from config import CATEGORY_DB, ALLOWED_EXTENSIONS
from init import create_app, db
from storage import upload_file

import base64
import uuid
import re
import os
import json

app = create_app()


@app.route('/api/events/<category>/<int:year>/<int:month>/<int:day>', methods=['GET'])
def get_events(category, year, month, day):

  if category not in CATEGORY_DB:
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
   
  if category not in CATEGORY_DB:
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


def decode_and_upload_file(src):
  result = re.search(
      "data:image/(?P<ext>.*?);base64,(?P<data>.*)", src, re.DOTALL)
  if result:
    ext = result.groupdict().get("ext")
    data = result.groupdict().get("data")

  else:
    raise Exception("Do not parse!")

  if ext in ALLOWED_EXTENSIONS:
    img = base64.urlsafe_b64decode(data)
    filename = "{}.{}".format(uuid.uuid4(), ext)

    public_url = upload_file(img, filename, "image/"+ext)
    return public_url
  else:
    return "Wrong file type."

@app.route('/api/event', methods=['GET', 'POST'])
def create_event():

  if request.method == 'POST':

    new_event = Event(
          title=request.json['title'],
          img=decode_and_upload_file(request.json['img']),
          category=request.json['category'], 
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

    return 'Saved to the datanase!' + jsonify(new_event)


if __name__ == '__main__':
    app.run(port='5002', debug=True)
