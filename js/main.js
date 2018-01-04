$(document).ready(function() {
  $(".loader-container").fadeOut("slow")
  $('#nav').onePageNav();
});

$(function() {
  $.stellar({
    horizontalScrolling: false,
    verticalOffset: 40
  });
});

new TypeIt('#typeit', {
   strings: ["Software Engineer", "Full Stack Developer", "Ukulele Player"],
   speed: 100,
   breakLines: false,
   autoStart: false,
   loop: true
});
