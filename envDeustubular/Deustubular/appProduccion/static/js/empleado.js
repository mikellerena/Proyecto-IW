const URL = "http://127.0.0.1:8000/appProduccion/produccion/empleados/api/";

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
                    <td class="td_estilos">Nombre</td>
                    <td class="td_estilos">DNI</td>
                    <td class="td_estilos">Enlaces</td>
                </tr>
            </thead>
            <tbody>`;

    for (let dato of json){
        tabla += crearFila(dato.id, dato.nombre, dato.dni);
    }
    tabla += `</tbody></table>`;
    return tabla;
}

function crearFila(id, nombre, dni){
    return `
        <tr>
            <td>${id}</td>
            <td class="td_estilos">${nombre}</td>
            <td class="td_estilos">${dni}</td>
            <td class="td_estilos">
                <div class="mar-inferior">
                    <a href="http://127.0.0.1:8000/appProduccion/produccion/empleados/${id}/">Ver</a> ||
                    <a href="http://127.0.0.1:8000/appProduccion/produccion/empleados/${id}/update/">Editar</a> ||
                    <a href="http://127.0.0.1:8000/appProduccion/produccion/empleados/${id}/delete/">Borrar</a>
                </div>
            </td>
        </tr>`;
}

function introducirTabla(json){
    let tabla = crearTabla(json);
    document.getElementById('cont').innerHTML = tabla;
}
