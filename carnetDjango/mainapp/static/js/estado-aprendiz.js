document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".estado-btn").forEach(button => {
        button.addEventListener("click", function () {
            const documento = this.getAttribute("data-id");
            const ficha = this.getAttribute("data-ficha");
            const estadoActual = this.getAttribute("data-estado") === "True";
            const nuevoEstado = !estadoActual;

            fetch("/cambiar_estado_aprendiz/", {  
                method: "POST",
                body: JSON.stringify({ documento: documento, ficha: ficha, estado: nuevoEstado }),
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken()
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    this.textContent = nuevoEstado ? "Activo" : "Inactivo";
                    this.classList.toggle("activo", nuevoEstado);
                    this.classList.toggle("inactivo", !nuevoEstado);
                    this.setAttribute("data-estado", nuevoEstado ? "True" : "False");
                } else {
                    alert("Error: " + data.message);
                }
            })
            .catch(error => console.error("Error en la solicitud:", error));
        });
    });

    function getCSRFToken() {
        const cookieValue = document.cookie
            .split("; ")
            .find(row => row.startsWith("csrftoken="))
            ?.split("=")[1];
        return cookieValue || "{{ csrf_token }}";
    }
});
