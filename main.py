from zeep import Client
from zeep.transports import Transport
from requests import Session

# Configuración del transporte con autenticación usando API Key.
# Esto permite el acceso seguro a los servicios web de la administración tributaria (SIAT).
session = Session()
session.headers.update({
    'apikey': 'TokenApi eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJCT0xJVklBTkZPT0QiLCJjb2RpZ29TaXN0ZW1hIjoiN0M0OEY3NkRBRkU0RjIwOUI5RDBENjYiLCJuaXQiOiJINHNJQUFBQUFBQUFBRE0yTVRHd05ETXdNZ0VBREF1Nk9Ra0FBQUE9IiwiaWQiOjYzNTMzOCwiZXhwIjoxNzE0NTA4NjEwLCJpYXQiOjE3MTIxMDM3ODAsIm5pdERlbGVnYWRvIjozNDQwOTYwMjQsInN1YnNpc3RlbWEiOiJTRkUifQ.yIsBJYDEzKGbB6POGh79Ov1V_ENAYQMRluz8gtfmwKHuppTwcWAs9Mpe8QBrEYEkP05JJYSfWbhx1tFWCuBLKw'
})

transport = Transport(session=session)

# Inicialización del cliente Zeep apuntando al WSDL del servicio de Facturación de Códigos.
# Especifica el nombre del servicio y el puerto según la definición en el WSDL.
wsdl_url = 'https://pilotosiatservicios.impuestos.gob.bo/v2/FacturacionCodigos?wsdl=ServicioFacturacionCodigos.wsdl'
client = Client(
    wsdl=wsdl_url,
    transport=transport,
    service_name='ServicioFacturacionCodigos',
    port_name='ServicioFacturacionCodigosPort'
)

# Datos requeridos para la solicitud de CUIS.
data = {
    "SolicitudCuis": {
        "codigoAmbiente": 2,            # 2 = entorno de pruebas (ver documentación SIAT)
        "codigoModalidad": 1,           # 1 = modalidad electrónica en línea
        "codigoPuntoVenta": 0,          # 0 = sin punto de venta
        "codigoSistema": "7C48F76DAFE4F209B9D0D66",  # Código de sistema asignado por SIAT
        "codigoSucursal": 0,            # 0 = casa matriz
        "nit": 344096024                # NIT del contribuyente/emisor
    }
}

# Llamada al servicio web para obtener un CUIS (Código Único de Iniciación de Sistemas).
response = client.service.cuis(**data)

# Se imprime la respuesta recibida, que puede incluir el código CUIS y su vigencia.
print(response)
