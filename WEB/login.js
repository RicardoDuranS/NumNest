document.addEventListener("DOMContentLoaded", function () {
  var form = document.getElementById("loginForm");
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    var usuario = document.getElementById("usuario").value;
    var contrasena = document.getElementById("contrasena").value;

    fetch("https://rickyduran.pythonanywhere.com/usuario/validar", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        nombre_usuario: usuario,
        contrasena: contrasena,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        // Verifica si el usuario es válido
        if (data[1].message === "Usuario no valido") {
          alert("El usuario no es válido.");
        } else {
          // Identifica si el usuario es un estudiante
          if (data[0].usuario === "estudiante") {
            // Redirige a dashboardEstudiante.html incluyendo el usuario_id como parámetro de consulta
            window.location.href =
              "dashboardEstudiante.html?usuario_id=" +
              encodeURIComponent(data[1].usuario_id);
          } else {
            // Redirige a dashboardMaestros.html
            window.location.href = "dashboardMaestros.html";
          }
        }
      })
      .catch((error) => console.error("Error:", error));
  });
});
