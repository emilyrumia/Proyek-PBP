  function showKomentar() {
    $.ajax({
      type: "GET",
      url: url ,
      data: {csrfmiddlewaretoken: "{{ csrf_token }}"},
      dataType: "json",
      success: function (data) {
        console.log(data)
        show(data)
      }
    })
  }

  const url = ""

  function show(data) {
    let comments= ``;

    for (let i of data) {
      comments += `
                <br>
                <div style="border-bottom:1px solid rgb(202, 200, 200);">
                    <br>
                      <span id="span-user"><img id="img-user" src="/static/images/profile.png" style="max-height:300px">
                        <h5>&nbsp;${i.fields.username}</h5></span>
                      <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;${i.fields.komentar}</p>
                      <p style="text-align:end">${i.fields.tanggal_komentar}</p>
                </div>
              `
    }
    
    document.getElementById("show-komentar").innerHTML = comments;
  }

  $(document).ready(function () {
    showKomentar()
  });
