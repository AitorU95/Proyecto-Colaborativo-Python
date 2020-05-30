function addBorrarEventListeners(){
    let enlacesBorrar = document.getElementsByClassName('borrar-tarea'); // Todos los elementos <a>
    for(enlace of enlacesBorrar) {
        // Añadir listener:
        enlace.addEventListener('click', function(event){
            event.preventDefault(); // Detener la acción por defecto de navegar
            // Mediante el objeto dataset podemos acceder a cualquier atributo de tipo "data-"
            let id = event.currentTarget.dataset.id; // Accedemos al atributo "data-id"
            borrarTareaById(id, tareas);
            crearTablaTareas(tareas);
        });
    }
}

/**
 * Borra de un array de objetos el objeto con el ID indicado.
 */
function borrarTareaById(id, tareas){
    for(let i = 0; i < tareas.length; i++) {
        if(tareas[i].id == id) {
            tareas.splice(i, 1);
            break;
        }
    }
}
