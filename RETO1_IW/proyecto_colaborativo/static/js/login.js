function login(){
            var usuario = document.getElementById("usuario").value;
            var password = document.getElementById("pass").value;

            if (usuario == "usuario" && password == "contraseña"){
                alert("Usuario y contraseña correctos")

            }
            else{
                alert("Ingrese un nombre de usuario y contrseña correctos");
            }
}
