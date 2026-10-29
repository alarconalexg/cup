"""Genera estrategias de seco viables para una carrera."""
import itertools
import pandas as pd

LIFE = {"S": 15, "M": 30, "H": 45}
WINDOW_FRAC = {"early": 0.33, "middle": 0.5, "late": 0.67}  # supuesto, calibrar

def candidates(laps, wear_mult=1.0, style_mult=1.0, max_stops=2):
    rows = []
    for n in range(1, max_stops + 2):
        for combo in itertools.product(LIFE, repeat=n):
            stint = laps / n  # reparto uniforme (aprox.)
            ok = all(LIFE[c] * wear_mult * style_mult >= stint for c in combo)
            margin = min(LIFE[c] * wear_mult * style_mult - stint for c in combo)
            rows.append({"strategy": "-".join(combo), "stops": n - 1,
                         "viable": ok, "min_margin_laps": round(margin, 1)})
    return pd.DataFrame(rows).sort_values(["viable", "min_margin_laps"], ascending=False)

if __name__ == "__main__":
    print(candidates(35).to_string(index=False))
