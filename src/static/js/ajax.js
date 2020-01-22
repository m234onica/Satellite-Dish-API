//get event data in modal
$('.event_detail_button').click(function() {
  var eventId = $(this).find('.detail_icon').attr('data-id');
  
  $.ajax({
    type: "GET",
    url: "api/event/" + eventId,
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
    $('#eventDesc').val(data[0].description)
    $('#eventReporterName').val(data[0].reporter.name)
    $('#eventReporterEmail').val(data[0].reporter.email)
    $('#eventReporterPhone').val(data[0].reporter.phone)
    $('#eventImage').attr('src', data[0].img)
    $('#eventCategory').val(data[0].category)
    $('#eventRegion').val(data[0].region)

    
    if (data[0].show_banner == "all") {
      $('#eventHomeBanner').attr('checked', true)
      $('#eventCategoryBanner').attr('checked', true)
      
    }else if (data[0].show_banner == "home") {
      $('#eventHomeBanner').attr('checked', true)
      $('#eventCategoryBanner').attr('checked', false)
      
    } else if (data[0].show_banner == "category") {
      $('#eventHomeBanner').attr('checked', false)
      $('#eventCategoryBanner').attr('checked', true)
    } 
    console.log(data[0]);
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
    'show_banner': "hide"
  }

  var checkedHome = $("#eventHomeBanner").prop('checked')
  var checkedCate = $("#eventCategoryBanner").prop('checked')

  console.log(checkedHome, checkedCate);
  

  if (checkedHome && !checkedCate) {
    Data.show_banner = "home";
  } else if (!checkedHome && checkedCate) {
    Data.show_banner = "category"
  } else if (checkedCate && checkedCate) {
    Data.show_banner = "all"
  } 
  
  $.ajax({
    type: "POST",
    url: "api/event/" + eventId,
    dataType: 'json',
    contentType: 'application/json; charset=utf-8',
    data: JSON.stringify(Data),
  }).done(function (data) {
    window.location.reload()    
  })
})

//update event data and reject it
$('.reject_button').click(function () {
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
    'region': $('#eventRegion').val(),
    'category': $('#eventCategory').val(),
    'status': false,
    'show_banner': "hide"
  }

  $.ajax({
    type: "POST",
    url: "api/event/" + eventId,
    dataType: 'json',
    contentType: 'application/json; charset=utf-8',
    data: JSON.stringify(Data)
  }).done(function(data) {
    window.location.reload()
  })
})

//get banner image
$('.banner_image_button').click(function() {
  var imageId = $(this).find('.image_icon').attr('data-id');
  
  $.ajax({
    type: "GET",
    url: "api/event/" + imageId,
    dataType: 'json',
    contentType: 'application/json; charset=utf-8',
  }).done(function (data) {
    $('#bannerImage').attr('src', data[0].img)
  })
})
