$function(){
    'use strict';
    $('#id_nov_form').on('submit', function(event){
        var post_url = $("#id_nov_form").data("post-url");

        var formData = new FormData(this);

        $.ajax({
            url: post_url,
            type: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success:function(response){
                var message = response.content.message;
                alert(message);
            },
        });

        event.preventDefault();
    });
}
