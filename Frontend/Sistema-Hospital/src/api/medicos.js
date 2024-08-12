async function obtenerPersonalMedico() {
    return new Promise((resolve, reject) => {
        fetch("http://127.0.0.1:8000/personal_medico/")
            .then((res) => {
                if (!res.ok) {
                    throw new Error("Error al obtener el personal médico");
                }
                return res.json();
            })
            .then((personalMedico) => {
                resolve(personalMedico);
            })
            .catch((error) => {
                console.error("Error al enviar la petición de personal médico al servidor: " + error);
                reject(error);
            });
    });
}

export {obtenerPersonalMedico}