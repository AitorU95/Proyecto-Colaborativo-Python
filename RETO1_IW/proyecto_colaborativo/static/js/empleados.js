var contenido = document.queryselector('#contenido')

function traer(){
    fetch("/empleadojson/")
        .then(res => res.json() )
        .then(datos => {
            tabla(datos)
        })
}

function tabla(datos){
    contenido.innerHTML = ''
    for(let valor of datos){
        contenido.innerHTML += `
            <tr>
                    <th scope="row">${valor.nombre}</th>
                    <td>${valor.apellido}</td>
                    <td>${valor.dni}</td>
                    <td>${valor.telefono}</td>
                    <td>${valor.email}</td>

            </tr>
        `
    }
}
