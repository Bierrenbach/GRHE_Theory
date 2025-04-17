import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Create directories
os.makedirs("docs/figures", exist_ok=True)
os.makedirs("data/bao_data", exist_ok=True)

# DESI DR2 data from Supplementary Material V, Table S5.2
desi_data = {
    "z": [0.295],
    "D_V_r_d": [7.92512927],
    "D_V_r_d_grhe": [7.82000007]
}

df = pd.DataFrame(desi_data)
z = df["z"].values
camb_values = df["D_V_r_d"].values
grhe_values = df["D_V_r_d_grhe"].values

# Create extended data for GRHE line
z_extended = np.array([0.28, 0.31])  # Full range of x-axis
grhe_values_extended = np.array([7.82000007, 7.82000007])  # Constant line

# Calculate MAPE
mape = np.mean(np.abs((camb_values - grhe_values) / (camb_values + 0.1))) * 100
print(f"MAPE for D_V/r_d: {mape:.2f}%")

# Plot
plt.scatter(z, camb_values, color="yellow", label="DESI DR2")
plt.plot(z_extended, grhe_values_extended, "r--", label="GRHE", linewidth=3)
plt.title("GRHE vs DESI DR2: D_V/r_d")
plt.xlabel("Redshift (z)")
plt.ylabel("D_V/r_d")
plt.xlim(0.28, 0.31)
plt.ylim(7.8, 8.0)
plt.legend()
plt.grid(True)
plt.savefig("docs/figures/grhe_bao_dv.png")
plt.close()

# Save CSV
try:
    df.to_csv("data/bao_data/desi_dr2_bao_dv.csv", index=False)
    print("CSV file 'desi_dr2_bao_dv.csv' saved successfully in data/bao_data/")
except Exception as e:
    print(f"Error saving CSV: {e}")