from zeep import Client, exceptions
from zeep.transports import Transport
from requests import Session

def setup_client():
    session = Session()
    session.headers.update({'apikey': 'TokenApi eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJCT0xJVklBTkZPT0QiLCJjb2RpZ29TaXN0ZW1hIjoiN0M0OEY3NkRBRkU0RjIwOUI5RDBENjYiLCJuaXQiOiJINHNJQUFBQUFBQUFBRE0yTVRHd05ETXdNZ0VBREF1Nk9Ra0FBQUE9IiwiaWQiOjYzNTMzOCwiZXhwIjoxNzE0NTA4NjEwLCJpYXQiOjE3MTIxMDM3ODAsIm5pdERlbGVnYWRvIjozNDQwOTYwMjQsInN1YnNpc3RlbWEiOiJTRkUifQ.yIsBJYDEzKGbB6POGh79Ov1V_ENAYQMRluz8gtfmwKHuppTwcWAs9Mpe8QBrEYEkP05JJYSfWbhx1tFWCuBLKw'})  # Usa tu token real aquí
    transport = Transport(session=session)
    wsdl_url = 'https://pilotosiatservicios.impuestos.gob.bo/v2/FacturacionCodigos?wsdl'
    client = Client(wsdl=wsdl_url, transport=transport)
    return client

def get_cufd(client, cuis, nit):
    data = {
        "SolicitudCufd": {
            "codigoAmbiente": 2,
            "codigoModalidad": 1,
            "codigoPuntoVenta": 0,
            "codigoSistema": "7C48F76DAFE4F209B9D0D66",
            "codigoSucursal": 0,
            "cuis": cuis,
            "nit": nit
        }
    }
    try:
        response = client.service.cufd(**data)
        handle_cufd_response(response)
    except exceptions.Fault as fault:
        print("SOAP Fault occurred:", fault)
    except Exception as e:
        print("An error occurred:", e)

def handle_cufd_response(response):
    if getattr(response, 'transaccion', False):
        print("CUFD se ha generado exitosamente:")
        print("Código CUFD:", getattr(response, 'codigo', 'No disponible'))
        print("Código de Control:", getattr(response, 'codigoControl', 'No disponible'))
        print("Dirección:", getattr(response, 'direccion', 'No disponible'))
        print("Fecha de Vigencia:", getattr(response, 'fechaVigencia', 'No disponible'))
    else:
        print("No se pudo generar el CUFD. Verificar los detalles del error.")

def main():
    client = setup_client()
    cuis = "ECD914AC"  # Suponiendo que este es el CUIS vigente
    nit = 344096024    # NIT del emisor
    get_cufd(client, cuis, nit)

if __name__ == "__main__":
    main()

