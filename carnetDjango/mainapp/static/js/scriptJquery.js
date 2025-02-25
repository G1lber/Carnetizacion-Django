$(document).ready(function () {
    function toggleFields() {
        let selectedRole = $("#id_rol_FK").val(); // Obtiene el valor del rol seleccionado

        // Definir qué roles requieren qué campos
        let roles_con_credenciales = ["3"]; // Requiere username, password y email
        let roles_con_email = ["2"]; // Requiere email y ficha
        let roles_con_ficha = ["1", "2"]; // Requiere ficha

        // Manejo de username, password y email para rol "4"
        if (roles_con_credenciales.includes(selectedRole)) {
            $("#username_field, #password_field, #email").show();
        } else {
            $("#username_field, #password_field").hide();
            $("#id_username, #id_password").val('');
        }

        // Manejo del email para rol "3"
        if (roles_con_email.includes(selectedRole)) {
            $("#email").show();
        } else if (!roles_con_credenciales.includes(selectedRole)) { 
            $("#email").hide();
            $("#id_email").val('');
        }

        // Manejo del campo ficha para roles "2" y "3"
        if (roles_con_ficha.includes(selectedRole)) {
            $("#ficha").show();
        } else {
            $("#ficha").hide();
            $("#id_ficha").val('');
        }
    }

    // Detecta cambios en el select de rol
    $("#id_rol_FK").on("change", toggleFields);
    toggleFields(); // Ejecuta la función al cargar la página para el estado inicial
});