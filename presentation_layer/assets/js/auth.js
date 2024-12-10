// assets/js/auth.js
$(document).ready(function () {
  $("#login-form").submit(function (event) {
    event.preventDefault(); // Evita el envío estándar del formulario
    var email = $("#email").val(); // Obtiene el correo electrónico
    var password = $("#password").val(); // Obtiene la contraseña

    // Realiza la solicitud AJAX para el inicio de sesión
    $.ajax({
      url: "/api/login",
      method: "POST",
      contentType: "application/json",
      data: JSON.stringify({ email: email, password: password }),
      success: function (response) {
        // Guarda el token en localStorage
        localStorage.setItem("token", response.token);
        // Redirige al usuario a su página principal
        window.location.href = "cliente/reservas.html";
      },
      error: function (error) {
        // Muestra un mensaje de error
        alert("Error al iniciar sesión: " + error.responseJSON.message);
      },
    });
  });
});
