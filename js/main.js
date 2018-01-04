$(document).ready(function() {
  $(".loader-container").fadeOut("slow")
});

new TypeIt('#typeit', {
   strings: ["Software Engineer", "Full Stack Developer", "Ukulele Player"],
   speed: 100,
   breakLines: false,
   autoStart: true,
   loop: true
});
