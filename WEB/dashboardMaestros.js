document.addEventListener("DOMContentLoaded", function () {
  // Avance Global///////////////////////////
  let modelsData = {
    labels: ["Mundo 1", "Mundo 2", "Mundo 3", "Mundo 4"],
    datasets: [
      {
        label: "Avance Global",
        data: [10, 20, 30, 40],
        backgroundColor: [
          "rgba(143, 192, 39, 1)",
          "rgba(58, 85, 124, 1)",
          "rgba(166, 166, 166, 1)",
          "rgba(255, 255, 255, 1)",
        ],
        borderColor: [
          "rgba(143, 192, 39, 1)",
          "rgba(58, 85, 124, 1)",
          "rgba(166, 166, 166, 1)",
          "rgba(255, 255, 255, 1)",
        ],
        borderWidth: 1,
      },
    ],
  };

  // Crear instancias de los gráficos
  const modelsChart = new Chart(
    document.getElementById("modelsChart").getContext("2d"),
    {
      type: "doughnut",
      data: modelsData,
      options: {
        plugins: {
          legend: {
            position: "left",
          },
        },
      },
    }
  );

  //Comparativa de avance por género////////////////////////////////////////////
  // Obtén el elemento canvas
  const featuresCanvas = document.getElementById("featuresChart");

  // Ahora inicializa el gráfico
  const featuresData = {
    labels: ["Hombres", "Mujeres"],
    datasets: [
      {
        label: "Avance",
        data: [1.7, 2],
        backgroundColor: "rgba(143, 192, 39, 1)",
        borderColor: "rgba(143, 192, 39, 1)",
        borderWidth: 1,
      },
    ],
  };

  const featuresChart = new Chart(featuresCanvas.getContext("2d"), {
    type: "bar",
    data: featuresData,
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });

  //downloadsChart ///////////////////////////////////////////////////////
  const downloadsCanvas = document.getElementById("studentsChart");
  const ctx = downloadsCanvas.getContext("2d");

  ctx.font = "72px Arial";
  ctx.textAlign = "center";
  ctx.fillStyle = "white";
  // Número a mostrar
  const number = 100;

  // Dibujar el número en el canvas
  ctx.fillText(number, downloadsCanvas.width / 2, downloadsCanvas.height / 2);

  const activePChartCanvas = document.getElementById("activePlayersChart");
  const cts = activePChartCanvas.getContext("2d");

  // Establecer el tamaño del canvas
  activePChartCanvas.width = 400;
  activePChartCanvas.height = 200;

  cts.font = "72px Arial";
  cts.textAlign = "center";
  cts.fillStyle = "white";
  // Número a mostrar
  const numberActivePlayers = 100;

  // Dibujar el número en el canvas
  cts.fillText(
    numberActivePlayers,
    activePChartCanvas.width / 2,
    activePChartCanvas.height / 2
  );

  // Realizar la solicitud AJAX para obtener todos los datos de estadísticas//////////CAMBIO ENPOINT
  fetch("https://rickyduran.pythonanywhere.com/dashboard/maestros", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify({
      /* datos a enviar al backend si es necesario */
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Datos recibidos del endpoint /estats:", data);

      // Desestructurar los datos obtenidos
      const maestrosData = data[0];
      //Estudiantes
      const estudiantesData = data[1];
      //Score
      const topPuntajeData = data[2];
      //avanceGlobalData
      const avanceGlobalData = data[3];
      //avanceGeneroData
      const avanceGeneroData = data[4];
      // estadisticasJugadoresData
      const estadisticasJugadoresData = data[5];
      // gruposLista
      const gruposData = data[6];
      // Todos los puntajes
      const puntajeData = data[7];

      // Update the chart for Avance Global///////////////////////////////////////
      modelsChart.data.datasets[0].data = avanceGlobalData;
      modelsChart.update();

      // Update the chart for Comparativa de avance por género//////////////////////
      featuresChart.data.datasets[0].data = avanceGeneroData;
      featuresChart.update();

      // Actualizar el número de descargas/////////////////////////////////////////
      const downloadsCanvas = document.getElementById("studentsChart");
      const ctx = downloadsCanvas.getContext("2d");
      ctx.clearRect(0, 0, downloadsCanvas.width, downloadsCanvas.height);
      ctx.font = "72px Arial";
      ctx.textAlign = "center";
      ctx.fillStyle = "white";
      ctx.fillText(
        estadisticasJugadoresData[0],
        downloadsCanvas.width / 2,
        downloadsCanvas.height / 2
      );

      // Actualizar el número de jugadores activos/////////////////////////////////
      const activePChartCanvas = document.getElementById("activePlayersChart");
      const cts = activePChartCanvas.getContext("2d");
      cts.clearRect(0, 0, activePChartCanvas.width, activePChartCanvas.height);
      cts.font = "72px Arial";
      cts.textAlign = "center";
      cts.fillStyle = "white";
      cts.fillText(
        estadisticasJugadoresData[1],
        activePChartCanvas.width / 2,
        activePChartCanvas.height / 2
      );

      // CREAR TABLA DE MAESTROS/////////////////////////////////////////////////////
      // Obtén la referencia a la tabla
      const table = document.getElementById("dataTable");

      // Función para convertir la celda del grupo en un menú desplegable
      function editRow(row, gruposData) {
        const cells = row.cells;

        // Crea un elemento select para el grupo
        const grupoSelect = document.createElement("select");
        grupoSelect.name = "grupo";

        // Agrega una opción para indicar que no hay grupo asignado
        const optionSinGrupo = document.createElement("option");
        optionSinGrupo.value = ""; // Puedes usar una cadena vacía o 'null' si prefieres
        optionSinGrupo.textContent = "No asignado";
        grupoSelect.appendChild(optionSinGrupo);

        // Agrega las opciones al select basadas en gruposData
        gruposData.forEach((grupo) => {
          const option = document.createElement("option");
          option.value = grupo;
          option.textContent = grupo;
          grupoSelect.appendChild(option);
        });

        // Establece el valor actual del grupo como la opción seleccionada
        grupoSelect.value = cells[1].textContent;

        // Reemplaza el contenido de la celda del grupo con el select
        cells[1].textContent = "";
        cells[1].appendChild(grupoSelect);

        // Reemplaza el botón de edición por un botón de guardar
        const saveBtn = document.createElement("button");
        saveBtn.className = "edit-btn";
        saveBtn.textContent = "Guardar";
        cells[2].innerHTML = ""; // Limpia la celda de acciones
        cells[2].appendChild(saveBtn);

        // Agrega un evento de clic al botón de guardar
        saveBtn.addEventListener("click", () => handleData(row, grupoSelect));
      }

      // Función para manejar los datos modificados
      function handleData(row, grupoSelect) {
        const cells = row.cells;
        // Asume que la celda 0 es la del maestro ID y no se modifica
        const maestroId = cells[0].textContent; // No se modifica, solo se lee
        const grupo = grupoSelect.value; // Obtiene el valor seleccionado del select

        // Prepara los datos a enviar como JSON
        const dataToSend = {
          maestro_id: maestroId,
          grupo: grupo,
        };
        console.log(dataToSend);

        // Define el endpoint al que enviarás los datos
        const endpoint =
          "https://rickyduran.pythonanywhere.com/maestro/modificar"; // Reemplaza con tu endpoint real

        // Realiza la solicitud POST con los datos
        fetch(endpoint, {
          method: "POST", // Especifica el método HTTP
          headers: {
            "Content-Type": "application/json", // Indica que estás enviando JSON
          },
          body: JSON.stringify(dataToSend), // Convierte el objeto a una cadena JSON
        })
          .then((response) => {
            if (!response.ok) {
              // Verifica si la respuesta no es exitosa
              throw new Error("Error al enviar los datos"); // Lanza un error si la respuesta no es exitosa
            }
            return response.json(); // Si la respuesta es exitosa, conviértela a JSON
          })
          .then((data) => {
            console.log("Datos enviados exitosamente:", data);
            // Verifica si el mensaje es "ok"
            if (data.message == true) {
              // Muestra una alerta de éxito
              alert("Todo salió bien.");
            } else {
              // Muestra una alerta de error
              alert("Hubo un error al modificar el maestro.");
            }
            // Aquí puedes manejar la respuesta del servidor, por ejemplo, actualizar la UI
          })
          .catch((error) => {
            console.error("Hubo un error:", error);
            // Muestra una alerta de error
            alert("Hubo un error al modificar el maestro.");
            // Maneja el error, por ejemplo, mostrando un mensaje al usuario
          });

        // Después de manejar los datos, puedes volver a mostrar los valores de texto y el botón de edición
        cells[1].textContent = grupo;
        cells[2].innerHTML = "";
        const editBtn = document.createElement("button");
        editBtn.className = "edit-btn";
        editBtn.textContent = "Editar";
        cells[2].appendChild(editBtn);
        editBtn.addEventListener("click", () => editRow(row, gruposData)); // Asegúrate de pasar gruposData aquí
      }

      // Itera sobre los datos de maestros para insertarlos en la tabla
      maestrosData.forEach((item) => {
        // Crea una nueva fila
        const row = table.insertRow();

        // Crea una celda para 'maestro_id' y 'grupo'
        const cellMaestroId = row.insertCell();
        const cellGrupo = row.insertCell();
        const cellAcciones = row.insertCell(); // Celda para acciones

        // Asigna los valores a las celdas
        cellMaestroId.textContent = item.maestro_id;
        cellGrupo.textContent = item.grupo;

        // Agrega un botón de edición en la celda de acciones
        const editBtn = document.createElement("button");
        editBtn.className = "edit-btn";
        editBtn.textContent = "Editar";
        cellAcciones.appendChild(editBtn);
        cellAcciones.className = "action-cell"; // Aplica el estilo a la celda de acciones

        // Agrega un evento de clic al botón de edición
        editBtn.addEventListener("click", () => editRow(row, gruposData));

        /////////////////////////////////////////////////////////////////////////////////////////
      });
      //Tabla de grupos////////////////////////////////////////////////////////////////////////
      // Obtén la referencia a la tabla de grupos
      const gruposTable = document.getElementById("gruposTable");

      // Itera sobre los grupos para insertarlos en la tabla
      gruposData.forEach((grupo, index) => {
        // Crea una nueva fila
        const row = gruposTable.insertRow();

        // Crea una celda para el nombre del grupo
        const cellGrupo = row.insertCell();
        // Asigna el valor al grupo
        cellGrupo.textContent = grupo;

        // Crea una celda para el botón "Eliminar"
        const cellEliminar = row.insertCell();
        const btnEliminar = document.createElement("button");
        btnEliminar.textContent = "Eliminar";
        btnEliminar.className = "btn-eliminar";
        btnEliminar.dataset.grupoId = grupo.id; // Asume que cada grupo tiene un ID
        btnEliminar.addEventListener("click", function () {
          // Prepara los datos a enviar como JSON
          const dataToSend = {
            grupo_id: cellGrupo.textContent, // Utiliza el ID del grupo para identificar el grupo a eliminar
          };

          // Realiza la solicitud POST para eliminar el grupo
          fetch("https://rickyduran.pythonanywhere.com/grupo/eliminar", {
            method: "POST", // Especifica el método HTTP
            headers: {
              "Content-Type": "application/json", // Indica que estás enviando JSON
            },
            body: JSON.stringify(dataToSend), // Convierte el objeto a una cadena JSON
          })
            .then((response) => {
              if (!response.ok) {
                // Verifica si la respuesta no es exitosa
                throw new Error("Error al enviar los datos"); // Lanza un error si la respuesta no es exitosa
              }
              return response.json(); // Si la respuesta es exitosa, conviértela a JSON
            })
            .then((data) => {
              if (data.message == true) {
                alert("El grupo se ha eliminado con exito.");
              }
              console.log("Grupo eliminado exitosamente:", data);
              // Aquí puedes manejar la respuesta del servidor, por ejemplo, actualizar la UI
              // Por ejemplo, podrías eliminar la fila de la tabla
              this.closest("tr").remove();
            })
            .catch((error) => {
              console.error("Hubo un error:", error);
              // Muestra una alerta de error
              alert("Hubo un error al eliminar el grupo.");
              // Maneja el error, por ejemplo, mostrando un mensaje al usuario
            });
        });
        cellEliminar.appendChild(btnEliminar);
      });

      // Fila para agregar grupos
      const row = gruposTable.insertRow(-1); // -1 para agregar al final

      // Crea una celda para el input
      const cellInput = row.insertCell();
      const input = document.createElement("input");
      input.type = "number";
      cellInput.appendChild(input);

      // Crea una celda para el botón "Agregar"
      const cellAgregar = row.insertCell();
      const btnAgregar = document.createElement("button");
      btnAgregar.textContent = "Agregar";
      btnAgregar.className = "edit-btn";
      btnAgregar.addEventListener("click", () => {
        const grupo = input.value;
        const dataToSend = {
          grupo_id: grupo,
        };

        fetch("https://rickyduran.pythonanywhere.com/grupo/agregar", {
          method: "POST", // Especifica el método HTTP
          headers: {
            "Content-Type": "application/json", // Indica que estás enviando JSON
          },
          body: JSON.stringify(dataToSend), // Convierte el objeto a una cadena JSON
        })
          .then((response) => {
            if (!response.ok) {
              // Verifica si la respuesta no es exitosa
              throw new Error("Error al enviar los datos"); // Lanza un error si la respuesta no es exitosa
            }
            return response.json(); // Si la respuesta es exitosa, conviértela a JSON
          })
          .then((data) => {
            console.log("Datos enviados exitosamente:", data);
            // Verifica si el mensaje es "ok"
            if (data.message == true) {
              // Muestra una alerta de éxito
              alert("Todo salió bien.");
            } else {
              // Muestra una alerta de error
              alert("Hubo un error al modificar grupo.");
            }
            // Aquí puedes manejar la respuesta del servidor, por ejemplo, actualizar la UI
          })
          .catch((error) => {
            console.error("Hubo un error:", error);
            // Muestra una alerta de error
            alert("Hubo un error al modificar el gruop.");
            // Maneja el error, por ejemplo, mostrando un mensaje al usuario
          });

        // Aquí va la lógica para manejar el agregar
        console.log("Agregar número:", input.value);
        // Aquí puedes agregar la lógica para agregar el número a tu lista de grupos y actualizar la tabla
      });
      cellAgregar.appendChild(btnAgregar);

      //TABLA ESTUDIANTES/////////////////////////////////////////////\
      // Función para convertir la celda del grupo en un menú desplegable y agregar un botón de guardar
      function editRowEstudiantes(row, gruposData) {
        const cells = row.cells;

        // Convierte solo la celda del número de lista en un input de texto
        const listNumCell = cells[1]; // Asume que la celda del número de lista es la segunda celda
        const listNumInput = document.createElement("input");
        listNumInput.type = "text";
        listNumInput.value = listNumCell.textContent; // Establece el valor actual de la celda
        listNumCell.textContent = "";
        listNumCell.appendChild(listNumInput);

        // Crea un elemento select para el grupo
        const grupoSelect = document.createElement("select");
        grupoSelect.name = "grupo";

        // Agrega una opción para indicar que no hay grupo asignado
        const optionSinGrupo = document.createElement("option");
        optionSinGrupo.value = "";
        optionSinGrupo.textContent = "No asignado";
        grupoSelect.appendChild(optionSinGrupo);

        // Agrega las opciones al select basadas en gruposData
        gruposData.forEach((grupo) => {
          const option = document.createElement("option");
          option.value = grupo;
          option.textContent = grupo;
          grupoSelect.appendChild(option);
        });

        // Establece el valor actual del grupo como la opción seleccionada
        grupoSelect.value = cells[2].textContent;

        // Reemplaza el contenido de la celda del grupo con el select
        cells[2].textContent = "";
        cells[2].appendChild(grupoSelect);

        // Reemplaza el botón de edición por un botón de guardar
        const saveBtn = document.createElement("button");
        saveBtn.className = "edit-btn";
        saveBtn.textContent = "Guardar";
        cells[4].innerHTML = ""; // Limpia la celda de acciones
        cells[4].appendChild(saveBtn);

        // Agrega un evento de clic al botón de guardar
        saveBtn.addEventListener("click", () => {
          // Aquí recoge el valor del input y realiza las acciones necesarias para actualizar los datos
          const newListNum = listNumInput.value;
          console.log("Guardar cambios, nuevo número de lista:", newListNum);

          // Restablece la celda del número de lista a su valor original y elimina el input
          listNumCell.textContent = newListNum;
          listNumCell.innerHTML = ""; // Limpia el input
          listNumCell.appendChild(document.createTextNode(newListNum));

          // Restablece la celda del grupo a su valor original y elimina el select
          const grupo = grupoSelect.value;
          cells[2].textContent = grupo;
          cells[2].innerHTML = ""; // Limpia el select
          cells[2].appendChild(document.createTextNode(grupo));

          // Prepara los datos a enviar como JSON
          const dataToSend = {
            estudiante_id: cells[0].textContent, // Asume que la celda 0 es la del estudiante ID
            listNum: newListNum, // El nuevo número de lista
            grupo: grupo, // El grupo seleccionado
          };

          // Realiza la solicitud POST con los datos
          fetch("https://rickyduran.pythonanywhere.com/estudiante/modificar", {
            method: "POST", // Especifica el método HTTP
            headers: {
              "Content-Type": "application/json", // Indica que estás enviando JSON
            },
            body: JSON.stringify(dataToSend), // Convierte el objeto a una cadena JSON
          })
            .then((response) => {
              if (!response.ok) {
                // Verifica si la respuesta no es exitosa
                throw new Error("Error al enviar los datos"); // Lanza un error si la respuesta no es exitosa
              }
              return response.json(); // Si la respuesta es exitosa, conviértela a JSON
            })
            .then((data) => {
              console.log("Datos enviados exitosamente:", data);
              // Verifica si el mensaje es "ok"
              if (data.message == true) {
                // Muestra una alerta de éxito
                alert("Todo salió bien.");
              } else {
                // Muestra una alerta de error
                alert("Hubo un error al modificar el estudiante.");
              }
              // Aquí puedes manejar la respuesta del servidor, por ejemplo, actualizar la UI
            })
            .catch((error) => {
              console.error("Hubo un error:", error);
              // Muestra una alerta de error
              alert("Hubo un error al modificar el estudiante.");
              // Maneja el error, por ejemplo, mostrando un mensaje al usuario
            });

          // No olvides volver a mostrar el valor de texto y el botón de edición después de guardar
          cells[4].innerHTML = ""; // Limpia la celda de acciones
          const editBtn = document.createElement("button");
          editBtn.className = "edit-btn";
          editBtn.textContent = "Editar";
          cells[4].appendChild(editBtn);
          editBtn.addEventListener("click", () =>
            editRowEstudiantes(row, gruposData)
          );
        });
      }

      //TABLA ESTUDIANTES/////////////////////////////////////////////
      // Obtén la referencia a la tabla
      const estudiantesTable = document.getElementById("estudiantesTable");

      // Itera sobre los datos de estudiantes para insertarlos en la tabla
      estudiantesData.forEach((estudiante) => {
        // Crea una nueva fila
        const row = estudiantesTable.insertRow();

        // Crea una celda para 'estudiante_id'
        const cellEstudianteId = row.insertCell();
        cellEstudianteId.textContent = estudiante.estudiante_id;

        // Crea una celda para 'listNum'
        const cellListNum = row.insertCell();
        cellListNum.textContent = estudiante.listNum;

        // Crea una celda para 'grupo'
        const cellGrupo = row.insertCell();
        cellGrupo.textContent = estudiante.grupo;

        // Crea una celda para 'progreso'
        const cellProgreso = row.insertCell();
        cellProgreso.textContent = estudiante.progreso;

        // Crea una celda para el botón de edición
        const cellAcciones = row.insertCell();
        const editBtn = document.createElement("button");
        editBtn.className = "edit-btn";
        editBtn.textContent = "Editar";
        cellAcciones.appendChild(editBtn);

        // Agrega un evento de clic al botón de edición
        editBtn.addEventListener("click", () =>
          editRowEstudiantes(row, gruposData)
        );
      });
      //TABLA PUNTAJES///////////////////////////////////////
      insertarDatosEnTabla(puntajeData);
      // Función para insertar datos en la tabla de puntajes
      function insertarDatosEnTabla(datos) {
        const tbody = document.querySelector("#puntajesTable tbody");
        if (!tbody) {
          console.error(
            "No se encontró el elemento <tbody> en la tabla de puntajes."
          );
          return;
        }

        // Limpiar el contenido actual de la tabla
        while (tbody.firstChild) {
          tbody.removeChild(tbody.firstChild);
        }

        // Insertar los datos en el <tbody>
        datos.forEach((dato) => {
          const row = tbody.insertRow();
          const cellEstudianteId = row.insertCell();
          const cellNivelId = row.insertCell();
          const cellFecha = row.insertCell();
          const cellPuntaje = row.insertCell();

          cellEstudianteId.textContent = dato.estudiante_id;
          cellNivelId.textContent = dato.nivel_id;
          cellFecha.textContent = dato.fecha;
          cellPuntaje.textContent = dato.valor;
        });
      }

      // Función para filtrar puntajes por criterio
      function aplicarFiltro(criterio, valor) {
        let puntajesFiltrados = [];
        if (criterio === "estudiante_id") {
          puntajesFiltrados = puntajeData.filter(
            (puntaje) => puntaje.estudiante_id === parseInt(valor)
          );
        } else if (criterio === "nivel_id") {
          puntajesFiltrados = puntajeData.filter(
            (puntaje) => puntaje.nivel_id === parseInt(valor)
          );
        } else if (criterio === "top_5") {
          // Asumiendo que quieres mostrar los 5 primeros registros
          puntajesFiltrados = topPuntajeData;
        } else if (criterio === "nothing") {
          // Asumiendo que quieres mostrar los registros sin ninguna modificación
          puntajesFiltrados = puntajeData;
        }
        // Puedes agregar más condiciones aquí para otros criterios
        return puntajesFiltrados;
      }

      function insertarTopPuntajesEnTabla(datos) {
        const tbody = document.querySelector("#puntajesTable tbody");
        if (!tbody) {
          console.error(
            "No se encontró el elemento <tbody> en la tabla de top puntajes."
          );
          return;
        }

        // Limpiar el contenido actual de la tabla
        while (tbody.firstChild) {
          tbody.removeChild(tbody.firstChild);
        }

        // Insertar los datos en el <tbody>
        datos.forEach((dato) => {
          const row = tbody.insertRow();
          const cellEstudianteId = row.insertCell();
          const cellPuntaje = row.insertCell();

          cellEstudianteId.textContent = dato.estudiante_id;
          cellPuntaje.textContent = dato.valor;
        });
      }
      // Evento para aplicar el filtro
      document
        .getElementById("aplicarFiltroBtn")
        .addEventListener("click", function () {
          const criterio = document.getElementById("filtroSelect").value;
          const valor = document.getElementById("valorFiltroInput").value;
          const puntajesFiltrados = aplicarFiltro(criterio, valor);
          insertarDatosEnTabla(puntajesFiltrados); // Usa la misma función para insertar los datos filtrados
        });

      // Asegúrate de llamar a insertarDatosEnTabla con los datos iniciales cuando la página se cargue
      document.addEventListener("DOMContentLoaded", function () {
        insertarDatosEnTabla(puntajeData); // Asume que puntajeData contiene tus datos iniciales
      });
    })
    .catch((error) => console.error("Error:", error));
});
