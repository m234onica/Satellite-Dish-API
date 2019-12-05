from main import db
from datetime import datetime
import enum


class category_Enum(enum.Enum):
    music = 0
    visual_art = 1
    market = 2
    theater = 3

class event(db.Model):
  __tablename__ = 'events'
  id = db.Column(db.Integer, primary_key=True)
  img = db.Column(db.String(100), nullable=False)
  title = db.Column(db.String(50), nullable=False)
  link = db.Column(db.String(100), nullable=False)
  desc = db.Column(db.String, nullable=False)
  
  created_at = db.Column(db.DateTime, default=datetime.now)
  start_date = db.Column(db.DateTime, nullable=False)
  end_date = db.Column(db.DateTime, nullable=False)
  display_date = db.Column(db.String, nullable=False)

  location = db.Column(db.String, nullable=False)
  note = db.Column(db.String, nullable=True)
  category = db.Column(db.Enum(category_Enum), nullable=False)
  reporter_name = db.Column(db.String(20), nullable=False)
  reporter_email = db.Column(db.String(50), nullable=False)
  reporter_phone = db.Column(db.String(20), nullable=False, unique=True)

  def __init__(self, img, title, link, desc, created_at, start_date, end_date, display_date, location, note, category, reporter_name, reporter_email, reporter_phone):
    self.img = img
    self.title = title
    self.link = link
    self.desc = desc
    self.created_at = created_at
    self.start_date = start_date
    self.end_date =end_date
    self.display_date = display_date
    self.location = location
    self.note = note
    self.category = category
    self.reporter_name = reporter_name
    self.reporter_email = reporter_email
    self.reporter_phone = reporter_phone

  def __repr__(self):
        return "Events('{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            self.img,
            self.title,
            self.link,
            self.desc,
            self.created_at,
            self.start_date,
            self.end_date,
            self.display_date,
            self.location,
            self.note,
            self.category,
            self.reporter_name,
            self.reporter_email,
            self.reporter_phone
        )
