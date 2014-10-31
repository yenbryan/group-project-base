$(document).ready(function() {
    var allPanels = $('.accordion > dd').hide();
    $('.open').hide();
    $('.open-arrow-icon').hide();

    $('.accordion > dt').click(function() {
        $(this).children().children('.open-arrow-icon').toggle();
        $(this).children().children('.closed-arrow').toggle();

        $(this).children('.open').toggle();
        $(this).children('.divider-hr-main').toggle();

        var alreadyOpen = $(this).next().css('display') === 'block';
        if (!alreadyOpen) {
            $(this).next().slideDown();
        }
        else {
            $(this).next().slideUp();
        }
    });

});

