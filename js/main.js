$(document).ready(function() {
  $(".loader-container").fadeOut("slow")
});

new TypeIt('#typeit', {
   strings: ["It's going to be alright :)"],
   speed: 200,
   breakLines: false,
   autoStart: true,
   loop: false
});
