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

const URL = "http://127.0.0.1:8000/appProduccion/produccion/equipos/api/";

let ver = document.getElementById('ver');
ver.addEventListener('click', event => {
    loadData();
})

function loadData(){
    console.log(url);
    fetch(URL)
        .then((response) => response.json())
        .then((json) => {
            introducirTabla(json);
        });
}

function crearTabla(json){
    let tabla = `
        <table>
            <thead>
                <tr>
                    <td>ID</td>
                    <td>Marca</td>
                    <td>Modelo</td>
                </tr>
            </thead>
            <tbody>`;

    for (dato of json){
        tabla += crearFila(dato.id, dato.marca, dato.modelo);
    }
    tabla += `</tbody></table>`;
    return tabla;
}

function crearFila(id, marca, modelo){
    return `
        <tr>
            <td>${id}</td>
            <td>${marca}</td>
            <td>${modelo}</td>
        </tr>`;
}

function introducirTabla(json){
    let tabla = crearTabla(json);
    document.getElementById('cont').innerHTML = tabla;
}
