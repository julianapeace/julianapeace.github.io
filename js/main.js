$(document).ready(function() {
  $(".loader-container").fadeOut("slow")
});

new TypeIt('#typeit', {
   strings: ["Software Developer", "Penetration Tester", "Ukulele Player"],
   speed: 200,
   breakLines: false,
   autoStart: true,
   loop: false
});
