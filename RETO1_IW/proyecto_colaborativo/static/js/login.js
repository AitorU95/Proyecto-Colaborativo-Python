var intento = 3 //Variable para contar el numero de intentos
//Función para ejecutar el login en el botón
function validar(){
    var username = document.getElementById("username").value; //Obtenemos el valor del username
    var password = document.getElementById("password").value; //Obtenemos el valor de la password
    //Comprobamos si es el correcto
    if (username == "usuario" && password == "contraseña"){
        alert("Login correcto");
        window.location = 'http://127.0.0.1:8000/proyecto_colaborativo/'; //Redirigimos a otra pagina
    }
    else if(username == "usuario1" && password == "contraseña1"){
        alert("Login correcto");
        window.location = 'http://127.0.0.1:8000/proyecto_colaborativo/'; //Redirigimos a otra pagina
    }
    else if(username == "usuario2" && password == "contraseña2"){
        alert("Login correcto");
        window.location = 'http://127.0.0.1:8000/proyecto_colaborativo/'; //Redirigimos a otra pagina
    }
    else{
        intento --; //Decrementamos el intento
        if(intento > 1){
            alert("Login incorrecto. Te quedan " +intento+ " intentos");
            document.getElementById("username").value = "";
            document.getElementById("password").value = "";
        }
        else if(intento == 1){
            alert("Login incorrecto. Te queda " +intento+ " intento");
            document.getElementById("username").value = "";
            document.getElementById("password").value = "";
        }
        //Deshabilitamos los campos despues de 3 intentos
        else if (intento == 0){
            alert("Login incorrecto. No te quedan más intentos");
            document.getElementById("username").value = "";
            document.getElementById("password").value = "";
            document.getElementById("username").disabled = true;
            document.getElementById("password").disabled = true;
            document.getElementById("submit").disabled = true;
        }


    }
}

