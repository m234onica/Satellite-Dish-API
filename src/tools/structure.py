def event(id, img, title, category, region, start_date, end_date, display_date, note, location, link, desc, reporter_name, reporter_email, reporter_phone, status, home_banner, category_banner, show_banner):
  structure = {
      "index": id,
      "img": img,
      "title": title,
      "category": category,
      "region": region,
      "date": {
          "start": start_date,
          "end": end_date,
      },
      "display_date": display_date,
      "note": note,
      "address": location,
      "link": link,
      "desc": desc,
      "reporter": {
          "name": reporter_name,
          "email": reporter_email,
          "phone": reporter_phone,
      },
      "status": status,
      "banner": {
          "home": home_banner,
          "category": category_banner,
          "show": show_banner
      }
  }
  return structure


def filter_events(img, title, region, start_date, end_date, display_date, location, link, desc):
  structure = {
    "img": img,
    "title": title,
    "region": region,
    "date": {
        "start": start_date,
        "end": end_date,
    },
    "display_date": display_date,
    "address": location,
    "link": link,
    "desc": desc
  }
  return structure

def banner(id, img, title, display_date, location, desc):
  structure = {
      "index": id,
      "img": img,
      "title": title,
      "display_date": display_date,
      "address": location,
      "desc": desc
  }
  return structure
