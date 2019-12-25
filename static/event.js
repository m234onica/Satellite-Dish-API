//get event data in modal
function get_event() {
  $('#event-list').on('click', '.event_detail_button', e => {
    e.preventDefault();
    var eventId = e.target.dataset.id;

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
}
get_event()

//update event data and accept it
$(document).ready(function () {
  $('.accept_button').click(function () {
    var eventId = $("#eventIndex").val();
    let Data = {
      'link': $('#eventLink').val(),
      'desc': $('#eventDesc').val(),
      'title': $('#eventTitle').val(),
      'start_date': $('#eventStart').val(),
      'end_date': $('#eventEnd').val(),
      'display_date': $('#eventDisplay').val(),
      'note': $('#eventTitle').val(),
      'location': $('#eventAddress').val(),
      'status': true,
      'region': $('#eventRegion').val(),
      'category': $('#eventCategory').val(),
      'home_banner': false,
      'category_banner': false
    }
    if ($("#eventHomeBanner").prop('checked')) {
      Data.home_banner = true
    } else {
      Data.home_banner = false
    }
    if ($("#eventCategoryBanner").prop('checked')) {
      Data.category_banner = true
    } else {
      Data.category_banner = false
    }
    form = JSON.stringify(Data)

    accept = $.ajax({
      type: "PUT",
      url: "/api/event/" + eventId,
      dataType: 'json',
      contentType: 'application/json; charset=utf-8',
      data: form,
    })
    accept.done(function (data) {
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
      'note': $('#eventTitle').val(),
      'location': $('#eventAddress').val(),
      'status': false,
      'region': $('#eventRegion').val(),
      'category': $('#eventCategory').val(),
      'home_banner': false,
      'category_banner': false
    }
    form = JSON.stringify(Data)

    reject = $.ajax({
      type: "PUT",
      url: "/api/event/" + eventId,
      dataType: 'json',
      contentType: 'application/json; charset=utf-8',
      data: form,
    })

    reject.done(function(data) {
      window.location.reload()
    })
  })
})

//get banner image
$('#banner-list').on('click', '.banner_image_button', e => {
  e.preventDefault();
  var eventId = e.target.dataset.id;
  $.ajax({
    type: "GET",
    url: "/api/event/" + eventId,
    dataType: 'json',
    contentType: 'application/json; charset=utf-8',
  }).done(function (data) {
    $('#bannerImage').attr('src', data[0].img)
  })
})
