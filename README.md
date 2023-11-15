# Pruebas Automatizadas con Selenium y unittest

Este conjunto de pruebas automatizadas utiliza Selenium y el framework de pruebas unittest en Python para evaluar la funcionalidad de una calculadora de porcentajes en el sitio web "http://www.calculator.net/". Las pruebas están diseñadas para cubrir varios escenarios, incluyendo números positivos, negativos, decimales, valores extremos y situaciones donde ambos valores son cero.

## Configuración del Entorno

### Dependencias
- **Python 3.12**: Asegúrate de tener Python 3.12 instalado.
- **Selenium**: Puedes instalarlo usando el siguiente comando:
  ```bash
  pip install selenium
  ```
- **HtmlTestRunner**: Puedes instalarlo usando el siguiente comando:
  ```bash
  pip install html-testRunner
  ```
- **WebDriver para Chrome**: Asegúrate de tener el controlador (driver) de Chrome descargado y en tu PATH.

## Ejecutar las Pruebas

1. Clona o descarga este repositorio en tu máquina local.
2. Navega hasta el directorio que contiene el código fuente.
3. Ejecuta el siguiente comando en la línea de comandos para ejecutar las pruebas:
  ```bash
  python nombre_del_archivo.py -v
  ```

## Descripción de las Pruebas

### Prueba 1: Números Positivos
Se verifica que el porcentaje de dos números positivos se calcule correctamente.

### Prueba 2: Números Negativos
Se verifica que el porcentaje de un número negativo y uno positivo se calcule correctamente.

### Prueba 3: Números Decimales
Se verifica que el porcentaje de dos números decimales se calcule correctamente.

### Prueba 4: Valor Mínimo Permitido
Se verifica que el porcentaje con el valor mínimo permitido y un segundo valor se calcule correctamente.

### Prueba 5: Valor Máximo Permitido
Se verifica que el porcentaje con el valor máximo permitido y un segundo valor se calcule correctamente.

### Prueba 6: Valor Igual a 0
Se verifica que el porcentaje con un valor igual a 0 y otro valor se calcule correctamente.

### Prueba 7: Ambos Valores Igual a 0
Se verifica que el porcentaje con ambos valores igual a 0 se calcule correctamente.

## Informe de Ejecución de Pruebas

Después de ejecutar las pruebas, se generará un informe en formato HTML llamado "reporte_de_pruebas.html". Puedes abrir este informe en un navegador web para obtener detalles sobre la ejecución de cada prueba, incluyendo éxitos y fallos.

¡Contribuciones y mejoras son bienvenidas! Si encuentras problemas o tienes sugerencias, por favor, abre un problema o envía una solicitud de extracción.
!()[screenshots/last_test_result.png]

