$(document).ready(function () {
    function toggleFields() {
        let selectedRole = $("#id_rol_FK").val(); // Obtiene el valor del rol seleccionado

        // Definir qué roles requieren qué campos
        let roles_con_credenciales = ["4"]; // Requiere username, password y email
        let roles_con_email = ["3"]; // Requiere email
        let roles_con_ficha = ["2", "3"]; // Requiere ficha

        // Ocultar todos los campos y limpiar sus valores
        $("#id_username, #id_password, #id_email, #id_ficha").val('').prop("disabled", true);
        $("#username_field, #password_field, #email_field, #ficha_field").hide();

        // Si el rol seleccionado está en la lista, se muestran y habilitan los campos
        if (roles_con_credenciales.includes(selectedRole)) {
            $("#username_field, #password_field, #email_field").show();
            $("#id_username, #id_password, #id_email").prop("disabled", false);
        }

        if (roles_con_email.includes(selectedRole)) {
            $("#email_field").show();
            $("#id_email").prop("disabled", false);
        }

        if (roles_con_ficha.includes(selectedRole)) {
            $("#ficha_field").show();
            $("#id_ficha").prop("disabled", false);
        }
    }

    // Detecta cambios en el select de rol
    $("#id_rol_FK").on("change", toggleFields);
    
    // Ejecuta la función al cargar la página para limpiar, establecer visibilidad y deshabilitar correctamente
    toggleFields();
});