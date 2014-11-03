// Need to use proper syntax for javascript
// camelCase!
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
            data: datas,
            success: function(){
            }
        });
    }


    $('.help-button').on('click', function() {
        var action_id = $(this).attr("id");
        $.ajax({
            url: '/help_done/',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify(action_id)
        });
        var NumOfNeedHelp = $('.header.help').text().split(' Need Help')[0];
        NumOfNeedHelp--;
        if (NumOfNeedHelp === 1) {
            $('.header.help').text('1 Needs Help');
        } else if (NumOfNeedHelp > 1) {
            $('.header.help').text(NumOfNeedHelp+' Need Help');
        } else {
            $('.header.help').text('0 Need Help');
        }
        $(this).removeClass('help-button').addClass('help-button-active');
        active_div = $(this).parent().parent();
        $(this).parent().parent().parent().append(active_div);
        $(this).children().html("Helped!")
    });


    $('.question-button').on('click', function() {
        var question_id = $(this).attr("id");
        console.log(question_id);
        $.ajax({
            url: '/question_done/',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify(question_id)
        });
        var NumOfQuestion = $('.header.question').text().split(' Total Question')[0];
        NumOfQuestion--;
        if (NumOfQuestion === 1) {
            $('.header.question').text('1 Question');
        } else if (NumOfQuestion > 1) {
            $('.header.question').text(NumOfQuestion + ' Total Questions');
        } else {
            $('.header.question').text('0 Total Questions');
        }

        $(this).removeClass('question-button').addClass('question-button-active');
        active_div = $(this).parent().parent();
        $(this).parent().parent().parent().append(active_div);
        $(this).children().html("Answered!")
    });


});
