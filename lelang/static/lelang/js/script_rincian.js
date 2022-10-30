
function konfirmasiBid(){
    const bid = $('input[name=banyak_bid]').val();
    $('#confirmation-bid-modal').text(`Anda akan bid barang lelang ini sejumlah Rp${bid}`);
}

function bidBarangLelang(item_id){
    const serializedData = getFormData($('#form-bid'));
    const bidURL = `/lelang/bid_barang_lelang/${item_id}`;
    $.ajax({
        type: 'POST',
        url: bidURL,
        data: serializedData,
        success: function (response) {
            const div = $(`#bid-tertinggi-${item_id}`);
            const rasio_donasi = response[0]["fields"]["banyak_bid"]
            div.children('h4').children('strong').text(`Rp${response[0]["fields"]["banyak_bid"].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`);
            div.children('span').text(`oleh ${response[0]["username"]}`);
            div.append(
                `<div class="modal fade" id="modalBid" tabindex="-1" aria-labelledby="modalBidLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                            <h5 class="modal-title" id="modalBidLabel">Informasi</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                            Bidding berhasil.
                            </div>
                        </div>
                    </div>
                </div>`
            );
            $('input[name=banyak_bid]').val('');
            $("#modalBid").modal('show');
            $('.modal-backdrop').remove();
            setTimeout(function(){
                $("#modalBid").modal('hide');
            }, 1500);
            setTimeout(function(){
                $("#modalBid").remove();
            }, 5000);
            
        },
        error: function (response) {
            alert(`Bid anda harus lebih besar dari Rp${response.responseText}`);
        }
    })
}

function addKomentar(item_id){
    const serializedData = getFormData($('#form-komentar'));
    const komentarURL = `/lelang/komentar_barang_lelang/${item_id}`;
    $.ajax({
        type: 'POST',
        url: komentarURL,
        data: serializedData,
        success: function (response) {
            const container = $(`.komentar`);
            container.append(
                `<h5>${response[0]["username"]}</h5>
                <p>${response[0]["fields"]["teks"]}</p>
                <span class="float-end">Baru saja</span>
                <div class="my-3" style="border-bottom:1px solid rgb(202, 200, 200);"><br></div>`
            );
            $('textarea[name=teks]').val('');
        },
    })
}

function getFormData($form){
    var unindexed_array = $form.serializeArray();
    var indexed_array = {};

    $.map(unindexed_array, function(n, i){
        indexed_array[n['name']] = n['value'];
    });

    return indexed_array;
}