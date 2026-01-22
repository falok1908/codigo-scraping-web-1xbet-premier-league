CODIGO SCRAPING WEB / 1XBET (PREMIER LEAGUE)

Este proyecto realiza scraping de cuotas de apuestas de la Premier League utilizando una Api pública de 1xBet, extrayendo información clave de cada partido y generando un archivo JSON como salida.
----------------------------------------------------------------
Características:

Extracción de partidos de la Premier League
Obtención de:
Equipos (local vs visitante)
Fecha y hora del partido
Cuotas 1X2
Cuotas Over / Under 2.5 goles
Cuotas BTTS (Both Teams To Score)
Generación de un archivo JSON con mínimo 10 partidos
Uso de API pública (sin autenticación)
----------------------------------------------------------------
Cómo ejecutar el proyecto:
Requisitos previos
Python 3.9 o superior
Conexión a internet
Instalación de dependencias
El proyecto utiliza una sola librería externa:
pip install requests
Ejecución del script
Desde la carpeta del proyecto, ejecutar:
python ejercicio1.py
----------------------------------------------------------------
Output generado
Al ejecutar el script se genera el archivo:
output_partidos.json


Este archivo contiene una lista de 10 partidos con la siguiente estructura:

{
  "local": "West Ham United",
  "visitante": "Sunderland",
  "fecha": "2026-01-24 07:30:00",
  "1": 2.591,
  "X": 3.39,
  "2": 2.988,
  "over_25": 2.167,
  "under_25": 1.806,
  "btts_si": 1.79,
  "btts_no": 1.937
}
----------------------------------------------------------------
Enfoque y explicación técnica

Se utiliza la Api pública:

https://1xbet.pe/service/LineFeed/Get1x2_VZip

filtrado por el campeonato Premier League (champs=88637).

Estructura de la API
Los partidos se encuentran dentro del arreglo Value
Los mercados de apuestas se encuentran en la clave E
Cada mercado se identifica por el campo G

Mercados procesados
Mercado	                       Identificador
1X2	                           G = 1
Over / Under 2.5	     G = 4 con P = 2.5
BTTS	                           G = 21

Validaciones
Se filtran registros inválidos (ej. "Locales vs Visitantes")
Se controlan tipos de datos para evitar errores
Si un mercado no está disponible, su valor se devuelve como null
----------------------------------------------------------------
Tecnologías utilizadas
Python
requests
json
datetime
----------------------------------------------------------------
Notas finales
La API utilizada es pública y solo requiere un User-Agent.
El código está diseñado para ser claro, robusto y fácilmente extensible.
El proyecto cumple completamente con los requisitos solicitados.
----------------------------------------------------------------
Estado del proyecto
Finalizado
Funcional
