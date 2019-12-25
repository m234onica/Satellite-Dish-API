from flask import Flask, request, jsonify, render_template, \
current_app, url_for, redirect, flash
from datetime import date, timedelta, datetime
from enum import Enum

from init import create_app, db
from config import CATEGORY_DB, ALLOWED_EXTENSIONS, PER_PAGE
from models import Event, category_Enum
from storage import decode_and_get_url
from data import data
import json

app = create_app()

#Backstage management
@app.route('/')
def index():
  return redirect(url_for('event'))


@app.route('/event', methods=['GET'])
def event():
  page = request.args.get('page', 1, type=int)
  pagination = Event.query.order_by(Event.start_date.asc()).\
      paginate(page, per_page=PER_PAGE, error_out=True, max_per_page=None)
  all_events = pagination.items
  return render_template("event.html", 
                          result=data('events', all_events), 
                          pagination=pagination)


@app.route('/banner')
def get_all_banner():
  page = request.args.get('page', 1, type=int)
  pagination = Event.query.filter_by(status=1).order_by(Event.id).\
      paginate(page, per_page=PER_PAGE, error_out=True,
               max_per_page=None)
  all_banners = pagination.items
  return render_template("all_banner.html", 
                          result=data('banners', all_banners), 
                          pagination=pagination)


@app.route('/home_banner', methods=['GET'])
def home_banner():
  page = request.args.get('page', 1, type=int)
  pagination = Event.query.filter_by(status=1).filter_by(home_banner=1).order_by(Event.id).\
                  paginate(page, per_page=PER_PAGE, error_out=True, max_per_page=None)
  home_banners = pagination.items
  return render_template("home.html", 
                          result=data('banners', home_banners), 
                          pagination=pagination)


@app.route('/category_banner/<category>', methods=['GET'])
def category_banner(category):
  if category not in CATEGORY_DB:
    return 'Category is not found.', 400

  page = request.args.get('page', 1, type=int)
  pagination = Event.query.filter_by(status=1).\
                  filter_by(category_banner=1). filter_by(category=category). order_by(Event.id).\
                  paginate(page, per_page=PER_PAGE, error_out=True, max_per_page=None)
  category_banners = pagination.items

  for category in CATEGORY_DB:
    return render_template(category+".html", 
                            result=data('banners', category_banners), 
                            pagination=pagination)


#api for front-end
@app.route('/api/banner', methods=['GET'])
def banner():
  all_banners = Event.query.all()
  result = data('banners', all_banners)
  return jsonify(result)


@app.route('/api/home_banner', methods=['GET'])
def get_home_banner():
  home_banners = Event.query.filter_by(status=1).filter_by(home_banner=1).all()
  result = data('banners', home_banners)
  return jsonify(result)


@app.route('/api/category_banner/<category>', methods=['GET'])
def get_category_banner(category):
  if category not in CATEGORY_DB:
    return 'Category is not found.', 400

  category_banners = Event.query.filter_by(
      status=1).filter_by(category_banner=1).filter_by(category=category).all()
  result = data('banners', category_banners)
  return jsonify(result)


@app.route('/api/events/<category>/<int:year>/<int:month>/<int:day>', methods=['GET'])
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


@app.route('/api/<category>/banner', methods=['GET'])
def get_banner(category):
  if category not in CATEGORY_DB:
    return 'Category is not found.', 400

  event_banners = Event.query.filter_by(category=category).all()
  if event_banners == None:
      return {}
  result = data('banner', event_banners)
  return jsonify(result)


#update event
@app.route('/api/event/<int:id>', methods=['GET', 'PUT'])
def each_event(id):
  event = Event.query.filter_by(id=id).first()

  if request.method == 'GET':
    if event == None: 
      return {}

    result = data('event', event)
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
  return "update success!"


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
    result = data('events', all_events)
    return jsonify(result)      

if __name__ == '__main__':
    app.run(port='5002')
