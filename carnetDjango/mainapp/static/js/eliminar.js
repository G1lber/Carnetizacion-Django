document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".btn-delete").forEach(button => {
        button.addEventListener("click", function () {
            let documento = this.getAttribute("data-documento");
            let url = this.getAttribute("data-url");

            if (confirm(`¿Estás seguro de que quieres eliminar el usuario con documento ${documento}?`)) {
                fetch(url, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                        "X-CSRFToken": getCSRFToken()  // Añadir CSRF Token
                    },
                    body: `documento=${documento}`
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert("Usuario eliminado correctamente.");
                        document.getElementById(`usuario-${documento}`).remove(); // Elimina la fila de la tabla
                    } else {
                        alert(`Error: ${data.error}`);
                    }
                })
                .catch(error => console.error("Error al eliminar usuario:", error));
            }
        });
    });
});

// Función para obtener el token CSRF desde el template
function getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute("content");
}
