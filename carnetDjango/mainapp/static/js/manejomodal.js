document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('editModal');
    var span = document.getElementsByClassName('close')[0];
    var editButtons = document.querySelectorAll('.btn-edit');

    editButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            var row = this.closest('tr');
            var documento = row.querySelector('td:nth-child(3)').innerText;
            var firstName = row.querySelector('td:nth-child(1)').innerText;
            var lastName = row.querySelector('td:nth-child(2)').innerText;

            document.getElementById('editDocumento').value = documento;
            document.getElementById('editFirstName').value = firstName;
            document.getElementById('editLastName').value = lastName;

            modal.style.display = 'block';
        });
    });

    span.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }

});
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');  // Obtén el token CSRF

document.getElementById('editForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = {
        documento: document.getElementById('editDocumento').value,
        first_name: document.getElementById('editFirstName').value,
        last_name: document.getElementById('editLastName').value,
    };

    fetch('/actualizar-usuario/', {
        method: 'POST',
        body: JSON.stringify(formData),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken  // Envía el token CSRF
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Usuario actualizado correctamente');
            modal.style.display = 'none';
            location.reload();  // Recargar la página para ver los cambios
        } else {
            alert('Error al actualizar el usuario: ' + data.error);
        }
    })
    .catch(error => console.error('Error:', error));
});
