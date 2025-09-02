setInterval(picar,1000)

function saludar(){
   // document.write("Hola desde función")
   var miH1 = document.getElementById("saludo")
   miH1.classList.add("rojo")
   miH1.innerHTML = "Hola desde función"
}

function picar(){
   var ojo = document.getElementById("ojo")
   ojo.classList.toggle("ojo-cerrado")
}

