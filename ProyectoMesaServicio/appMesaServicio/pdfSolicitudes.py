from fpdf import FPDF
from datetime import datetime


class Pdf(FPDF):
    def header(self):
        # Logo
        self.image('media/logo-sena.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        self.ln()
        # Moverse a la derecha
        self.cell(60)
        # Titulo
        self.cell(80, 10, 'MESA DE SERVICIOS CTPI - CAUCA', 0, 0, 'C')
        self.ln()
        self.cell(60)
        self.cell(80, 10, 'REPORTE SOLICITUDES', 0, 0, 'C')
        # Salto de línea
        self.ln(30)

    # Page footer
    def footer(self):
        # Posición a 1.5 cm desde abajo
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Colocar número de página
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def mostrarDatos(self, solicitudes):
        # Colocar el texto fecha
        self.cell(30, 10, "Fecha: ")
        fecha = datetime.now()
        # colocar la fecha del día
        self.cell(40, 10, str(fecha.day) + "/" +
                  str(fecha.month) + "/" + str(fecha.year))
        self.ln()
        # crear encabezado de la tabla
        self.set_font("Arial", "B", 12)
        self.cell(40, 10, "Instructor", 1, 0, 'C')
        self.cell(100, 10, "Solicitud", 1, 0, 'C')
        self.cell(30, 10, "Ambiente", 1, 0, 'C')
        self.cell(20, 10, "Fecha", 1, 0, 'C')
        self.ln()
        # crear las filas de la tabla de acuerdo a los datos
        fila = 110
        self.set_font("Arial", "", 8)
        for solicitud in solicitudes:
            self.cell(40, 10, f"{solicitud.solUsuario.first_name} {
                      solicitud.solUsuario.last_name}", 1, 0, 'L')
            self.cell(100, 10, solicitud.solDescripcion, 1, 0, 'L')
            self.cell(30, 10, solicitud.solOficinaAmbiente.ofiNombre, 1, 0, 'L')
            self.cell(20, 10, str(solicitud.fechaHoraCreacion), 1, 0, 'C')
            self.ln()
            fila += 4
        self.ln()
        self.set_font("Arial", "B", 12)
        self.cell(200, 10, '_______________________________________', 0, 0, 'C')
        self.ln()
        self.cell(200, 10, 'Lider TIC CTPI', 0, 0, 'C')
