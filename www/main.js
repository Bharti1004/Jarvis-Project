$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect:"bounceIn",
        },
        out:{
            effect:"bounceOut",
        },
    })
<<<<<<< HEAD
=======

    //Siri Configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 840,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
      });

      //Siri message animation
      $('.siri-message').textillate({
        loop: true,
        sync: true,
        in:{
            effect:"fadeInUp",
            sync: true
        },
        out:{
            effect:"fadeOutUp",
            sync: true
        },
    })
>>>>>>> 8c8b51f (Jarvis)
});