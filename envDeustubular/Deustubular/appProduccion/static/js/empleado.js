const URL = "http://127.0.0.1:8000/appProduccion/empleados/api/";

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
//        <table id="table-js">
//            <thead>
//                <tr>
//                    <td>ID</td>
//                    <td class="td_estilos">Nombre</td>
//                    <td class="td_estilos">DNI</td>
//                    <td class="td_estilos">Enlaces</td>
//                </tr>
//            </thead>
//            <tbody>`;
//
//    for (let dato of json){
//        tabla += crearFila(dato.id, dato.nombre, dato.dni);
//    }
//    tabla += `</tbody></table>`;
//    return tabla;
//}
//
//function crearFila(id, nombre, dni){
//    return `
//        <tr>
//            <td>${id}</td>
//            <td class="td_estilos">${nombre}</td>
//            <td class="td_estilos">${dni}</td>
//            <td class="td_estilos">
//                <div class="mar-inferior">
//                    <a href="http://127.0.0.1:8000/appProduccion/produccion/empleados/${id}/">Ver</a> ||
//                    <a href="http://127.0.0.1:8000/appProduccion/produccion/empleados/${id}/update/">Editar</a> ||
//                    <a href="http://127.0.0.1:8000/appProduccion/produccion/empleados/${id}/delete/">Borrar</a>
//                </div>
//            </td>
//        </tr>`;
//}
//
//function introducirTabla(json){
//    let tabla = crearTabla(json);
//    document.getElementById('cont').innerHTML = tabla;
//}


/*Busqueda por nombre de empleado*/


let busq = document.getElementById('busq');
busq.addEventListener('click', event => {
    event.preventDefault();
    let fil = document.getElementById('fil');
    console.log(fil.value);
    loadData(fil.value);
})

function loadData(fil){
    let url = URL + "?nombre=" + fil;
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
        lista += crearEmpleado(dato.id, dato.nombre, dato.dni);
    }
    lista += `</ul>`;
    return lista;
}

function crearEmpleado(id, nombre, dni){
    return `
        <li>
            <p class="mar-inferior p-lista">Empleado</p>
            <div class="mar-inferior">
                <a href="http://127.0.0.1:8000/appProduccion/empleados/${id}/">Ver</a> ||
                <a href="http://127.0.0.1:8000/appProduccion/empleados/${id}/update/">Editar</a> ||
                <a href="http://127.0.0.1:8000/appProduccion/empleados/${id}/delete/">Borrar</a>
            </div>
            <ul class="listas">
                <li>ID: ${id}</li><br>
                <li>Nombre: ${nombre}</li><br>
                <li>DNI: ${dni}</li>
            </ul>
            <br>
        </li>`;
}

function introducirLista(json){
    let lista = crearLista(json);
    document.getElementById('cont').innerHTML = lista;
}
