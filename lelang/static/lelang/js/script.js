
function bidBarangLelang(item_id){
    const serializedData = getFormData($('#form-bid'));
    const bidURL = `/lelang/bid_barang_lelang/${item_id}`;
    $.ajax({
        type: 'POST',
        url: bidURL,
        data: serializedData,
        success: function (response) {
            const div = $(`#bid-tertinggi-${item_id}`);
            div.children('h4').children('strong').text(`Rp${response[0]["fields"]["banyak_bid"].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`);
            div.children('span').text(`oleh ${response[0]["username"]}`);
        },
        error: function (response) {
            console.log(response);
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
            console.log(response);
            const container = $(`.komentar`);
            console.log(container);
            container.append(
                `<h5>${response[0]["username"]}</h5>
                <p>${response[0]["fields"]["teks"]}</p>
                <span class="float-end">0 minutes lalu</span>
                <div class="my-3" style="border-bottom:1px solid rgb(202, 200, 200);"><br></div>`
            );
        },
        error: function (response) {
            console.log(response);
            alert(response.responseText);
        }
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