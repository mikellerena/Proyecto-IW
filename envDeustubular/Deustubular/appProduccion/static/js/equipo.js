const URL = "http://127.0.0.1:8000/appProduccion/produccion/equipos/api/";

let ver = document.getElementById('ver');
ver.addEventListener('click', event => {
    event.preventDefault();
    loadData();
})

function loadData(){
    console.log(URL);
    fetch(URL)
        .then((response) => response.json())
        .then((json) => {
            introducirTabla(json);
        });
}

function crearTabla(json){
    let tabla = `
        <table id="table-js">
            <thead>
                <tr>
                    <td>ID</td>
                    <td class="td_estilos">Marca</td>
                    <td class="td_estilos">Modelo</td>
                    <td class="td_estilos">Enlaces</td>
                </tr>
            </thead>
            <tbody>`;

    for (let dato of json){
        tabla += crearFila(dato.id, dato.marca, dato.modelo);
    }
    tabla += `</tbody></table>`;
    return tabla;
}

function crearFila(id, marca, modelo){
    return `
        <tr>
            <td>${id}</td>
            <td class="td_estilos">${marca}</td>
            <td class="td_estilos">${modelo}</td>
            <td class="td_estilos">
                <div class="mar-inferior">
                    <a href="http://127.0.0.1:8000/appProduccion/produccion/equipos/${id}/">Ver</a> ||
                    <a href="http://127.0.0.1:8000/appProduccion/produccion/equipos/${id}/update/">Editar</a> ||
                    <a href="http://127.0.0.1:8000/appProduccion/produccion/equipos/${id}/delete/">Borrar</a>
                </div>
            </td>
        </tr>`;
}

function introducirTabla(json){
    let tabla = crearTabla(json);
    document.getElementById('cont').innerHTML = tabla;
}
