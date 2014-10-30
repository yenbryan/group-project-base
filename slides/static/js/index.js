$(document).ready(function() {
    $('h2').prepend('<button class="btn btn-lg get_url"  id="actionButton" data-toggle="modal" data-target="#myModal">Actions</button>');

    $('.help').on('click', function() {
        console.log('help');
        console.log(page_title);
        console.log(page_url);
        $(this).addClass("help_active");
        setTimeout(function () {
            $(".help").removeClass("help_active");
        }, 3000);

        var student_real_name = $('#userName').text();
        console.log(student_real_name);
        var current_slide = $('#myModalLabel').text();
        console.log(current_slide);

        var datas = {
            student: student_real_name,
            slide: current_slide
        };
        datas = JSON.stringify(datas);
        console.log(datas);

        $.ajax({
            url: '/help/',
            type: 'POST',
            dataType: 'json',
            data: datas,
            success: function (response) {
                console.log(response);
            }
        });
    });

    $('.done').on('click', function() {
        console.log('done');
        console.log(page_title);
        console.log(page_url);
        $(this).addClass("done_active");
        setTimeout(function(){$(".done").removeClass("done_active");}, 3000);
    });

    $('.question_submit').on('click', function() {
        console.log('question');
        console.log(page_title);
        console.log(page_url);
        console.log($('.question_text').val());
        $('.question_text').val("");
    });
});
