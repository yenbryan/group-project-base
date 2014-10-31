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


    function teacher_toggle(num) {
        var current_slide = window.location.href;
        var slide_url = current_slide.split('week')[1];
        console.log(slide_url);
        console.log();
        var question_text = $('.question_text').val();

        var datas = {
            week: week,
            day: day2,
            am_pm: am_pm,
            slide_number: h2SlideNumber,
            text: question_text
        };
        datas = JSON.stringify(datas);
        console.log(datas);

        $.ajax({
            url: '/help_done/' + num,
            type: 'POST',
            dataType: 'json',
            data: datas
        });
    }


    $('.help-button').on('click', function() {
        teacher_toggle(1);

    });
});
