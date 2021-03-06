const URL = "http://127.0.0.1:8000/appProduccion/procesos/api/";

//let ver = document.getElementById('ver');
//ver.addEventListener('click', event => {
//    event.preventDefault();
//    loadData();
//})
//
//function loadData(){
//    console.log(URL);
//    fetch(URL)
//        .then((response) => response.json())
//        .then((json) => {
//            introducirTabla(json);
//        });
//}
//
//function crearTabla(json){
//    let tabla = `
//        <div class="div-table">
//            <table id="table-js">
//                <thead>
//                    <tr>
//                        <td>ID</td>
//                        <td class="td_estilos">Codigo Orden<br>Frabricación</td>
//                        <td class="td_estilos">Codigo Proceso</td>
//                        <td class="td_estilos">Referencia</td>
//                        <td class="td_estilos">Nombre</td>
//                        <td class="td_estilos">Enlaces</td>
//                    </tr>
//                </thead>
//                <tbody>`;
//
//    for (let dato of json){
//        tabla += crearFila(dato.id, dato.codigo_orden_fabricacion, dato.codigo_proceso, dato.referencia, dato.nombre_proceso);
//    }
//    tabla += `</tbody></table></div>`;
//    return tabla;
//}
//
//function crearFila(id, codigo_orden_fabricacion, codigo_proceso, referencia, nombre_proceso){
//    return `
//        <tr>
//            <td>${id}</td>
//            <td class="td_estilos">${codigo_orden_fabricacion}</td>
//            <td class="td_estilos">${codigo_proceso}</td>
//            <td class="td_estilos">${referencia}</td>
//            <td class="td_estilos">${nombre_proceso}</td>
//            <td class="td_estilos">
//                <div class="mar-inferior">
//                    <a href="http://127.0.0.1:8000/appProduccion/produccion/procesos/${id}/">Ver</a> ||
//                    <a href="http://127.0.0.1:8000/appProduccion/produccion/procesos/${id}/update/">Editar</a> ||
//                    <a href="http://127.0.0.1:8000/appProduccion/produccion/procesos/${id}/delete/">Borrar</a>
//                </div>
//            </td>
//        </tr>`;
//}
//
//function introducirTabla(json){
//    let tabla = crearTabla(json);
//    document.getElementById('cont').innerHTML = tabla;
//}

/*Busqueda por nombre de proceso*/

let busq = document.getElementById('busq');
busq.addEventListener('click', event => {
    event.preventDefault();
    let fil = document.getElementById('fil');
    console.log(fil.value);
    loadData(fil.value);
})

function loadData(fil){
    let url = URL + "?nombre_proceso=" + fil;
    console.log(url);
    fetch(url)
        .then((response) => response.json())
        .then((json) => {
            introducirLista(json);
        });
}

function crearLista(json){
    let lista = `
        <ul class="lista">
            `;

    for (let dato of json){
        lista += crearEquipo(dato.id, dato.codigo_orden_fabricacion, dato.codigo_proceso, dato.referencia, dato.nombre_proceso);
    }
    lista += `</ul>`;
    return lista;
}

function crearEquipo(id, codigo_orden_fabricacion, codigo_proceso, referencia, nombre_proceso){
    return `
        <li>
            <p class="mar-inferior p-lista">Proceso</p>
            <div class="mar-inferior">
                <a href="http://127.0.0.1:8000/appProduccion/procesos/${id}/">Ver</a> ||
                <a href="http://127.0.0.1:8000/appProduccion/procesos/${id}/update/">Editar</a> ||
                <a href="http://127.0.0.1:8000/appProduccion/procesos/${id}/delete/">Borrar</a>
            </div>
            <ul class="listas">
                <li>ID: ${id}</li><br>
                <li>Codigo Orden Fabricación: ${codigo_orden_fabricacion}</li><br>
                <li>Codigo Proceso: ${codigo_proceso}</li><br>
                <li>Referencia: ${referencia}</li><br>
                <li>Nombre: ${nombre_proceso }</li>
            </ul>
        </li>`;
}

function introducirLista(json){
    let lista = crearLista(json);
    document.getElementById('cont').innerHTML = lista;
}

