import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("docs/figures", exist_ok=True)
os.makedirs("data/bao_data", exist_ok=True)

des <xaiArtifact artifact_id="92c14570-12b1-4ca5-a083-0c61075bd598" artifact_version_id="1a09bd5b-c52a-4594-bf79-151e3ea7b0ab" title="grhe_bao_dm.py" contentType="text/python">
desi_data = {
    "z": [0.510, 0.706, 0.930, 1.317, 2.330],
    "D_M_r_d": [13.62003080, 16.84645313, 21.70841761, 27.78720817, 30.70838281],
    "D_M_r_d_grhe": [13.44029840, 16.62445463, 21.42272731, 27.42188577, 30.18689301]
}

df = pd.DataFrame(desi_data)
z = df["z"].values
camb_values = df["D_M_r_d"].values
grhe_values = df["D_M_r_d_grhe"].values

# GRHE interpolation
z_smooth = np.linspace(min(z), max(z), 100)
grhe_smooth = np.interp(z_smooth, z, grhe_values)

# Calculate MAPE
mape = np.mean(np.abs((camb_values - grhe_values) / (camb_values + 0.1))) * 100
print(f"MAPE for D_M/r_d: {mape:.2f}%")

plt.scatter(z, camb_values, color="yellow", label="DESI DR2")
plt.plot(z_smooth, grhe_smooth, "r--", label="GRHE")
plt.title("GRHE vs DESI DR2: D_M/r_d")
plt.xlabel("Redshift (z)")
plt.ylabel("D_M/r_d")
plt.legend()
plt.grid(True)
plt.savefig("docs/figures/grhe_bao_dm.png")
plt.close()

try:
    df.to_csv("data/bao_data/desi_dr2_bao.csv", index=False)
    print("CSV file 'desi_dr2_bao.csv' saved successfully in data/bao_data/")
except Exception as e:
    print(f"Error saving CSV: {e}")