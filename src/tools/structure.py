def event(id, img, title, category, region, start_date, end_date, display_date, note, location, link, description, reporter_name, reporter_email, reporter_phone, status, show_banner):
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
      "desc": description,
      "reporter": {
          "name": reporter_name,
          "email": reporter_email,
          "phone": reporter_phone,
      },
      "status": status,
      "show_banner": show_banner
  }
  return structure


def filter_events(img, title, region, start_date, end_date, display_date, location, link, description):
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
    "desc": description
  }
  return structure


def banner(id, img, title, display_date, location, description):
  structure = {
      "index": id,
      "img": img,
      "title": title,
      "display_date": display_date,
      "address": location,
      "desc": description
  }
  return structure
