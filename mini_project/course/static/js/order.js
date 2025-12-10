$('#orderCreate').submit(function (event) {
    event.preventDefault();
    let form = $(this);
    let data = {};

    $.each($(form).serializeArray(), function(index, field) {
        data[field.name] = field.value;
    });

    $.ajax(form.attr('action'), {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': data,
        'success': function (response) {
            $('#OrderCreateModal').modal('hide');
            $('#customAlert').modal('show');

            form[0].reset(); // reset every inputs in the form
        },
    });
});
