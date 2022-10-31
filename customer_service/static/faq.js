
// // Displaying for the first time
// $(document).ready(displayFAQ())
// $(document).ready(displayPertanyaan())

// Script untuk FORM PERTANYAAN 
function submitPertanyaan() {
  $.ajax({
    url: "add-pertanyaan/",
    type: 'POST',
    data: { csrfmiddlewaretoken: window.CSRF_TOKEN,
        'kategori': $('#kategori').val(),
        'teks_pertanyaan': $('#teks_pertanyaan').val() }, 
    success: function(res){
      var html = `<div class="col">
                  <div class="card">
                  <div class="card-header h5" style="vertical-align: middle;">
                      <strong> ${res.fields.teks_pertanyaan} </strong></div>
                  <div class="card-body">
                  <form id="${res.pk}">
                      {% csrf_token %}
                      {{ form_jawaban|crispy }}
                  <div class="container text-center mt-3">
                      <button type="button" class="btn btn-primary" onclick = 'submitAnswer("${res.pk}")' id="submit-ans">Submit Answer</button>
                  </div>
                  </form>
                  </div>
              </div>
              <br>
              </div>`
      $('#display-pertanyaan').append(html)
    }
  });
  $('#form-modal')[0].reset();
  $("#modalPertanyaan").modal('hide');
}

// Script untuk FORM JAWABAN
function submitAnswer(id) {    
  $.ajax({
    url: "add-jawaban/"+id,
    type: 'POST',
    data: { csrfmiddlewaretoken: window.CSRF_TOKEN,
          'jawaban': $('#jawaban').val() }, 

    success: function(res) {
      var html = `<div class="col">
                    <div class="card">
                      <div class="card-header h5" style="vertical-align: middle;">
                        <strong>${res.fields.pertanyaan.fields.teks_pertanyaan}</strong></div>
                        <div class="card-body">
                          <p class="card-text">${res.fields.jawaban}</p>
                        </div>
                      </div>
                    <br>
                  </div>`           
      $('#display-faq').append(html)
      displayPertanyaan()
    }
  }); 
  $('#form-jawaban')[0].reset();
  $("#modalJawaban").modal('hide');
}

// Script untuk MENAMPILKAN FAQ
function displayFAQ() {
  $.ajax({
    url: "json/faq",
    type: 'GET',
    dataType: 'json',
    success: function(res) {
      var htmlString = ""
      res.forEach((faq) => {
        if (faq.fields.pertanyaan[0] == "UMUM") {
            htmlString += `<button class="accordion umum rounded">
                            <i class="fa-solid fa-circle-question" style="font-size:1.25em; padding-right:8px;"></i>
                            <strong style="font-size:18px;">${faq.fields.pertanyaan[1]}</strong>
                            </button>
                            <div class="panel rounded">
                                <h6 style="margin-block: 18px;">${faq.fields.jawaban}</h6>
                            </div>
                        <span class="break"></span>`
        } else if (faq.fields.pertanyaan[0] == "LELANG") {
            htmlString += `<button class="accordion lelang rounded">
                            <i class="fa-solid fa-gavel" style="font-size:1.5em; padding-right:8px;"></i>
                            <strong style="font-size:18px;">${faq.fields.pertanyaan[1]}</strong></button>
                            <div class="panel rounded">
                                <h6 style="margin-block: 18px;">${faq.fields.jawaban}</h6>
                            </div>
                        <span class="break"></span>`
        } else {
            htmlString += `<button class="accordion galang rounded">
                            <i class="fa-solid fa-hand-holding-dollar" style="font-size:1.5em; padding-right:8px;"></i>
                            <strong style="font-size:18px;">${faq.fields.pertanyaan[1]}</strong></button>
                            <div class="panel rounded">
                                <h6 style="margin-block: 18px;">${faq.fields.jawaban}</h6>
                            </div>
                        <span class="break"></span>`
        }
      }); $('#display-faq').html(htmlString)

      // SCRIPT BUAT ACCORDION
      var acc = document.getElementsByClassName("accordion");
      var i;
      
      for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
          if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
          } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
          } 
        });
      }
    }
  });
}

// JQUERY BUAT MODAL 
$(document).ready(function(){
  const modalJawaban = document.getElementById('modalJawaban')
  modalJawaban.addEventListener('show.bs.modal', event => {

  // Button that triggered the modal
  const button = event.relatedTarget

  // Extract info from data-bs-* attributes
  const id = button.getAttribute('data-bs-id')
  const qs = button.getAttribute('data-bs-qs')

  // Change id of form-jawaban
  let btn = document.getElementById('submit-ans')
  btn.id = id

  // Update the modal's content.
  const modalTitle = modalJawaban.querySelector('.modal-title')
  modalTitle.textContent = qs

  })
})

// Script untuk MENAMPILKAN PERTANYAAN  
function displayPertanyaan() {
  $.ajax({
      url: "json/pertanyaan",
      type: 'GET',
      dataType: 'json',
      success: function(res) {
        var htmlString = ""
        res.forEach((pertanyaan) => {
          htmlString += `<div class="col">
                        <div class="card">
                          <div class="card-body">
                          <h5 class="card-title" style="padding:10px;">${pertanyaan.fields.teks_pertanyaan}</h5>
                          <div class="btn-toolbar w-100 container g-4 mt-3" style="padding:5px">
                            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalJawaban" 
                              data-bs-id=${pertanyaan.pk} data-bs-qs="${pertanyaan.fields.teks_pertanyaan}">
                              Answer</button>
                            <button type="button" class="btn btn-danger" onclick='deletePertanyaan("${pertanyaan.pk}")' id="btn-delete">Delete</button>
                          </div>
                        </div>
                      </div>
                      <br>
                    </div>`
        }); 
        $('#display-pertanyaan').html(htmlString)
      }
  });
}

// Script buat HAPUS PERTANYAAN
function deletePertanyaan(id){ 
  $.ajax({
      url: "delete/"+id,
      type: "DELETE",
      success: function(res){
          // $("#col-" + id).remove();
          alert("berhasil dihapus")
          displayPertanyaan()
      }
  });
}

// Displaying for the first time
$(document).ready(displayPertanyaan())
$(document).ready(displayFAQ())




