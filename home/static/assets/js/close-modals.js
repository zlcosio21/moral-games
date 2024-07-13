$(document).ready(function () {

    $('#modalLogin').on('show.bs.modal', function () {
        if ($('#modalRegister').hasClass('show')) {
            $('#modalRegister').modal('hide');
        }
    });

    $('#modalRegister').on('show.bs.modal', function () {
        if ($('#modalLogin').hasClass('show')) {
            $('#modalLogin').modal('hide');
        }
    });

    $('[data-toggle="modal"]').on('click', function () {
        var targetModal = $(this).data('target');
        var currentModal = $(this).closest('.modal');

        if (currentModal.length) {
            currentModal.modal('hide');
            $(targetModal).modal('show');
        }
    });

});