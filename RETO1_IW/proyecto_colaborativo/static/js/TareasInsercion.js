
const tareas="/proyecto_colaborativo/descripcionjson/"

// funcion para insertar las tareas a bbdd
function InsertarTareas(){



   const data = new FormData(document.getElementById('uno'));

    fetch(tareas, {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .then((data) => {
        alert("Tarea enviada correctamente")
    })

}

