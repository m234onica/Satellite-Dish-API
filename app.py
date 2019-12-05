from flask import Flask, request, jsonify
from main import create_app
from sqlalchemy import or_
from models import event
from datetime import date, timedelta, time

app = create_app()


# fake_data = [
#     {
#         "img": "https://satellite-l5yx88bg3.now.sh/fakePics/1.jpeg",
#         "title": "Urban Nomad Freakout Music Fest | 2019 遊牧怪奇音樂祭",
#         "region": "北部",
#         "date": {
#             "start": "2019-11-01",
#             "end": "2019-12-10"
#         },
#         "display_date": "11/20（一）、11/30（一）、12/5 （一）",
#         "address": "新光三越 台北信義新天地(台北市台北市信義區松高路19號)",
#         "link": "https://accupass",
#         "desc": "dddddddd"
#     }
# ]


@app.route('/events/<categories>/<years>/<months>/<days>', methods=['GET'])
def get_events(categories, years, months, days):
    
  urlDate = date(int(years), int(months), int(days))
  searchEndDate = urlDate - timedelta(days=-7)
  
  event_data = event.query.filter_by(category=categories).\
      filter(~(or_(event.end_date < urlDate, event.start_date > searchEndDate))).all()
  print(type(event_data))
  if not event_data:
    return 'No data'
  for data in event_data:
    result = [
      {
        "img": data.img,
        "title": data.title,
        "date": {
            "start": data.start_date,
            "end": data.end_date,
        },
        "display_date": data.display_date,
        "address": data.location,
        "link": data.link,
        "desc": data.desc
      }
    ]
    return jsonify(result)

  
    
    
if __name__ == '__main__':
    app.run(port='5002', debug=True)
