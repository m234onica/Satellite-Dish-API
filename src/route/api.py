from flask import (Flask, request, jsonify, render_template, Blueprint,
                  current_app, url_for, redirect)

from datetime import date, timedelta, datetime
from enum import Enum

from src import db
from src.tools.data import data
from src.tools.storage import decode_and_get_url
from src.models.model import Event, category_Enum, banner_Enum, region_Enum
from config import CATEGORY_DB, ALLOWED_EXTENSIONS, PER_PAGE


api = Blueprint('api', __name__)


@api.route('/api/banner', methods=['GET'])
def banner():
  all_banners = Event.query.filter_by(status=1).\
      filter(Event.show_banner != "hide").all()
  result = data('banners', all_banners)
  return jsonify(result)


@api.route('/api/home_banner', methods=['GET'])
def get_home_banner():
  home_banners = Event.query.filter_by(status=1).filter_by(home_banner=1).all()
  result = data('banners', home_banners)
  return jsonify(result)


@api.route('/api/category_banner/<category>', methods=['GET'])
def get_category_banner(category):
  if category not in CATEGORY_DB:
    return 'Category is not found.', 400

  category_banners = Event.query.filter_by(
      status=1).filter_by(category_banner=1).filter_by(category=category).all()
  result = data('banners', category_banners)
  return jsonify(result)


@api.route('/api/events/<category>/<int:year>/<int:month>/<int:day>', methods=['GET'])
def filter_events(category, year, month, day):

  if category not in CATEGORY_DB:
    return 'Category is not found.', 400
  
  try:
    url_start_date = date(year, month, day)
  except ValueError as n:
    print(n)
    return 'The date is not correct.', 400

  url_end_date = url_start_date + timedelta(days=7)
  events = Event.query.\
      filter_by(category=category).\
      filter(Event.end_date >= url_start_date).\
      filter(Event.start_date <= url_end_date).\
      all()
  
  result = data('filter_events', events)
  return jsonify(result)


@api.route('/api/<category>/banner', methods=['GET'])
def get_banner(category):
  if category not in CATEGORY_DB:
    return 'Category is not found.', 400

  event_banners = Event.query.filter_by(category=category).all()
  if event_banners == None:
      return {}
  result = data('banners', event_banners)
  return jsonify(result)


#update event
@api.route('/api/event/<int:id>', methods=['GET', 'POST'])
def each_event(id):
  event = Event.query.filter_by(id=id).first()

  if request.method == 'GET':
    if event == None: 
      return {}

    result = data('event', event)
    return jsonify(result)

  if request.method == 'POST':
    event.title=request.json['title']
    event.category=request.json['category']
    event.link=request.json['link']
    event.description = request.json['desc']
    event.region = request.json['region']
    event.start_date = request.json['start_date']
    event.end_date = request.json['end_date']
    event.display_date = request.json['display_date']
    event.location = request.json['location']
    event.note=request.json['note']
    event.status = request.json['status']
    event.show_banner = request.json['show_banner']

    db.session.commit()
    return jsonify({'result': 'success', 'event_index': event.id})

#create event
@api.route('/api/event', methods=['GET', 'POST'])
def create_event():
  if request.method == 'POST':
    new_event = Event(
      title=request.json['title'],
      category=category_Enum(request.json['category']),
      img="",
      link=request.json['link'],
      created_at=datetime.now(),
      description=request.json['desc'],
      region=region_Enum(0),
      start_date=request.json['date']['start'],
      end_date=request.json['date']['end'],
      display_date=request.json['display_date'],
      location=request.json['location'],
      note=request.json['note'],
      reporter_name=request.json['reporter']['name'],
      reporter_email=request.json['reporter']['email'],
      reporter_phone=request.json['reporter']['phone'],
      status=None,
      show_banner=banner_Enum(0)
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
    result = data('events', all_events)
    return jsonify(result)      
