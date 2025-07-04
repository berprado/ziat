from zeep import Client, exceptions
from zeep.transports import Transport
from requests import Session

def setup_client():
    """
    Configura y retorna un cliente SOAP para consumir los servicios de la 
    administración tributaria boliviana (SIAT), utilizando autenticación por API Key.

    Returns:
        zeep.Client: Cliente configurado para el consumo de servicios web.
    """
    session = Session()
    session.headers.update({
        'apikey': 'TokenApi eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJCT0xJVklBTkZPT0QiLCJjb2RpZ29TaXN0ZW1hIjoiN0M0OEY3NkRBRkU0RjIwOUI5RDBENjYiLCJuaXQiOiJINHNJQUFBQUFBQUFBRE0yTVRHd05ETXdNZ0VBREF1Nk9Ra0FBQUE9IiwiaWQiOjYzNTMzOCwiZXhwIjoxNzE0NTA4NjEwLCJpYXQiOjE3MTIxMDM3ODAsIm5pdERlbGVnYWRvIjozNDQwOTYwMjQsInN1YnNpc3RlbWEiOiJTRkUifQ.yIsBJYDEzKGbB6POGh79Ov1V_ENAYQMRluz8gtfmwKHuppTwcWAs9Mpe8QBrEYEkP05JJYSfWbhx1tFWCuBLKw'
    })  # Usa tu token real aquí
    transport = Transport(session=session)
    wsdl_url = 'https://pilotosiatservicios.impuestos.gob.bo/v2/FacturacionCodigos?wsdl'
    client = Client(wsdl=wsdl_url, transport=transport)
    return client

def get_cuis(client, nit):
    """
    Solicita un nuevo CUIS usando el cliente configurado y el NIT del emisor.

    Args:
        client (zeep.Client): Cliente SOAP configurado.
        nit (int): Número de Identificación Tributaria del emisor.
    """
    data = {
        "SolicitudCuis": {
            "codigoAmbiente": 2,       # 2 = Pruebas
            "codigoModalidad": 1,      # 1 = Electrónica en línea
            "codigoPuntoVenta": 0,     # 0 = Sin punto de venta
            "codigoSistema": "7C48F76DAFE4F209B9D0D66", # Código de sistema asignado
            "codigoSucursal": 0,       # 0 = Casa matriz
            "nit": nit
        }
    }
    try:
        response = client.service.cuis(**data)
        handle_cuis_response(response)
    except exceptions.Fault as fault:
        print("Ocurrió un error SOAP:", fault)
    except Exception as e:
        print("Ocurrió un error general:", e)

def handle_cuis_response(response):
    """
    Procesa la respuesta de la solicitud CUIS y muestra los resultados por consola.

    Args:
        response (object): Respuesta devuelta por el servicio web de CUIS.
    """
    if getattr(response, 'transaccion', False):
        print("CUIS generado exitosamente:")
        print("Código CUIS:", getattr(response, 'codigo', 'No disponible'))
        print("Fecha de Vigencia:", getattr(response, 'fechaVigencia', 'No disponible'))
    else:
        print("No se pudo generar el CUIS. Verificar los detalles del error.")
        if hasattr(response, 'mensajesList'):
            for mensaje in response.mensajesList:
                print(f"Código mensaje: {mensaje.codigo}, Descripción: {mensaje.descripcion}")

def main():
    """
    Ejecución principal: configura el cliente, define el NIT y solicita el CUIS.
    """
    client = setup_client()
    nit = 344096024  # NIT del emisor
    get_cuis(client, nit)

if __name__ == "__main__":
    main()
