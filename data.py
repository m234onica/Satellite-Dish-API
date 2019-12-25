from structure import filter_events, event, banner

def data(data_type, all_data):
  result = []

  if data_type == "event":
    each_event_category = all_data.category
    result.append(event(all_data.id,
                        all_data.img,
                        all_data.title,
                        each_event_category.name,
                        all_data.region,
                        all_data.start_date.strftime("%Y-%m-%d"),
                        all_data.end_date.strftime("%Y-%m-%d"),
                        all_data.display_date,
                        all_data.note,
                        all_data.location,
                        all_data.link,
                        all_data.desc,
                        all_data.reporter_name,
                        all_data.reporter_email,
                        all_data.reporter_phone,
                        all_data.status,
                        all_data.home_banner,
                        all_data.category_banner)
                  )

  elif data_type == 'events':
    for each_data in all_data:
      each_event_category = each_data.category
      result.append(event(each_data.id,
                        each_data.img,
                        each_data.title,
                        each_event_category.name,
                        each_data.region,
                        each_data.start_date.strftime("%Y-%m-%d"),
                        each_data.end_date.strftime("%Y-%m-%d"),
                        each_data.display_date,
                        each_data.note,
                        each_data.location,
                        each_data.link,
                        each_data.desc,
                        each_data.reporter_name,
                        each_data.reporter_email,
                        each_data.reporter_phone,
                        each_data.status,
                        each_data.home_banner,
                        each_data.category_banner,
                        )
                    )

  elif data_type == "filter_events":
    for each_data in all_data:
      result.append(filter_events(each_data.img,
                        each_data.title,
                        each_data.region,
                        each_data.start_date.strftime("%Y-%m-%d"),
                        each_data.end_date.strftime("%Y-%m-%d"),
                        each_data.display_date,
                        each_data.location,
                        each_data.link,
                        each_data.desc,
                        )
                    )

  elif data_type == "banners":
    for each_data in all_data:
      result.append(banner(each_data.id,
                        each_data.img,
                        each_data.title,
                        each_data.display_date,
                        each_data.location,
                        each_data.desc,
                        )
                    )
  else:
    return 'Wrong data type.'
  return result
