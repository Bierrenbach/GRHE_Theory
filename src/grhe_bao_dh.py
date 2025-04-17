import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("docs/figures", exist_ok=True)
os.makedirs("data/bao_data", exist_ok=True)

desi_data = {
    "z": [0.510, 0.706, 0.930, 1.317, 1.491, 2.330],
    "D_H_r_d": [20.98334647, 20.07872919, 21.70841761, 23.722285, 20.07217182, 8.52256583],
    "D_H_r_d_grhe": [20.70715467, 19.81438789, 21.42272731, 23.64132205, 25.72931632, 8.40961023]
}

df = pd.DataFrame(desi_data)
z = df["z"].values
camb_values = df["D_H_r_d"].values
grhe_values = df["D_H_r_d_grhe"].values

# GRHE interpolation
z_smooth = np.linspace(min(z), max(z), 100)
grhe_smooth = np.interp(z_smooth, z, grhe_values)

# Calculate MAPE
mape = np.mean(np.abs((camb_values - grhe_values) / (camb_values + 0.1))) * 100
print(f"MAPE for D_H/r_d: {mape:.2f}%")

plt.scatter(z, camb_values, color="yellow", label="DESI DR2")
plt.plot(z_smooth, grhe_smooth, "r--", label="GRHE")
plt.title("GRHE vs DESI DR2: D_H/r_d")
plt.xlabel("Redshift (z)")
plt.ylabel("D_H/r_d")
plt.legend()
plt.grid(True)
plt.savefig("docs/figures/grhe_bao_dh.png")
plt.close()

try:
    df.to_csv("data/bao_data/desi_dr2_bao_dh.csv", index=False)
    print("CSV file 'desi_dr2_bao_dh.csv' saved successfully in data/bao_data/")
except Exception as e:
    print(f"Error saving CSV: {e}")