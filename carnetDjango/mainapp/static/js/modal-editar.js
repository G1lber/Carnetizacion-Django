// Modal de edición
const editModal = document.getElementById("editModal");
const closeEditButton = document.querySelector(".close");

// Verificar si existen antes de añadir eventos
if (!editModal) {
    console.error("Error: No se encontró el modal de edición en el DOM.");
}
if (!closeEditButton) {
    console.error("Error: No se encontró el botón de cerrar en el DOM.");
}
document.querySelectorAll(".btn-edit").forEach(button => {
    button.addEventListener("click", function () {
        let fichaId = this.getAttribute("data-id");

        console.log(`Abriendo modal de edición para ficha ID: ${fichaId}`);

        // Hacer una solicitud AJAX para obtener los datos de la ficha
        fetch(`/obtener-ficha/${fichaId}/`)
            .then(response => response.json())
            .then(data => {
                document.getElementById("fichaId").value = data.id;
                document.getElementById("fechaInicio").value = data.fechaInicio;
                document.getElementById("fechaFin").value = data.fechaFin;
                document.getElementById("estado").value = data.estado;

                // Mostrar el modal de edición
                editModal.classList.add("show");
            })
            .catch(error => console.error("Error al obtener los datos de la ficha:", error));
    });
});

// Cerrar modal con botón de "X"
if (closeEditButton) {
    closeEditButton.addEventListener("click", function () {
        console.log('Modal de edición cerrado');
        editModal.classList.remove("show");
    });
} // Elimina el `)` extra

// Cerrar modal al hacer clic fuera de él
window.onclick = function(event) {
    if (event.target === editModal) {
        console.log('Modal de edición cerrado desde el fondo');
        editModal.classList.remove("show");
    }
};


