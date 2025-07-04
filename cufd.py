from zeep import Client, exceptions
from zeep.transports import Transport
from requests import Session

def setup_client():
    """
    Configura y retorna un cliente SOAP para consumir los servicios de la
    administración tributaria boliviana (SIAT) utilizando autenticación por API Key.
    
    Returns:
        Client: Cliente configurado para el consumo de servicios web.
    """
    session = Session()
    session.headers.update({
        'apikey': 'TokenApi eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJCT0xJVklBTkZPT0QiLCJjb2RpZ29TaXN0ZW1hIjoiN0M0OEY3NkRBRkU0RjIwOUI5RDBENjYiLCJuaXQiOiJINHNJQUFBQUFBQUFB[...]'
    })
    transport = Transport(session=session)
    wsdl_url = 'https://pilotosiatservicios.impuestos.gob.bo/v2/FacturacionCodigos?wsdl'
    client = Client(wsdl=wsdl_url, transport=transport)
    return client

def get_cufd(client, cuis, nit):
    """
    Solicita un nuevo CUFD utilizando los datos proporcionados.

    Args:
        client (Client): Cliente SOAP configurado.
        cuis (str): Código único de identificación de sucursal.
        nit (int): Número de Identificación Tributaria del emisor.
    """
    data = {
        "SolicitudCufd": {
            "codigoAmbiente": 2,  # 2: ambiente de pruebas
            "codigoModalidad": 1, # 1: modalidad electrónica en línea
            "codigoPuntoVenta": 0, # 0: sin punto de venta
            "codigoSistema": "7C48F76DAFE4F209B9D0D66", # Código de sistema asignado
            "codigoSucursal": 0,   # 0: sucursal principal
            "cuis": cuis,
            "nit": nit
        }
    }
    try:
        response = client.service.cufd(**data)
        handle_cufd_response(response)
    except exceptions.Fault as fault:
        print("Ocurrió un error SOAP:", fault)
    except Exception as e:
        print("Ocurrió un error general:", e)

def handle_cufd_response(response):
    """
    Procesa la respuesta de la solicitud CUFD e imprime los resultados.

    Args:
        response (object): Respuesta devuelta por el servicio CUFD.
    """
    if getattr(response, 'transaccion', False):
        print("CUFD se ha generado exitosamente:")
        print("Código CUFD:", getattr(response, 'codigo', 'No disponible'))
        print("Código de Control:", getattr(response, 'codigoControl', 'No disponible'))
        print("Dirección:", getattr(response, 'direccion', 'No disponible'))
        print("Fecha de Vigencia:", getattr(response, 'fechaVigencia', 'No disponible'))
    else:
        print("No se pudo generar el CUFD. Verificar los detalles del error.")

def main():
    """
    Ejecución principal: configura el cliente, define parámetros y solicita el CUFD.
    """
    client = setup_client()
    cuis = "ECD914AC"  # CUIS vigente a utilizar
    nit = 344096024    # NIT del emisor
    get_cufd(client, cuis, nit)

if __name__ == "__main__":
    main()
