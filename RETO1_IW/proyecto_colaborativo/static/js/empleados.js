let h3 = document.getElementById('prueba1');
h3.addEventListener('click', traer1)
const SERVICE_URL="https://got-quotes.herokuapp.com/quotes";
const empleadoid="/proyecto_colaborativo/empleadojson/5/"
const listaempleados="/proyecto_colaborativo/empleadojson/"



function traer1(empleado){
    fetch(listaempleados)
        .then((response) => response.json() )
        .then((empleado) => {
           let empleado1= crearempleado(empleado)
           document.getElementById('prueba1').innerHTML = empleado1;

        })
}
function crearTarea( nombre, email){
    return `
        <tr>

            <td>${nombre}>></td>
            <td>${email}</td>
        </tr>`;
}
function crearempleado(empleado) {



    let tabla = `
        <table>
            <thead>
                <tr>

                    <td>nombre</td>
                    <td>email</td>
                </tr>
            </thead>
            <tbody>
    `;


    for(let valor of empleado) {

        tabla += crearTarea( valor.nombre, valor.email);
    }
    tabla += '</tbody></table>'
    return tabla;
}
document.getElementById('insertar').addEventListener('click', insertar);

const tareas=[]

function insertar(){
 event.preventDefault();
 fetch(listaempleados)
        .then((response) => response.json() )
        .then((empleado) => {



    let formulario = document.getElementById('uno');

    let nuevaTarea = {
        nombre: formulario.children["nombre"].value,
        apellido: formulario.children["apellido"].value,
        dni: formulario.children["dni"].value,
        telofono: formulario.children["telefono"].value,
        email: formulario.children["email"].value
    }

    empleado.push(nuevaTarea);
    fetch(listaempleados,{
    method: 'POST',
     headers : {
    'Content-Type' : 'application/json'
     },
      body : JSON.stringify({
        nuevaTarea
      })
     })
     .then(response => response.json())
     .then(json => console.log(json))



    listaempleados2=crearempleado(empleado);
    document.getElementById('aki').innerHTML = listaempleados2;

        })


}







