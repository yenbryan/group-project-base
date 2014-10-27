$(document).ready(function() {
    $('h2').append('<button style="float: right;" class="btn btn-primary btn-lg get_url"  id="actionButton" data-toggle="modal" data-target="#myModal">Actions</button>');

    $('.help').on('click', function() {
        console.log('help');
        console.log(page_title);
        console.log(page_url);
        $(this).addClass("help_active");
        setTimeout(function(){$(".help").removeClass("help_active");}, 3000);
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
