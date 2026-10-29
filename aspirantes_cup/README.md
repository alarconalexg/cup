# Aspirantes Cup: proyecto de modelado

Objetivo: entender cómo afectan atributos, estrategia y circuito al resultado en F1 Racer, y optimizar con ML.

## Estructura
- data/races.csv: una fila por carrera (ficha de /next + resultado)
- data/car_stats.csv: atributos antes de cada carrera y puntos gastados
- data/tyres.csv: duración base de compuestos y multiplicadores medidos
- data/practice_log.csv: salidas de /practice (pegar texto crudo + valores)
- data/strategy.csv: setup usado en cada carrera (/style, /pit)
- src/strategies.py: genera estrategias viables según vueltas y desgaste
- src/analysis.py: gráficos y modelo sustituto (se activa con >= 10 carreras)

## Flujo por carrera
1. /next -> añadir fila a races.csv
2. /stats -> añadir fila a car_stats.csv
3. /practice (máx. 3) -> practice_log.csv
4. /upgrade, /style, /pit -> strategy.csv
5. Tras la carrera, /standings -> completar position y points en races.csv
6. python src/analysis.py

## Codificación de la ficha de /next
Desgaste y atributos: 1 = 🔼, 0 = sin símbolo, -1 = 🔽.
(Pendiente de confirmar la leyenda: en Spa el desgaste 🔷 se tomó como 0.)
