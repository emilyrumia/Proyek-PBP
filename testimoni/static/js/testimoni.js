$(document).ready(function(){
    $.getJSON("json/", function(data) {
        $.each(data, function(key, testimoni) {
            $("#testimoni_cards").append('<div class="col-12 col-md-6 col-lg-4">' +
                                            '<div class="card w-75">' +
                                            '<div class="card-body text-center">' +
                                                '<p id="pesan" class="card-text">' + testimoni.fields.pesan + '</p>' +
                                            '</div>' +
                                            '<div class="card_nama">' +
                                                '<h6 id="nama" class="card-subtitle mb-2 text-muted">' + "from: " + testimoni.fields.nama + '</h6>' +
                                            '</div>' +
                                            '<ul id="list" class="list-group list-group-flush">' +
                                                '<li class="list-group-item">' + "Target: " + testimoni.fields.target + '</li>' + 
                                            '</ul' +
                                            '</div>'+
                                        '</div>');

        })
    });

    $("#submit_testimoni").click(function(e){

        e.preventDefault();

        $.ajax({
            type : 'POST',
            url : '/testimoni/add-testimoni/',        
            data : $('#testimoni_form').serialize(),
            
            success: function(response){
                // Mengambil isi dari field forum post
                nama = $('#id_nama').val(),
                target = $('#id_target').val(),
                pesan = $('#id_pesan').val() 
                
                if(nama.length === 0){
                    nama = "Anonymous";
                }
                if(target.length === 0){
                    target = "-";
                }

                new_data = {
                    nama : nama,
                    target : target,
                    pesan : pesan,
                    csrfmiddlewaretoken : '{{ csrf_token }}'
                }

                $("#testimoni_cards").append('<div class="col-12 col-md-6 col-lg-4">' +
                                                            '<div class="card w-75">' +
                                                            '<div class="card-body text-center">' +
                                                                '<p id="pesan" class="card-text">' + pesan + '</p>' +
                                                            '</div>' +
                                                            '<div class="card_nama">' +
                                                                '<h6 id="nama" class="card-subtitle mb-2 text-muted">' + "from: " + nama + '</h6>' +
                                                            '</div>' +
                                                            '<ul id="list" class="list-group list-group-flush">' +
                                                                '<li class="list-group-item">' + "Target: " + target + '</li>' + 
                                                            '</ul' +
                                                            '</div>'+
                                                        '</div>');

                // Menghapus text dalam field setelah submit                                   
                $("#id_nama").val('');
                $("#id_target").val('');
                $("#id_pesan").val(''); 

                // Menutup modal setelah submit
                $('#create_testimoni_modal').modal('hide')
            },
            error: function(error){
                console.log(error)
            },
        })
    });
});