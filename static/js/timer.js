$(document).ready(function() {
    MAX_SIZE = 1000;
    $(".matrix_form").submit(function (event) {
        event.preventDefault();
        $(".matrix_c").html('');
        var start = new Date().getTime();
        $.ajax({
            url: '/',
            type: "POST",
            data: $(this).serialize(),
            success: function (data) {
                $(".matrix_c").html(data.matrix_c || '');
                $(".error_a").html(data.errors && data.errors.matrix_a || '');
                $(".error_b").html(data.errors && data.errors.matrix_b || '');
                var end = new Date().getTime();
                var time = end - start;
                $(".time").text('(request time: ' + time + 'ms)');
            }
        });
    });
    $(".mult_form").submit(function (event) {
        event.preventDefault();
        $(".matrix_c").html('');
        var start = new Date().getTime();
        $.ajax({
            url: '/',
            type: "POST",
            data: $(this).serialize(),
            success: function (data) {
                $(".matrix_c").html(data.matrix_c || '');
                /*$(".error_a").html(data.errors && data.errors.matrix_a || '');
                $(".error_b").html(data.errors && data.errors.matrix_b || '');*/
                var end = new Date().getTime();
                var time = end - start;
                $(".time").text('(request time: ' + time + 'ms)');
            }
        });
    });
    $(".gen_form").submit(function (event) {
        event.preventDefault();
        raw_num = $("#id_a_raw_num").val();
        col_num = $("#id_a_col_num").val();
        matrix_a = '';
        matrix_b = '';
        if (raw_num <= MAX_SIZE && col_num <= MAX_SIZE)
        {
            for (i = 0; i < raw_num; i++) {
                for (j = 0; j < col_num; j++) {
                    matrix_a += '1 '
                }
                matrix_a += '\n'
            }
            for (i = 0; i < col_num; i++) {
                for (j = 0; j < raw_num; j++) {
                    matrix_b += '1 '
                }
                matrix_b += '\n'
            }
        } else {
            matrix_a = matrix_b = 'Matrix is too big! (Raw and column number must be less or equal ' + MAX_SIZE +')';
        }
        $("#id_matrix_a").val(matrix_a);
        $("#id_matrix_b").val(matrix_b);
    });
});