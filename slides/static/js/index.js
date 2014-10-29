$(document).ready(function() {
    $('h2').append('<button style="float: right;" class="btn btn-primary btn-lg get_url"  id="actionButton" data-toggle="modal" data-target="#myModal">Actions</button>');
    $('#help-button-img-done').hide();
    $('#done-button-img-done').hide();

    $('#actionButton').click(function() {
        url = page_url;
        console.log(url);
        var test = $('#actionButton').text();
        console.log(test);
    });

    var idCounter = 1;
    $("h2").each(function() {
        $(this).attr('id', idCounter);
        idCounter++;
    });

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
            url: '/action/' + num,
            type: 'POST',
            dataType: 'json',
            data: datas
        });
    }

    $('.help').on('click', function() {
        $(this).addClass("help_active");
        $('#help-button-img').hide();
        $('#help-button-img-done').show();

        setTimeout(function () {
            $('#help-button-img-done').hide();
            $('#help-button-img').show();
            $(".help").removeClass("help_active");}, 3000);


        page_data(1);
    });

    $('.done').on('click', function() {
        $(this).addClass("done_active");
        $('#done-button-img').hide();
        $('#done-button-img-done').show();

        setTimeout(function(){
            $('#done-button-img-done').hide();
            $('#done-button-img').show();
            $(".done").removeClass("done_active");}, 3000);

        page_data(2);

    });

    $('.question_submit').on('click', function() {
        var question_text = $('.question_text').val();

        page_data(3);

        $('.question_text').val("Question submitted!");
        setTimeout(function(){ jQuery(".question_text").val("");}, 1500);
    });
});



