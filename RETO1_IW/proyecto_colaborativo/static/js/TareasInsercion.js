
const tareas="/proyecto_colaborativo/descripcionjson/"




function InsertarTareas(){



   const data = new FormData(document.getElementById('uno'));

    fetch(tareas, {
        method: "POST",
        body: data
    })
    .then(response => response.json())
    .then((data) => {
        alert("se ha cargado correctamente")
    })

}

