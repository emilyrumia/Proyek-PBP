$(document).ready(function(){
    $('#dropdown-kategori').hover(function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(50).fadeIn(100);
    }, function() {
        $(this).find('.dropdown-menu').stop(true, true).delay(50).fadeOut(100);
    });
    const getTaskURL = window.location.href + "json";
    $.ajax({
    type: 'GET',
    url: getTaskURL,
    success: function (response) {
        if (!response.length){
            $('#card-grid').prepend(`
            <div class="d-flex justify-content-center" id="no-task-div">
                <h1>No Task :)</h1>
            </div>`)
        }
        else{
            for (let i = 0; i < response.length; i++){
                const time_different = new Date(response[i]["fields"]["tanggal_berakhir"]) - new Date();
                var days = Math.floor(time_different / 1000 / 60 / 60/ 24);
                var hours = Math.floor(time_different / 1000 / 60 / 60);
                var minutes = Math.floor(time_different / 1000 / 60);
                var output = days + " days";
                if (days <= 0){
                    if (hours <= 0){
                        output = minutes + " minutes";
                    }
                    else{
                        output = hours + " hours";
                    }
                }
                var imgSrc = `/media/${response[i]["fields"]["gambar"]}`;
                var img = new Image(); 
                img.onerror = function(){imgSrc = `https://tk-pbp-bidcare.s3.ap-southeast-1.amazonaws.com/${response[i]["fields"]["gambar"]}`};
                img.src = imgSrc;

                $('#container-index-lelang').append(
                    `<div class="col">
                    <a href="${response[i]["pk"]}" style="text-decoration:none; color:black;">
                        <div class="card border-light h-100 ">
                            <div class="img-container">
                                <img src="${imgSrc}" class="card-img-top" alt="${response[i]["fields"]["nama_barang"]}" style="max-width: 100%;max-height: 100%;object-fit: cover;"> 
                            </div>
                            <div class="card-body"> 
                                <div class="clearfix mb-3"> 
                                    ${response[i]["fields"]["status_keaktifan"] ? '<span class="float-start badge rounded-pill bg-success">Aktif</span>': '<span class="float-start badge rounded-pill bg-danger">Tidak Aktif</span>'}
                                </div> 
                                <h5 class="card-title" style="color: rgb(70, 70, 70);">${response[i]["fields"]["nama_barang"]}</h5>
                                <h5><strong>Rp${response[i]["fields"]["bid_tertinggi"].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}</strong></h5>
                                ${response[i]["fields"]["status_keaktifan"] ? `<span class="badge bg-primary">${output}</span>`: '<span class="badge bg-primary">Lelang Selesai</span>'}
                            </div> 
                        </div> 
                    </a>
                </div> `
                )
            }
        }
    },
    error: function (response) {
        console.log(response);
    }
    })  
});

function checkImage(imageSrc, good, bad) {
    var img = new Image();
    img.onload = good; 
    img.onerror = bad;
    img.src = imageSrc;
}