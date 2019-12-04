from flask import Flask, request, jsonify
from main import create_app
from models import event
from datetime import date, timedelta, time
import json

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


@app.route('/events/<years>/<months>/<days>', methods=['GET'])
def get_events(years, months, days):
  event_data = event.query.all()
  urlDate = date(int(years), int(months), int(days))
  searchEndDate = urlDate - timedelta(days=+7)

  for data in event_data:
    # start_date = datetime.strptime(data['start_date'], "%Y-%m-%d")
    # end_date = datetime.strptime(data['end_date'], "%Y-%m-%d")
    start = data.start_date
    end = data.end_date
    if searchEndDate > start and urlDate <= end:
      result = {
        "start":start,
        "end":end,
        "title":data.title
      }
      return result
    else:
      return 'No data'
  
if __name__ == '__main__':
  app.run(port='5002', debug=True)


