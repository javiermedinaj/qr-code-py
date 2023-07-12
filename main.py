import qrcode


def generar_qr(link, nombre_archivo):
    # Crea un objeto QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Agrega el enlace al objeto QRCode
    qr.add_data(link)
    qr.make(fit=True)

    # Crea una imagen QRCode
    imagen_qr = qr.make_image(fill_color="black", back_color="white")

    # Guarda la imagen QRCode en la carpeta raíz con el nombre de archivo especificado
    imagen_qr.save(nombre_archivo)


enlace = "https://javier-medina-portfolio.vercel.app/"
nombre_archivo = "codigo_qr.png"

generar_qr(enlace, nombre_archivo)
