async function registrarSolicitud(solicitud) {
  return new Promise((resolve, reject) => {
      fetch("http://127.0.0.1:8000/solicitudes/", {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify(solicitud),
      })
      .then((res) => {
          if (!res.ok) {
              throw new Error("Error al registrar la solicitud");
          }
          return res.json();
      })
      .then((response) => {
          resolve(response);
      })
      .catch((error) => {
          console.error("Error al enviar la solicitud al servidor: " + error);
          reject(error);
      });
  });
}

async function obtenerDatosSolicitud() {
    return new Promise((resolve, reject) => {
        fetch("http://127.0.0.1:8000/solicitudes/")
            .then((res) => {
                if (!res.ok) {
                    throw new Error("Error al obtener el personal médico");
                }
                return res.json();
            })
            .then((solicitud) => {
                resolve(solicitud);
            })
            .catch((error) => {
                console.error("Error al enviar la petición de personal médico al servidor: " + error);
                reject(error);
            });
    });
}

export {registrarSolicitud, obtenerDatosSolicitud}