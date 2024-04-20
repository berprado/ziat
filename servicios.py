from zeep import Client

wsdl_url = 'https://pilotosiatservicios.impuestos.gob.bo/v2/FacturacionCodigos?wsdl'
client = Client(wsdl_url)
print(client.service)  # Debería mostrar los servicios disponibles
