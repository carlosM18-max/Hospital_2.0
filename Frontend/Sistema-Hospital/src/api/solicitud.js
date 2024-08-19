async function registrarSolicitud(data) {
    try {
        const response = await fetch('http://127.0.0.1:8000/solicitudes/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`Error al registrar la solicitud: ${errorData.detail}`);
        }
        
        const result = await response.json();
        return result;
    } catch (error) {
        console.error(error.message);
        throw new Error('Error al registrar la solicitud');
    }
};

async function obtenerSolicitudes() {
    try {
        const response = await fetch('http://127.0.0.1:8000/solicitudes/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`Error al obtener las solicitudes: ${errorData.detail}`);
        }

        const result = await response.json();
        return result;
    } catch (error) {
        console.error(error.message);
        throw new Error('Error al obtener las solicitudes');
    }
};

async function obtenerSolicitudPorId(id) {
    try {
        const response = await fetch(`http://127.0.0.1:8000/solicitudes/${id}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`Error al obtener la solicitud con ID ${id}: ${errorData.detail}`);
        }

        const result = await response.json();
        return result;
    } catch (error) {
        console.error(error.message);
        throw new Error(`Error al obtener la solicitud con ID ${id}`);
    }
};

async function actualizarSolicitud(id, solicitudData) {
    try {
        const response = await fetch(`http://127.0.0.1:8000/solicitudes/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(solicitudData),
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`Error al actualizar la solicitud con ID ${id}: ${errorData.detail}`);
        }

        const result = await response.json();
        return result;
    } catch (error) {
        console.error(error.message);
        throw new Error(`Error al actualizar la solicitud con ID ${id}`);
    }
};

export {registrarSolicitud, obtenerSolicitudes, obtenerSolicitudPorId, actualizarSolicitud}