
const tareas="/proyecto_colaborativo/descripcionjson/"


let mostrar = document.getElementById('enviar');
mostrar.addEventListener('click',InsertarTareas )

function InsertarTareas(){

   let formulario = document.getElementById('uno');
   let nuevaTarea = {
   texto:formulario.children["texto"].value}

  fetch(tareas,{
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
}

