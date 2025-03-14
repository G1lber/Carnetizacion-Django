// Obtén los elementos del DOM
const modal = document.getElementById("modal");
const createButton = document.getElementById("createButton");
const createPersonal = document.getElementById("createPersonal");
const closeButton = document.getElementById("closeButton");

if (createButton) {
    createButton.onclick = function(event) {
        event.preventDefault();  // Previene que el formulario se envíe y la página se recargue
        console.log('Modal abierto');
        modal.classList.add("show");
    };
}

if (createPersonal) {
    createPersonal.onclick = function(event) {
        event.preventDefault();  // Previene que el formulario se envíe y la página se recargue
        console.log('Modal abierto');
        modal.classList.add("show");
    };
}

// Cerrar modal cuando se haga clic en el botón de cerrar
if (closeButton) {
    closeButton.onclick = function() {
        console.log('Modal cerrado');
        modal.classList.remove("show");
    };
}

// Cerrar modal cuando se haga clic fuera de él
window.onclick = function(event) {
    if (event.target === modal) {
        console.log('Modal cerrado desde el fondo');
        modal.classList.remove("show");
    }
};
