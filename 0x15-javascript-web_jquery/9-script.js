$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr)&format=json', function (data, textStatus) {
    if (textStatus === 'success') {
      $('#sf_wind_speed').text(data.query.results.channel.wind.speed);
    }
  });
});
