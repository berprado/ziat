from zeep import Client

# URL del WSDL del servicio de la administración tributaria boliviana (SIAT).
# Este WSDL define los métodos disponibles para la interoperabilidad con el sistema de facturación electrónica.
wsdl_url = 'https://pilotosiatservicios.impuestos.gob.bo/v2/FacturacionCodigos?wsdl'

# Inicializa el cliente Zeep para consumir servicios SOAP definidos en el WSDL.
client = Client(wsdl_url)

# Imprime la lista de servicios disponibles, útil para explorar y conocer los métodos expuestos por el SIAT.
print(client.service)  # Debería mostrar los servicios disponibles
