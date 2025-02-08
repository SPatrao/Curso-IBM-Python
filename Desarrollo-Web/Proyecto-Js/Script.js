// script.js

// Muestra un mensaje en la consola cuando se carga el script
console.log("El archivo script.js ha sido cargado correctamente.");

// Función para saludar
function saludar(nombre) {
    return "Hola, " + nombre + "!";
}

// Ejecutar la función y mostrar el resultado en consola
console.log(saludar("Estudiante"));

// Manipulación del DOM: cambiar el texto de un elemento
window.onload = function() {
    let mensajeElemento = document.getElementById("mensaje");
    if (mensajeElemento) {
        mensajeElemento.innerText = "¡Este texto ha sido modificado por script.js!";
    }
};

// Evento para el botón
let boton = document.getElementById("miBoton");
if (boton) {
    boton.addEventListener("click", function() {
        alert("¡Has hecho clic en el botón!");
    });
}

// Temporizador setTimeout
setTimeout(function() {
    console.log("Este mensaje aparece tras 3 segundos desde script.js");
}, 3000);

// Temporizador setInterval
let contador = 0;
let intervalo = setInterval(function() {
    contador++;
    console.log("Contador en script.js: " + contador);
    if (contador >= 5) {
        clearInterval(intervalo);
    }
}, 1000);