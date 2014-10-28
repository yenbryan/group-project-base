$(document).ready(function() {
    $('h2').append('<button style="float: right;" class="btn btn-primary btn-lg get_url"  id="actionButton" data-toggle="modal" data-target="#myModal">Actions</button>');

    $('.help').on('click', function() {
        $(this).addClass("help_active");
        setTimeout(function () {
            $(".help").removeClass("help_active");
        }, 3000);

        var current_slide = page_url;
        var slide_url = current_slide.split('http://127.0.0.1:8000/')[1];

        var datas = {
            slide: slide_url
        };
        datas = JSON.stringify(datas);

        $.ajax({
            url: '/help/',
            type: 'POST',
            dataType: 'json',
            data: datas
        });
    });

    $('.done').on('click', function() {
        console.log('done');
        console.log(page_title);
        console.log(page_url);
        $(this).addClass("done_active");
        setTimeout(function(){$(".done").removeClass("done_active");}, 3000);

        var current_slide = page_url;
        var slide_url = current_slide.split('http://127.0.0.1:8000/')[1];

        var slide_datas = {
            slide: slide_url
        };

        slide_datas = JSON.stringify(slide_datas);
        console.log(slide_datas);

        $.ajax({
            url: '/done/',
            type: 'POST',
            dataType: 'json',
            data: slide_datas
        });
    });

    $('.question_submit').on('click', function() {
        var question_text = $('.question_text').val();
        console.log(question_text);

        var current_slide = page_url;
        var slide_url = current_slide.split('http://127.0.0.1:8000/')[1];

        var slide_datas = {
            slide: slide_url,
            text: question_text
        };

        slide_datas = JSON.stringify(slide_datas);
        console.log(slide_datas);

        $.ajax({
            url: '/question/',
            type: 'POST',
            dataType: 'json',
            data: slide_datas
        });
    });
});
