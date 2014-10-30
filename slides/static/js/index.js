$(document).ready(function() {
    $('#help-button-img-done').hide();
    $('#done-button-img-done').hide();
    var h2SlideNumber = 0;
    var page_title;
    var page_url;

    $(document).on('click', '.get_url', function() {
        page_title = $(this).parent().parent().clone().children().remove().end().text()
        $('.modal-title').html(page_title);
        page_url = window.location.href;
    });

    $('h2').append('<div class="buttonSelector"><button style="float: right;" class="btn btn-primary btn-lg get_url"  id="actionButton" data-toggle="modal" data-target="#myModal">Actions</button></div>');

    $('#actionButton').click(function() {
        url = page_url;
        var test = $('#actionButton').text();
        console.log(test);
    });

    var idCounter = 1;
    $("h2").each(function() {
        $(this).attr('id', idCounter);
        idCounter++;
    });

    var divCounter = 1;
    $(".buttonSelector").each(function() {
        $(this).attr('id', divCounter);
        divCounter++;
    });

    $(".buttonSelector").on('click', function() {
        var parent = $(this).parent()
        h2SlideNumber = (parent.attr('id'))

    });

    function page_data(num) {
        var current_slide = page_url;
        var slide_url = current_slide.split('week')[1];
        var week = slide_url[0];
        var day2 = slide_url.split('/')[1];
        console.log("day2:    "+day2);

        var day = slide_url[2];
        console.log(slide_url);
        var am_pm = slide_url.substring(3,6);
        console.log("week" + week);
        console.log("day" + day);
        console.log("number" + h2SlideNumber);
        if (am_pm == "_am") {
            am_pm = 0;
            console.log("AM_PM:  "+am_pm)
        }
        else if (am_pm == "_pm") {
            am_pm = 1;
            console.log("AM_PM:  "+am_pm)
        }
        else {
            am_pm = 2;
        }

        console.log(current_slide);
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
//    $('.buttonSelector').css("margin-top", "-5%");
    $('.buttonSelector').css("postion", "absolute");
//    $('.buttonSelector').css("margin-bottom", "5%");
    $('.buttonSelector').css("display", "inline-block");
    $('.buttonSelector').css("float", "right");





//    $('.buttonSelector').css("position", "absolute")

});
