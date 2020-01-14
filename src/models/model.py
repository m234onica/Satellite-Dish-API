from src import db
from datetime import datetime
import enum


class category_Enum(enum.Enum):
    music = 0
    visual_art = 1
    market = 2
    theatre = 3

class Event(db.Model):
  __tablename__ = 'events'
  id = db.Column(db.Integer, primary_key=True)
  img = db.Column(db.String(100), nullable=False)
  title = db.Column(db.String(50), nullable=False)
  link = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String, nullable=False)
  
  created_at = db.Column(db.DateTime, default=datetime.now())
  start_date = db.Column(db.Date, nullable=False)
  end_date = db.Column(db.Date, nullable=False)
  display_date = db.Column(db.String, nullable=False)

  region = db.Column(db.String, nullable=True)
  location = db.Column(db.String, nullable=False)
  note = db.Column(db.String, nullable=True)
  category = db.Column(db.Enum(category_Enum), nullable=False)
  reporter_name = db.Column(db.String(20), nullable=False)
  reporter_email = db.Column(db.String(50), nullable=False)
  reporter_phone = db.Column(db.String(20), nullable=False, unique=True)

  status = db.Column(db.Boolean, nullable=True)
  home_banner = db.Column(db.Boolean, nullable=True, default=False)
  category_banner = db.Column(db.Boolean, nullable=True, default=False)
  show_banner = db.Column(db.Boolean, nullable=True, default=False)
  

  def __repr__(self):
        return "Events('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            self.img,
            self.title,
            self.link,
            self.description,
            self.region,
            self.created_at,
            self.start_date,
            self.end_date,
            self.display_date,
            self.location,
            self.note,
            self.category,
            self.reporter_name,
            self.reporter_email,
            self.reporter_phone,
            self.status,
            self.home_banner,
            self.category_banner,
            self.show_banner
        )
