//get event data in modal
$('.event_detail_button').click(function() {
  var eventId = $(this).find('.detail_icon').attr('data-id');
  
  $.ajax({
    type: "GET",
    url: "/api/event/" + eventId,
    dataType: 'json',
    contentType: 'application/json; charset=utf-8',
  }).done(function (data) {
    $('#eventIndex').val(data[0].index)
    $('#eventTitle').val(data[0].title)
    $('#eventLink').val(data[0].link)
    $('#eventStart').val(data[0].date.start)
    $('#eventEnd').val(data[0].date.end)
    $('#eventDisplay').val(data[0].display_date)
    $('#eventNote').val(data[0].note)
    $('#eventAddress').val(data[0].address)
    $('#eventDesc').val(data[0].desc)
    $('#eventReporterName').val(data[0].reporter.name)
    $('#eventReporterEmail').val(data[0].reporter.email)
    $('#eventReporterPhone').val(data[0].reporter.phone)
    $('#eventImage').attr('src', data[0].img)
    $('#eventCategory').val(data[0].category)
    $('#eventRegion').val(data[0].region)

    if (data[0].banner.home == true) {
      $('#eventHomeBanner').attr('checked', true)
    } else {
      $('#eventHomeBanner').attr('checked', false)
    }
    
    if (data[0].banner.category == true) {
      $('#eventCategoryBanner').attr('checked', true)
    } else {
      $('#eventCategoryBanner').attr('checked', false)
    }
  })
})

//update event data and accept it

$('.accept_button').click(function () {
  var eventId = $("#eventIndex").val();
  var Data = {
    'link': $('#eventLink').val(),
    'desc': $('#eventDesc').val(),
    'title': $('#eventTitle').val(),
    'start_date': $('#eventStart').val(),
    'end_date': $('#eventEnd').val(),
    'display_date': $('#eventDisplay').val(),
    'note': $('#eventNote').val(),
    'location': $('#eventAddress').val(),
    'status': true,
    'region': $('#eventRegion').val(),
    'category': $('#eventCategory').val(),
    'home_banner': false,
    'category_banner': false,
    'show_banner': false
  }
  
  if ($("#eventHomeBanner").prop('checked')) {
    Data.home_banner = true;
    Data.show_banner = true;
  } else {
    Data.home_banner = false;
  }
  
  if ($("#eventCategoryBanner").prop('checked')) {
    Data.category_banner = true
  } else {
    Data.category_banner = false
  }

  if (Data.category_banner == true || Data.home_banner == true ){
    Data.show_banner = true;
  } else{
    Data.show_banner = false;
  }
  
  form = JSON.stringify(Data)
  $.ajax({
    type: "PUT",
    url: "/api/event/" + eventId,
    dataType: 'json',
    contentType: 'application/json; charset=utf-8',
    data: form,
  }).done(function (data) {
    window.location.reload()    
  })
})

//update event data and reject it
$('.reject_button').click(function () {
  var eventId = $("#eventIndex").val();
  let Data = {
    'link': $('#eventLink').val(),
    'desc': $('#eventDesc').val(),
    'title': $('#eventTitle').val(),
    'start_date': $('#eventStart').val(),
    'end_date': $('#eventEnd').val(),
    'display_date': $('#eventDisplay').val(),
    'note': $('#eventNote').val(),
    'location': $('#eventAddress').val(),
    'status': false,
    'region': $('#eventRegion').val(),
    'category': $('#eventCategory').val(),
    'home_banner': false,
    'category_banner': false,
    'show_banner': false
  }
  form = JSON.stringify(Data)

  $.ajax({
    type: "PUT",
    url: "/api/event/" + eventId,
    dataType: 'json',
    contentType: 'application/json; charset=utf-8',
    data: form,
  }).done(function(data) {
    window.location.reload()
  })
})

//get banner image
$('.banner_image_button').click(function() {
  var imageId = $(this).find('.image_icon').attr('data-id');
  
  $.ajax({
    type: "GET",
    url: "/api/event/" + imageId,
    dataType: 'json',
    contentType: 'application/json; charset=utf-8',
  }).done(function (data) {
    $('#bannerImage').attr('src', data[0].img)
  })
})
