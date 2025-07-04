
# ziat

Repositorio orientado a la integración de facturación electrónica utilizando el paquete Zeep para servicios SOAP.

## Descripción

Este proyecto, escrito principalmente en Python, facilita la emisión y gestión de comprobantes electrónicos. Incorpora Zeep como cliente SOAP, permitiendo la interoperabilidad con diversos servicios de facturación en línea y fuera de línea.

## Estructura principal

- `zeep/`: Módulos y utilidades para interactuar con servicios web SOAP usando Zeep.
- Soporte para integración modular y refactorización siguiendo buenas prácticas PEP8.
- Preparado para escenarios de operación online y offline.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/berprado/ziat.git
   cd ziat
   ```
2. Instala los requisitos:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Configura los parámetros de conexión a los servicios SOAP en los módulos correspondientes dentro de `zeep/`.
2. Lanza los scripts de emisión o consulta según la documentación interna.
3. Personaliza la lógica según los requerimientos de tu operación.

## Contribuciones

Las contribuciones para mejorar la modularidad, compatibilidad y documentación son bienvenidas. Por favor, sigue las convenciones de codificación y envía tus PRs a la rama principal.
