$(document).ready(function() {
    $('h2').append('<button style="float: right;" class="btn btn-primary btn-lg get_url"  id="actionButton" data-toggle="modal" data-target="#myModal">Actions</button>');

    function page_data(num) {
        var current_slide = page_url;
        var slide_url = current_slide.split('week')[1];
        var question_text = $('.question_text').val();

        var datas = {
            slide: slide_url,
            text: question_text
        };

        datas = JSON.stringify(datas);

        $.ajax({
            url: '/action/' + num,
            type: 'POST',
            dataType: 'json',
            data: datas
        });
    }

    $('.help').on('click', function() {
        $(this).addClass("help_active");
        setTimeout(function () {
            $(".help").removeClass("help_active");
        }, 3000);

        page_data(1);
    });

    $('.done').on('click', function() {
        $(this).addClass("done_active");
        setTimeout(function(){$(".done").removeClass("done_active");}, 3000);

        page_data(2);

    });

    $('.question_submit').on('click', function() {
        var question_text = $('.question_text').val();
        $('.question_text').val("");

        page_data(3);

    });
});
