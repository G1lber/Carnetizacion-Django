// Obtén los elementos del DOM
const modal = document.getElementById("modal");
const createButton = document.getElementById("createButton");
const closeButton = document.getElementById("closeButton");

// Mostrar modal cuando se haga clic en el botón "CREAR"
if (createButton) {
    createButton.onclick = function() {
        modal.classList.add("show");
    };
}

// Cerrar modal cuando se haga clic en el botón de cerrar
if (closeButton) {
    closeButton.onclick = function() {
        modal.classList.remove("show");
    };
}

// Cerrar modal cuando se haga clic fuera de él
window.onclick = function(event) {
    if (event.target === modal) {
        modal.classList.remove("show");
    }
};