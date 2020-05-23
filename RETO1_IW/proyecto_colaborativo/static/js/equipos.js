let h3 = document.getElementById('prueba2');
h3.addEventListener('click', traer1)
const SERVICE_URL="https://got-quotes.herokuapp.com/quotes";
const equipoid="/proyecto_colaborativo/equipojson/5/"
const listaequipos="/proyecto_colaborativo/equipojson/"



function traer1(equipo){
    fetch(listaequipos)
        .then((response) => response.json() )
        .then((equipo) => {
           let equipo1= crearequipo(equipo)
           document.getElementById('prueba2').innerHTML = equipo1;

        })
}
function crearTarea(modelo, nserie){
    return `
        <tr>
            <td>${modelo}>></td>
            <td>${nserie}</td>
        </tr>`;
}
function crearequipo(equipo) {

    let tabla = `
        <table>
            <thead>
                <tr>

                    <td>modelo</td>
                    <td>nserie</td>
                </tr>
            </thead>
            <tbody>
    `;


    for(let valor of equipo) {

        tabla += crearTarea( valor.modelo, valor.nserie);
    }
    tabla += '</tbody></table>'
    return tabla;
}
document.getElementById('insertar').addEventListener('click', insertar);

function insertar(){
 event.preventDefault();
 fetch(listaequipos)
        .then((response) => response.json() )
        .then((equipo) => {


    let formulario = document.getElementById('uno');

    let nuevaTarea = {
        modelo: formulario.children["modelo"].value,
        numeroserie: formulario.children["numeroserie"].value,
        marca: formulario.children["marca"].value,
        tipo: formulario.children["tipo"].value
        fecha adquisicion: formulario.children["fecha adquisicion"].value,
        fecha puesta en marcha: formulario.children["fecha puesta en marcha"].value,
        proveedor: formulario.children["proveedor"].value,
        planta: formulario.children["planta"].value
    }

    equipo.push(nuevaTarea);



    listaequipos2=crearequipo(equipo);
    console.log(listaequipos2)
    document.getElementById('aki').innerHTML = listaequipos2;

        })


}
