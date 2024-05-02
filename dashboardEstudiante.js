document.addEventListener("DOMContentLoaded", function () {
  // Obtener la instancia actual de la URL
  const url = new URL(window.location.href);

  // Usar URLSearchParams para acceder al parámetro 'usuario_id'
  const usuario_id = url.searchParams.get("usuario_id");

  console.log(usuario_id); // Ahora puedes usar 'usuario_id' en tu cód

  // Realizar la solicitud AJAX para obtener todos los datos de estadísticas//////////CAMBIO ENPOINT
  fetch("https://rickyduran.pythonanywhere.com/dashboard/estudiante", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify({
      estudiante_id: usuario_id, // Reemplaza "valor" con el valor real que deseas enviar
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Datos recibidos del endpoint /estats:", data);

      // Accede directamente a "estudiante_info" y "puntajes" desde los datos recibidos
      const estudianteInfo = data.estudiante_info;
      const puntajesData = data.puntajes;

      // Obtén la referencia a la tabla
      const table = document.getElementById("dataEstudianteTable");

      // Crea una nueva fila para "estudiante_info"
      const row = table.insertRow();

      // Crea celdas para cada propiedad de "estudiante_info"
      const cellEstudianteId = row.insertCell();
      const cellGrupo = row.insertCell();
      const cellListNum = row.insertCell();
      const cellProgreso = row.insertCell();

      // Asigna los valores a las celdas
      cellEstudianteId.textContent = estudianteInfo.estudiante_id;
      cellGrupo.textContent = estudianteInfo.grupo;
      cellListNum.textContent = estudianteInfo.listNum;
      cellProgreso.textContent = estudianteInfo.progreso;

      // CREAR TABLA DE Info/////////////////////////////////////////////////////
      // Obtén la referencia a la tabla
      const puntajeTable = document.getElementById("puntajeTable");

      // Itera sobre los datos de maestros para insertarlos en la tabla
      puntajesData.forEach((item) => {
        // Crea una nueva fila
        const row = puntajeTable.insertRow();

        // Crea una celda para 'maestro_id' y 'grupo'
        const cellEstudianteId = row.insertCell();
        const cellFecha = row.insertCell();
        const cellNivelID = row.insertCell();
        const cellValor = row.insertCell();

        // Asigna los valores a las celdas
        cellEstudianteId.textContent = item.estudiante_id;
        cellFecha.textContent = item.fecha;
        cellNivelID.textContent = item.nivel_id;
        cellValor.textContent = item.valor;
        /////////////////////////////////////////////////////////////////////////////////////////
      });
    })
    .catch((error) => console.error("Error:", error));
});
