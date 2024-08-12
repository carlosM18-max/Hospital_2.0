async function obtenerPersonas() {
    return new Promise((resolve, reject) => {
        fetch("http://127.0.0.1:8000/persons/")
            .then((res) => {
                if (!res.ok) {
                    throw new Error("Error al obtener las personas");
                }
                return res.json();
            })
            .then((personas) => {
                resolve(personas);
            })
            .catch((error) => {
                console.error("Error al enviar la petición de personas al servidor: " + error);
                reject(error);
            });
    });
}


export { obtenerPersonas }