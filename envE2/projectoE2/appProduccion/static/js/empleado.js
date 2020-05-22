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
        <table>
            <thead>
                <tr>
                    <td>Nombre</td>
                    <td>DNI</td>
                </tr>
            </thead>
            <tbody>`;

    for (let dato of json){
        tabla += crearFila(dato.nombre, dato.dni);
    }
    tabla += `</tbody></table>`;
    return tabla;
}

function crearFila(nombre, dni){
    return `
        <tr>
            <td>${nombre}</td>
            <td>${dni}</td>
        </tr>`;
}

function introducirTabla(json){
    let tabla = crearTabla(json);
    document.getElementById('cont').innerHTML = tabla;
}
