$(document).ready(function(){
    $('#change_name_edit').on('click', function() {
        $('#change_name, #change_name_text, #change_name_save').toggle();
    });

    $('#change_email_edit').on('click', function() {
        $('#change_email, #change_email_text, #change_email_save').toggle();
    });

    $('#change_name_save').on('click', function() {
        var new_name = $('#change_name_text').val();
        $.ajax ({
            url: "/edit/name/",
            type: "POST",
            dataType: 'json',
            data: JSON.stringify(new_name),
            success: function(data){
                if (data === "success"){
                    $('#change_name, #change_name_text, #change_name_save').toggle();
                    $('#change_name').html(new_name);
                    $('#change_name_save').after("<td id='change_name_note' style='color:lightgreen;'><b>Name validated!</b></td>");
                    setTimeout("$('#change_name_note').hide();", 3000);
                    $('#change_name_text').val("");
                } else {
                    $('#change_name_save').after("<td id='change_name_note' style='color:red;'><b>Name cannot be empty!</b></td>");
                    setTimeout("$('#change_name_note').hide();", 3000);
                    $('#change_name_text').val("");
                }
            }
        });
    });

    $('#change_email_save').on('click', function() {
        var new_email = $('#change_email_text').val();
        $.ajax ({
            url: "/edit/email/",
            type: "POST",
            dataType: 'json',
            data: JSON.stringify(new_email),
            success: function(data){
                if (data === "success"){
                    $('#change_email, #change_email_text, #change_email_save').toggle();
                    $('#change_email').html(new_email);
                    $('#change_email_save').after("<td id='change_email_note' style='color:green;'><b>Email validated!</b></td>");
                    setTimeout("$('#change_email_note').hide();", 3000);
                    $('#change_email_text').val("");
                } else {
                    $('#change_email_save').after("<td id='change_email_note' style='color:red;'><b>Incorrect email form!</b></td>");
                    setTimeout("$('#change_email_note').hide();", 3000);
                    $('#change_email_text').val("");
                }
            }
        });
    })


});
