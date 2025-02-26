$(document).ready(function() {
    $('.btn-delete').click(function() {
        var documento = $(this).data('documento');
        var url = $(this).data('url');
        console.log("Documento:", documento);  // Depuración
        console.log("URL:", url);  // Depuración
        console.log("CSRF Token:", csrftoken);  // Depuración

        if (confirm('¿Estás seguro de que deseas eliminar este usuario?')) {
            $.ajax({
                url: url,
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken
                },
                data: {
                    'documento': documento,
                },
                success: function(response) {
                    console.log("Respuesta del servidor:", response);  // Depuración
                    if (response.success) {
                        $('#usuario-' + documento).remove();
                    } else {
                        alert('Error al eliminar el usuario: ' + response.error);
                    }
                },
                error: function(xhr, status, error) {
                    console.error("Error en la solicitud AJAX:", error);  // Depuración
                    alert('Error al eliminar el usuario. Detalles: ' + xhr.responseText);
                }
            });
        }
    });
});