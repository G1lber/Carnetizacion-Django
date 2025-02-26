document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("modal");
    const closeButton = document.getElementById("closeButton");
    const form = document.getElementById("editForm");
    const mensajeExito = document.createElement("div");

    // Estilos del mensaje
    mensajeExito.style.position = "absolute";
    mensajeExito.style.top = "10px";
    mensajeExito.style.left = "50%";
    mensajeExito.style.transform = "translateX(-50%)";
    mensajeExito.style.backgroundColor = "#28a745";
    mensajeExito.style.color = "white";
    mensajeExito.style.padding = "10px 20px";
    mensajeExito.style.borderRadius = "5px";
    mensajeExito.style.display = "none";
    mensajeExito.style.zIndex = "1000";
    mensajeExito.textContent = "Cambios realizados con éxito ✅";
    document.body.appendChild(mensajeExito);

    // Función para mostrar mensaje de éxito
    function mostrarMensaje() {
        mensajeExito.style.display = "block";
        setTimeout(() => {
            mensajeExito.style.display = "none"; 
        }, 3000);
    }

    document.querySelectorAll(".btn-edit").forEach(button => {
        button.addEventListener("click", function () {
            const documento = this.getAttribute("data-id");
            const rh = this.getAttribute("data-rh");

            document.getElementById("usuarioDocumento").value = documento;
            document.getElementById("rh").value = rh;

            modal.classList.add("show");  // ✅ Ahora el modal usa la clase correcta
        });
    });

    closeButton.addEventListener("click", function () {
        modal.classList.remove("show");  // ✅ Cerrar con la clase correcta
    });

    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.classList.remove("show");
        }
    });

    // Enviar el formulario con AJAX
    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const formData = new FormData(form);

        fetch(editarAprendizURL, {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                modal.classList.remove("show");  // ✅ Ahora el modal se cierra correctamente
                mostrarMensaje();  
                setTimeout(() => location.reload(), 1000);  
            } else {
                alert("Error: " + data.message);
            }
        })
        .catch(error => console.error("Error en la solicitud:", error));
    });
});