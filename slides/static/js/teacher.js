$(document).ready(function() {

    function page_data(num) {
        var current_slide = page_url;
        var slide_url = current_slide.split('week')[1];
        console.log(slide_url);
        var question_text = $('.question_text').val();

        var datas = {
            slide: slide_url,
            text: question_text
        };

        datas = JSON.stringify(datas);

        $.ajax({
            url: '/teacher_action/' + num,
            type: 'POST',
            dataType: 'json',
            data: datas
        });
    }

    $('.help-button').on('click', function() {


        $(this).addClass("help_active");
        setTimeout(function () {
            $(".help").removeClass("help_active");
        }, 3000);

        page_data(1);


    });
});
