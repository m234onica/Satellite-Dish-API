from flask import (Flask, request, jsonify, render_template, Blueprint, g,
                   current_app, url_for, redirect)

from datetime import date, datetime
from enum import Enum

from src import db
from src.tools.data import data
from src.tools.storage import decode_and_get_url
from src.models.model import Event, category_Enum, db
from config import CATEGORY_DB, ALLOWED_EXTENSIONS, PER_PAGE


cms = Blueprint('cms', __name__)



@cms.route('/event', methods=['GET'])
def events():
  page = request.args.get('page', 1, type=int)
  pagination = Event.query.order_by(Event.start_date.asc()).\
      paginate(page, per_page=PER_PAGE, error_out=True, max_per_page=None)
  all_events = pagination.items

  return render_template("event.html",
                         result=data('events', all_events),
                         pagination=pagination)


@cms.route('/banner', methods=['GET'])
def get_all_banner():
  page = request.args.get('page', 1, type=int)
  pagination = Event.query.filter_by(status=1).\
      filter(Event.show_banner != "hide").\
      paginate(page, per_page=PER_PAGE, error_out=True, max_per_page=None)
  all_banners = pagination.items

  return render_template("banners/all.html",
                         result=data('banners', all_banners),
                         pagination=pagination)


@cms.route('/home_banner', methods=['GET'])
def home_banner():
  page = request.args.get('page', 1, type=int)
  pagination = Event.query.filter_by(status=1).\
      filter(Event.show_banner != "hide").filter(Event.show_banner != "category").\
      paginate(page, per_page=PER_PAGE, error_out=True, max_per_page=None)
  home_banners = pagination.items

  return render_template("banners/home.html",
                         result=data('banners', home_banners),
                         pagination=pagination)


@cms.route('/category_banner/<category>', methods=['GET'])
def category_banner(category):
  if category not in CATEGORY_DB:
    return 'Category is not found.', 400

  page = request.args.get('page', 1, type=int)
  pagination = Event.query.filter_by(status=1).filter_by(category=category).\
      filter(Event.show_banner != "home").filter(Event.show_banner != "hide").\
      paginate(page, per_page=PER_PAGE, error_out=True, max_per_page=None)
  category_banners = pagination.items

  return render_template("banners/" + category + ".html",
                         result=data('banners', category_banners),
                         pagination=pagination, category=category)
