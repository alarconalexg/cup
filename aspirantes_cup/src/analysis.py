"""Gráficos y modelo sustituto. Requiere pandas, matplotlib, scikit-learn."""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

D = Path(__file__).resolve().parent.parent / "data"
races = pd.read_csv(D / "races.csv")
stats = pd.read_csv(D / "car_stats.csv")
df = races.merge(stats, on="race_no").merge(pd.read_csv(D / "strategy.csv"), on="race_no")
done = df.dropna(subset=["position"])
print(f"Carreras con resultado: {len(done)}")

attrs = ["speed", "acceleration", "aero", "handling", "braking",
         "reliability", "tyre_management", "wet_weather", "overtaking", "consistency"]

if len(done) >= 3:
    done.plot(x="race_no", y="position", marker="o", title="Posición por carrera")
    plt.gca().invert_yaxis()
    plt.savefig(D.parent / "posicion.png")

if len(done) >= 10:
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.inspection import permutation_importance
    X = done[attrs + ["laps", "tyre_wear", "w_speed", "w_accel", "w_aero", "w_handling", "w_braking"]]
    y = done["position"]
    m = GradientBoostingRegressor().fit(X, y)
    imp = permutation_importance(m, X, y, n_repeats=20, random_state=0)
    pd.Series(imp.importances_mean, index=X.columns).sort_values().plot.barh(title="Importancia de variables")
    plt.tight_layout(); plt.savefig(D.parent / "importancia.png")
else:
    print("Aún pocos datos: sigue añadiendo carreras y prácticas.")
