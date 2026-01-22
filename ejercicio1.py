import requests
import json
from datetime import datetime

URL = "https://1xbet.pe/service/LineFeed/Get1x2_VZip?champs=88637&count=25&lng=es&mode=4&country=145&partner=368&getEmpty=true&virtualSports=true"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

print("Obteniendo cuotas de Premier League...\n")

response = requests.get(URL, headers=HEADERS)
response.raise_for_status()
data = response.json()

partidos = []

# ================== EXTRACCIÓN ==================
for item in data.get("Value", []):

    local = item.get("O1")
    visitante = item.get("O2")

    # Filtros de seguridad
    if not local or not visitante:
        continue
    if local == "Locales" and visitante == "Visitantes":
        continue

    # Fecha
    timestamp = item.get("S")
    fecha = datetime.fromtimestamp(timestamp) if timestamp else None

    cuota_1 = None
    cuota_x = None
    cuota_2 = None
    over_25 = None
    under_25 = None
    btts_si = None
    btts_no = None

    # --------- MERCADOS EN E ---------
    for op in item.get("E", []):

        if not isinstance(op, dict):
            continue

        g = op.get("G")
        t = op.get("T")
        c = op.get("C")
        p = op.get("P")

        # 🟢 1X2
        if g == 1:
            if t == 1:
                cuota_1 = c
            elif t == 2:
                cuota_x = c
            elif t == 3:
                cuota_2 = c

        # 🟢 Over / Under 2.5
        elif g == 4 and p == 2.5:
            if t == 9:
                over_25 = c
            elif t == 10:
                under_25 = c

        # 🟢 BTTS
        elif g == 21:
            if t == 180:
                btts_si = c
            elif t == 181:
                btts_no = c

    partidos.append({
        "local": local,
        "visitante": visitante,
        "fecha": fecha,
        "1": cuota_1,
        "X": cuota_x,
        "2": cuota_2,
        "over_25": over_25,
        "under_25": under_25,
        "btts_si": btts_si,
        "btts_no": btts_no
    })

# ================== SOLO 10 PARTIDOS ==================
partidos = partidos[:10]

# ================== GUARDAR JSON ==================
with open("output_partidos.json", "w", encoding="utf-8") as f:
    json.dump(partidos, f, ensure_ascii=False, indent=4, default=str)

# ================== OUTPUT ==================
print(f"Partidos guardados: {len(partidos)}")
print("Archivo generado: output_partidos.json\n")

for p in partidos:
    print(f"{p['local']} vs {p['visitante']}")
    print(f"Fecha: {p['fecha']}")
    print(f"1X2 -> 1: {p['1']} | X: {p['X']} | 2: {p['2']}")
    print(f"Over 2.5: {p['over_25']} | Under 2.5: {p['under_25']}")
    print(f"BTTS -> Sí: {p['btts_si']} | No: {p['btts_no']}")
    print("-" * 60)

print("Script finalizado correctamente.")
