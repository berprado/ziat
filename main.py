from zeep import Client
from zeep.transports import Transport
from requests import Session

# Configuración del transporte con autenticación si es necesario
session = Session()
session.headers.update({'apikey': 'TokenApi eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJCT0xJVklBTkZPT0QiLCJjb2RpZ29TaXN0ZW1hIjoiN0M0OEY3NkRBRkU0RjIwOUI5RDBENjYiLCJuaXQiOiJINHNJQUFBQUFBQUFBRE0yTVRHd05ETXdNZ0VBREF1Nk9Ra0FBQUE9IiwiaWQiOjYzNTMzOCwiZXhwIjoxNzE0NTA4NjEwLCJpYXQiOjE3MTIxMDM3ODAsIm5pdERlbGVnYWRvIjozNDQwOTYwMjQsInN1YnNpc3RlbWEiOiJTRkUifQ.yIsBJYDEzKGbB6POGh79Ov1V_ENAYQMRluz8gtfmwKHuppTwcWAs9Mpe8QBrEYEkP05JJYSfWbhx1tFWCuBLKw'})
transport = Transport(session=session)

# Cliente Zeep
wsdl = 'https://pilotosiatservicios.impuestos.gob.bo/v2/FacturacionCodigos?wsdl=ServicioFacturacionCodigos.wsdl'
client = Client(
    wsdl='https://pilotosiatservicios.impuestos.gob.bo/v2/FacturacionCodigos?wsdl=ServicioFacturacionCodigos.wsdl',
    transport=transport,
    service_name='ServicioFacturacionCodigos',
    port_name='ServicioFacturacionCodigosPort'
)


# Datos para la solicitud
data = {
    "SolicitudCuis": {
        "codigoAmbiente": 2,
        "codigoModalidad": 1,
        "codigoPuntoVenta": 0,
        "codigoSistema": "7C48F76DAFE4F209B9D0D66",
        "codigoSucursal": 0,
        "nit": 344096024
    }
}

# Llamada al servicio
response = client.service.cuis(**data)

print(response)

