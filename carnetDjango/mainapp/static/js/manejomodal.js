document.addEventListener("DOMContentLoaded", function () {
    const editModal = document.getElementById("editModal");
    const closeEditButton = document.querySelector(".close-button"); // Asegúrate de que esta clase es correcta

    if (!editModal) {
        console.error("Error: No se encontró el modal de edición en el DOM.");
        return; // Evita ejecutar el código si el modal no existe
    }

    if (!closeEditButton) {
        console.error("Error: No se encontró el botón de cerrar en el DOM.");
    }

    // Delegación de eventos para los botones de edición
    document.addEventListener("click", function (event) {
        if (event.target.classList.contains("btn-edit")) {
            let userId = event.target.getAttribute("data-id");

            console.log(`Abriendo modal de edición para usuario ID: ${userId}`);

            // Hacer una solicitud AJAX para obtener los datos del usuario desde la base de datos
            fetch(`/obtener-usuario/${userId}/`)
                .then(response => response.json())
                .then(data => {
                    console.log("Datos obtenidos:", data);

                    // Llenar los campos del modal con los datos obtenidos
                    document.getElementById("editDocumento").value = data.documento;
                    document.getElementById("editFirstName").value = data.first_name;
                    document.getElementById("editLastName").value = data.last_name;
                    document.getElementById("editUsername").value = data.username;
                    document.getElementById("editPassword").value = data.password;

                      // Llenar el select con opciones dinámicas
                    let selectRh = document.getElementById("editRh");
                    selectRh.innerHTML = ""; // Limpiar opciones previas
                    data.opciones.forEach(opcion => {
                        let option = document.createElement("option");
                        option.value = opcion[0];
                        option.textContent = opcion[1];
                        if (opcion[0] == data.opcion_seleccionada) {
                            option.selected = true;
                        }
                        selectRh.appendChild(option);
                    });

                    let selectRol = document.getElementById("editRol");
                    selectRol.innerHTML = ""; // Limpiar opciones previas
                    data.roles.forEach(opcion => {
                        let option = document.createElement("option");
                        option.value = opcion[0];
                        option.textContent = opcion[1];
                        if (opcion[0] == data.opcion_anterior) {
                            option.selected = true;
                        }
                        selectRol.appendChild(option);
                    });

                    let selectTipo_doc = document.getElementById("editTipo");
                    selectTipo_doc.innerHTML = ""; // Limpiar opciones previas
                    data.tipos.forEach(opcion => {
                        let option = document.createElement("option");
                        option.value = opcion[0];
                        option.textContent = opcion[1];
                        if (opcion[0] == data.opcion_antes) {
                            option.selected = true;
                        }
                        selectTipo_doc.appendChild(option);
                    });

                    // Mostrar el modal
                    editModal.classList.add("show");
                })
                .catch(error => console.error("Error al obtener los datos del usuario:", error));
        }
    });

    // Cerrar modal con botón de "X"
    if (closeEditButton) {
        closeEditButton.addEventListener("click", function () {
            console.log("Modal de edición cerrado");
            editModal.classList.remove("show");
        });
    }

    // Cerrar modal al hacer clic fuera de él
    window.addEventListener("click", function (event) {
        if (event.target === editModal) {
            console.log("Modal de edición cerrado desde el fondo");
            editModal.classList.remove("show");
        }
    });

    // Obtener el token CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === name + "=") {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie("csrftoken"); // Obtiene el token CSRF

    // Manejo del formulario de edición
    
});
