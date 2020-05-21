    'use strict';
    $('#id_nov_form').on('submit', function(event){
        event.preventDefault();
        var post_url = $("#id_nov_form").data("post-url");
        var usu = $("[name=usuario]").val();
        console.log(usu);
        var gen = $("[name=genero]").val();
        console.log(gen);
        var mail = $("[name=email]").val();
        var formData = new FormData();
        console.log(mail);
        $.ajax({
            url: post_url,
            method: "POST",
            data: $("#id_nov_form").serialize(),
            success: function(response){
                alert(response);
            },
            error: function (error) {
                    alert("Error en el servidor comprueba tu conexion y vuelve a intentarlo");
                    console.log(error);
            }

        });
    });
