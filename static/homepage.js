var image = document.getElementById("image");
/*
$('button').on('click', function() {
  $.ajax({
        // Your server script to process the upload
        url: '/changeImage', //the url where the request is sending
        type: 'POST',      // this is a sending upload request

        // Form data
        data: new FormData($('form')[0]), //creating a form data to send

        // Tell jQuery not to process data or worry about content-type
        // You *must* include these options!
        cache: false,
        contentType: false,
        processData: false,

        // Custom XMLHttpRequest
        xhr: function() {
            var myXhr = $.ajaxSettings.xhr();
            if (myXhr.upload) {
                // For handling the progress of the upload
                myXhr.upload.addEventListener('progress', function(e) {
                    if (e.lengthComputable) {
                        $('progress').attr({
                            value: e.loaded,
                            max: e.total,
                        });
                    }
                } , false);
            }
            return myXhr;
        },

       success: function (response){
           $('button').remove();
      }
    });
});
*/
console.log("hellow owrld");


$('#button').on('click', function(){
  $.get("/hello", function(){
    console.log("seccuss");
  })
})
