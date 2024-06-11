let tecnicos = []

function listarTecnicos() {
    let url = "/listarTecnicos/"
    fetch(url, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        }
    })
        .then(respuesta => respuesta.json())
        .then(resultado => {
            tecnicos = JSON.parse(resultado.tecnicos)
            console.log(tecnicos)
        })
        .catch(error => {
            console.error(error)
        })

}

function agregarIdCaso(id) {
    document.getElementById('idCaso').value = id
}

/**
 * A partir de la selección de una 
 * imagen en el control fileFoto del
 * formulario, se obtiene la url para
 * poder mostrarlo en un control tipo
 * IMG
 * @param {*} evento 
 */
function mostrarImagen(evento) {
    const archivos = evento.target.files
    const archivo = archivos[0]
    const url = URL.createObjectURL(archivo)
    const imagen = document.getElementById('imagenMostrar')
    imagen.setAttribute('src', url)
}

