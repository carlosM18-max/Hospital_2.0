async function obtenerSolicitudes() {
  return new Promise((resolve, reject) => {
    fetch("http://127.0.0.1:8000/solicitudes/")
      .then((res) => {
        if (!res.ok) {
          throw new Error("Error al obtener las soliciutudes");
        }
        return res.json();
      })
      .then((solicitudes) => {
        resolve(solicitudes);
      })
      .catch((error) => {
        console.error("Error al enviar la peticion de la solicitud al servidor: " + error);
        reject(error);
      });
  });
};

async function obtenerSolicitudes2(solicitud) {
  return new Promise((resolve, reject) => {
    fetch("http://127.0.0.1:8000/solicitudes/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(solicitud),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error(
            "Error al obtener las solicitudes: " + res
          );
        }

        resolve(res.json());
      })
      .catch((error) => {
        console.error(
          "Error al enviar la peticion de la solicitud al servidor: " + error
        );
        reject(error);
      });
  });
};

async function obtenerSolicitudesID(solicitud) {
  return new Promise((resolve, reject) => {
    fetch("http://127.0.0.1:8000/solicitudes/{id}", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(solicitud),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error(
            "Error al obtener las solicitudes: " + res
          );
        }

        resolve(res.json());
      })
      .catch((error) => {
        console.error(
          "Error al enviar la peticion de la solicitud al servidor: " + error
        );
        reject(error);
      });
  });
};
async function crearSolicitud(solicitud) {
  return new Promise((resolve, reject) => {
    fetch("http://127.0.0.1:8000/solicitudes/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(solicitud),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error(
            "Error al crear la solicitud: " + res
          );
        }

        resolve(res.json());
      })
      .catch((error) => {
        console.error(
          "Error al enviar la peticion de la solicitud al servidor: " + error
        );
        reject(error);
      });
  });
};

async function actualizarSolicitud(solicitud) {
  return new Promise((resolve, reject) => {
    fetch("http://127.0.0.1:8000/solicitudes/{id}", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(solicitud),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error(
            "Error al actualizar la solicitud de la solicitud al servidor: " + res
          );
        }

        resolve(res.json());
      })
      .catch((error) => {
        console.error(
          "Error al enviar la peticion de la solicitud al servidor: " + error
        );
        reject(error);
      });
  });
};

async function eliminarSolicitud(solicitud) {
  return new Promise((resolve, reject) => {
    fetch("http://127.0.0.1:8000/solicitudes/{id}", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(solicitud),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error(
            "Error al insertar los datos de la solicitud al servidor: " + res
          );
        }

        resolve(res.json());
      })
      .catch((error) => {
        console.error(
          "Error al enviar la peticion de la solicitud al servidor: " + error
        );
        reject(error);
      });
  });
};

export { obtenerSolicitudes, obtenerSolicitudesID, crearSolicitud, actualizarSolicitud, eliminarSolicitud };
