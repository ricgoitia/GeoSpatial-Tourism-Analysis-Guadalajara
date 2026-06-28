import folium
import pandas as pd
import numpy as np
from folium.plugins import MarkerCluster, HeatMap

# ============================
# 1. Generar conjunto de datos
# ============================

np.random.seed(42)

num_puntos = 40

data = pd.DataFrame({
    "Lugar": [f"Punto turístico {i+1}" for i in range(num_puntos)],
    "Latitud": np.random.uniform(20.63, 20.72, num_puntos),   # Guadalajara
    "Longitud": np.random.uniform(-103.40, -103.30, num_puntos),
    "Visitantes": np.random.randint(50, 500, num_puntos),
    "Calificacion": np.round(np.random.uniform(2.5, 5.0, num_puntos), 2),
    "Tipo": np.random.choice(
        ["Museo", "Parque", "Restaurante", "Monumento", "Centro cultural"],
        num_puntos
    )
})

print(data.head())

# =========================
# 2. Crear mapa base
# =========================

mapa = folium.Map(
    location=[20.67, -103.35],
    zoom_start=13
)

# ==================================
# 3. Agregar marcadores interactivos
# ==================================

cluster = MarkerCluster().add_to(mapa)

for _, row in data.iterrows():

    if row["Calificacion"] >= 4.3:
        color = "green"
    elif row["Calificacion"] >= 3.5:
        color = "orange"
    else:
        color = "red"

    popup_text = f"""
    <b>{row['Lugar']}</b><br>
    Tipo: {row['Tipo']}<br>
    Visitantes: {row['Visitantes']}<br>
    Calificación: {row['Calificacion']}
    """

    folium.CircleMarker(
        location=[row["Latitud"], row["Longitud"]],
        radius=row["Visitantes"] / 50,
        color=color,
        fill=True,
        fill_opacity=0.7,
        popup=folium.Popup(popup_text, max_width=250)
    ).add_to(cluster)

# =========================
# 4. Agregar mapa de calor
# =========================

heat_data = data[["Latitud", "Longitud", "Visitantes"]].values.tolist()

HeatMap(
    heat_data,
    radius=20,
    blur=15
).add_to(mapa)

# =========================
# 5. Guardar mapa interactivo
# =========================

mapa.save("mapa_turismo_guadalajara.html")

mapa
