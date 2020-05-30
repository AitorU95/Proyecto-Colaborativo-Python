
const tareas="/proyecto_colaborativo/descripcionjson/"


let mostrar = document.getElementById('mostrar');
mostrar.addEventListener('click', TraerTareas)

function TraerTareas(){
 fetch(tareas)
        .then((response) => response.json() )
        .then((tareas) => {
           let Tarea= CrearTablaTareas(tareas)
           document.getElementById('tarea1').innerHTML = Tarea;

        })

}
function CrearTablaTareas(tareas) {



    let tabla = `
        <table>
            <thead>
                <tr>

                    <td>texto</td>

                </tr>
            </thead>
            <tbody>
    `;


    for(let valor of tareas) {

        tabla += CrearTarea( valor.texto);
    }
    tabla += '</tbody></table>'
    return tabla;
}
function CrearTarea( texto){

    return `
        <tr>

            <td>${texto}</td>

        </tr>`;
}

