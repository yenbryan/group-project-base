<<<<<<< HEAD
///**
// * Created by GoldenGate on 10/26/14.
// */
//$(document).ready(function() {
////    $(".slide-deck").append("<a href="+ {% url 'week1_day1' %}+">")
//});
=======
$(document).ready(function() {
    $('h2').append('<button style="float: right;" class="btn btn-primary btn-lg get_url" data-toggle="modal" data-target="#myModal">Actions</button>');

    $('.help').on('click', function() {
        console.log('help');
        console.log(page_title);
        console.log(page_url);
        $(this).addClass("help_active");
        $('#help_icon').hide();
        $('#help_icon_active').show();
    });

    $('.done').on('click', function() {
        console.log('done');
        console.log(page_title);
        console.log(page_url);
        $(this).addClass("done_active");
        $('#done_icon').hide();
        $('#done_icon_active').show();
    });

    $('.question_submit').on('click', function() {
        console.log('question');
        console.log(page_title);
        console.log(page_url);
        console.log($('.question_text').val());
        $('.question_text').val("");
    });

});
>>>>>>> d7b6dbb674a71ee0482ce7602226e4b3f2db7cf6
