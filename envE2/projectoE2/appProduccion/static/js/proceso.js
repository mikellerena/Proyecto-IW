const URL = "http://127.0.0.1:8000/appProduccion/produccion/procesos/api/";

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
        <table>
            <thead>
                <tr>
                    <td>ID</td>
                    <td class="td_estilos">Codigo Orden<br>Frabricación</td>
                    <td class="td_estilos">Codigo Proceso</td>
                    <td class="td_estilos">Referencia</td>
                    <td class="td_estilos">Nombre</td>
                </tr>
            </thead>
            <tbody>`;

    for (let dato of json){
        tabla += crearFila(dato.id, dato.codigo_orden_fabricacion, dato.codigo_proceso, dato.referencia, dato.nombre_proceso);
    }
    tabla += `</tbody></table>`;
    return tabla;
}

function crearFila(id, codigo_orden_fabricacion, codigo_proceso, referencia, nombre_proceso){
    return `
        <tr>
            <td>${id}</td>
            <td class="td_estilos">${codigo_orden_fabricacion}</td>
            <td class="td_estilos">${codigo_proceso}</td>
            <td class="td_estilos">${referencia}</td>
            <td class="td_estilos">${nombre_proceso}</td>
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
