

function crearlista(objeto){
    let lista='<ul>'
    for(const key in objeto){
        console.log(key)
        lista+=crearelemento(key,objeto[key])

    }
    lista+='</ul>'
    return lista;



}
function crearelemento(label,valor){
    return `<li>${label} : ${valor}</li>`;
}



let listaHTML=crearlista(estudiante)
document.getElementById('lista').insertAdjacentHTML('afterbegin',listaHTML)
