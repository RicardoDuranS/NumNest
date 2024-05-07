document.addEventListener("DOMContentLoaded", function () {
  var form = document.getElementById("registroForm");
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    var usuario = document.getElementById("usuario").value;
    var contrasena = document.getElementById("contrasena").value;
    var grupo = document.getElementById("grupo").value;
    var genero = document.getElementById("genero").value;
    var listNum = document.getElementById("listNum").value;

    fetch("https://rickyduran.pythonanywhere.com/usuario/crear", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        nombre_usuario: usuario,
        contrasena: contrasena,
        grupo: grupo,
        genero: genero,
        listNum: listNum,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.message == "Creación de estudiante") {
          alert(
            "El ESTUDIANTE se creó con éxito. Favor de iniciar sesion, con el usuario registrado."
          );
          usuarioValido();
        } else if (data.message == "Creación de maestro") {
          alert(
            "El MAESTRO se creó con éxito. Favor de iniciar sesion, con el usuario registrado."
          );
          usuarioValido();
        } else {
          console.error("Error:", data);
        }
      })
      .catch((error) => console.error("Error:", error));
  });

  // Obtén el elemento <select> por su ID
  var selectGrupo = document.getElementById("grupo");

  // Hacer la petición al endpoint /grupos/listar
  fetch("https://rickyduran.pythonanywhere.com/grupos/listar")
    .then((response) => response.json())
    .then((grupos) => {
      // Itera sobre la lista de grupos
      grupos.forEach((grupoId) => {
        // Crea un nuevo elemento <option> para cada grupo
        var option = document.createElement("option");
        option.value = grupoId; // Asume que cada elemento de la lista es un ID de grupo
        option.text = `Grupo ${grupoId}`;

        // Añade el <option> al <select>
        selectGrupo.appendChild(option);
      });
    })
    .catch((error) => console.error("Error al obtener los grupos:", error));
});

function cancelarFormulario() {
  window.location.href = "login.html"; // Cambia "index.html" por la página a la que deseas redirigir
}

function usuarioValido() {
  window.location.href = "login.html"; // Cambia "index.html" por la página a la que deseas redirigir
}
