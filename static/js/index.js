$(document).ready(function () {
  $("#imgSend").click(function (e) {
    e.preventDefault();

    var form = new FormData();
    var _img = $("#pic").get(0);
    var img = _img.files;
    var colorCnt = $(".colorCnt").val();
    form.append("img", img[0], img[0].name);

    var settings = {
      "async": true,
      "crossDomain": true,
      "url": "/pick/colors/" + colorCnt,
      "method": "POST",
      "processData": false,
      "contentType": false,
      "mimeType": "multipart/form-data",
      "data": form,
      dataType: "JSON"
    };

    $.ajax(settings).done(function (res) {
      console.log('잘됐다!');
      console.log(res);
      
      for(i = 0; i<res.colors.length; i++) {
        $($(".resColors")[i]).css("background-color", res.colors[i].hex);
      }
    }).fail(function (err) {
      console.log(err);
      alert('뭔가 이상해~');
    });
  });
});

function previewFile() {
  var preview = document.querySelector('#imgPreview');
  var file    = document.querySelector('input[type=file]').files[0];
  var reader  = new FileReader();

  reader.addEventListener("load", function () {
    preview.src = reader.result;
    $(preview).show();
  }, false);

  if (file) {
    reader.readAsDataURL(file);
  }
}