

    function saludar(event){
        event.preventDefault();
        if(event.type == 'click') {

        }
        else if(event.type == 'mouseover') {
          let subtitulo=document.getElementById('subtitulo')
          subtitulo.style.backgroundColor="blue"

        }
        else {
            console.log("Otro evento!");
        }
    }
    function eliminar1(event){
    eliminar.remove();
    alert("has eliminado un ticket")
    }
    function volveratras(event){
    alert("desea volver?")
    }

    function parrafo1(event){
     let parrafo=document.getElementById('parrafo')
     parrafo.remove();

    }
    let h2 = document.getElementById('subtitulo');
    h2.addEventListener('mouseover', saludar);



    let p=document.getElementById('parrafo');
    p.addEventListener('mouseover', parrafo1);

    let eliminar=document.getElementsByClassName('fas fa-trash-alt');
    eliminar.addEventListener('click', eliminar1);

    let tickets=document.getElementById('ticket');







