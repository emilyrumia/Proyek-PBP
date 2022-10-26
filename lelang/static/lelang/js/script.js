$("#add-lelang-btn").click(function(e){
    e.preventDefault();
    const serializedData = getFormData($('#add-task-form'));
    $.ajax({
        type: 'POST',
        url: addTaskURL,
        data: serializedData,
        success: function (response) {
            // on successfull creating object
            $("#add-task-form").trigger('reset');
            $("#title-input").focus();
            // display the newly friend to table.
            var instance = JSON.parse(response);
            var fields = instance[0]["fields"];
            var task_id = instance[0]["pk"];
            if ($('#no-task-div').length){
                $('#no-task-div').remove();
                $('#card-grid').prepend('<h1 class="text-center id="task-exist-h1">Todolist</h1>');
            }
            addTaskAsync($('#card-grid'), fields, task_id);
        },
        error: function (response) {
            // alert the error if any error occured
            alert(response["responseJSON"]["error"]);
        }
        })
        $('#staticBackdrop').modal('hide');
});