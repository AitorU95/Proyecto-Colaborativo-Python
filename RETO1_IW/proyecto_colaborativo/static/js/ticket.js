let h3 = document.getElementById('prueba3');
h3.addEventListener('click', traer1)
const SERVICE_URL="https://got-quotes.herokuapp.com/quotes";
const ticketid="/proyecto_colaborativo/ticket/5/"
const listatickets="/proyecto_colaborativo/ticketjson/"



function traer1(ticket){
    fetch(listatickets)
        .then((response) => response.json() )
        .then((ticket) => {
        console.log(ticket)
           let ticket1= crearticket(ticket)
           document.getElementById('prueba3').innerHTML = ticket1;

        })
}
function crearTarea(numeroref, titulo){
    return `
        <tr>
            <td>${numeroref}>></td>
            <td>${titulo}</td>
        </tr>`;
}
function crearticket(ticket) {

    let tabla = `
        <table>
            <thead>
                <tr>

                    <td>numeroref</td>
                    <td>titulo</td>
                </tr>
            </thead>
            <tbody>
    `;


    for(let valor of ticket) {

        tabla += crearTarea( valor.numeroref, valor.titulo);
    }
    tabla += '</tbody></table>'
    return tabla;
}
document.getElementById('insertar').addEventListener('click', insertar);

function insertar(){
 event.preventDefault();
 fetch(listatickets)
        .then((response) => response.json() )
        .then((ticket) => {


    let formulario = document.getElementById('uno');

    let nuevaTarea = {
        numeroref: formulario.children["numeroref"].value,
        titulo: formulario.children["titulo"].value,
        descripcion: formulario.children["descripcion"].value,
        fechaapertura: formulario.children["fecha apertura"].value,
        fecharesolucion:formulario.children["fecha resolucion"].value,
        urgencia:formulario.children["urgencia"].value,
        tipo: formulario.children["tipo"].value,
        estado: formulario.children["estado"].value,
        empleado: formulario.children["empleado"].value,
        comentarios: formulario.children["comentarios"].value
    }

    equipo.push(nuevaTarea);



    listatickets2=crearticket(ticket);
    console.log(listatickets2)
    document.getElementById('aki').innerHTML = listatickets2;

        })


}
