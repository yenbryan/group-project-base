$(document).ready(function(){
    var name = $('#change_name_text').val();
    var email = $('#change_email_text').val();
    var password = $('#change_password_text').val();
    var confirm_password = $('#change_password_repeat').val();

    function change_name_save() {
        var new_name = $('#change_name_text').val();
        $.ajax ({
            url: "/edit/name/",
            type: "POST",
            dataType: 'json',
            data: JSON.stringify(new_name),
            success: function(data){
                setTimeout("$('.name_note').hide();", 3000);
                if (data === "success"){
                    $('#change_name_save').show();
                } else {
                    $('#change_name_fail').show();
                }
            }
        })
    }


    function change_email_save() {
        var new_email = $('#change_email_text').val();
        $.ajax ({
            url: "/edit/email/",
            type: "POST",
            dataType: 'json',
            data: JSON.stringify(new_email),
            success: function(data){
                setTimeout("$('.email_note').hide();", 3000);
                if (data === "success"){
                    $('#change_email_save').show();
                } else {
                    $('#change_email_fail').show();
                }
            }
        })
    }


    function change_password_save() {
        var new_password = $('#change_password_text').val();
        var new_confirm_password = $('#change_password_repeat').val();
        $.ajax ({
            url: "/edit/password/",
            type: "POST",
            dataType: 'json',
            data: JSON.stringify([new_password, new_confirm_password]),
            success: function(data){
                setTimeout("$('.password_note').hide();", 3000);
                if (data === "success"){
                    $('#change_password_save').show();
                } else if (data === "mismatch") {
                    $('#change_password_norepeat').show();
                } else {
                    $('#change_password_fail').show();
                }
            }
        })
    }


    function change_password_action(new_password, new_confirm_password) {
        console.log("change password action");
        change_password_save();
        password = new_password;
        confirm_password = new_confirm_password;
    }


    $('.profile_photo_change').on('click', function(){
        $('#id_image').trigger('click').on('change', function(){
            $('#id_image').parents('form').trigger("submit");
        });
        return false;
    });


//    function debounce(func, wait, immediate) {
//        var timeout;
//        return function() {
//            var context = this, args = arguments;
//            var later = function() {
//                timeout = null;
//                if (!immediate) func.apply(context, args);
//            };
//            var callNow = immediate && !timeout;
//            clearTimeout(timeout);
//            timeout = setTimeout(later, wait);
//            if (callNow) func.apply(context, args);
//        };
//    }
//
//    var myEfficientFn = debounce(function() {
//        change_name_save();
//    }, 250);
//    window.addEventListener('#change_name_text', myEfficientFn);

    setInterval(function(){
        var new_name = $('#change_name_text').val();
        var new_email = $('#change_email_text').val();
        var new_password = $('#change_password_text').val();
        var new_confirm_password = $('#change_password_repeat').val();
        if (new_name !== name) {
            console.log("change name action");
            change_name_save();
            name = new_name;
        }

        if (new_email !== email) {
            console.log("change email action");
            change_email_save();
            email = new_email;
        }

        if (new_password !== password || new_confirm_password !== confirm_password) {
            change_password_action(new_password, new_confirm_password)
        }
    }, 5000);

//    debounce function
//    show password digits
//    change photo do not redirect
});
