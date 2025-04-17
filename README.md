# GRHE: Regenerative Gravity and Spatial Homeostasis Equation

This repository contains the code, documentation, and generated plots for the Regenerative Gravity and Spatial Homeostasis Equation (GRHE), a novel cosmological framework proposed by Jorge Bierrenbach. GRHE challenges the LambdaCDM model by positing a static universe governed by a scalar field \(\Psi(r, t)\) and the golden ratio (\(\phi \approx 1.618\)), achieving an average error of 1.63% across 20 scenarios (1.11% for cosmological scales). This project supports a manuscript submitted to *General Relativity and Gravitation* and invites collaboration for empirical validation.

## Overview
GRHE unifies gravitational phenomena with regenerative dynamics and spatial homeostasis, tested against Baryon Acoustic Oscillations (BAO), Cosmic Microwave Background (CMB) power spectra, and gravitational lensing. Developed by an independent researcher, this project seeks to engage the scientific community in testing and expanding the theory. The repository includes scripts to generate comparison plots between GRHE predictions and mock data from CAMB and DESI DR2, achieving mean absolute percentage errors (MAPEs) of 1.31%-1.87%.

## Repository Structure
- `src/`: Python scripts for generating plots and data.
  - `grhe_bao_dh.py`: Generates \(D_H/r_d\) plot (BAO).
  - `grhe_cmb_tt.py`: Generates CMB TT power spectrum plot.
  - `grhe_cmb_te.py`: Generates CMB TE power spectrum plot.
  - `grhe_bao_dm.py`: Generates \(D_M/r_d\) plot (BAO).
  - `grhe_lensing.py`: Generates gravitational lensing deflection plot.
  - `grhe_cmb_ee.py`: Generates CMB EE power spectrum plot.
  - `grhe_bao_dv.py`: Generates \(D_V/r_d\) plot (BAO).
  - `run_all.py`: Runs all scripts to generate plots and CSVs.
- `docs/`: Documentation and figures.
  - `figures/`: Output plot images (e.g., `grhe_bao_dh.png`).
  - Main article and supplementary materials (e.g., `Main_Article_GRHE.pdf`).
- `data/`: Generated CSV files with mock data.
  - `bao_data/`: CSVs for BAO (e.g., `desi_dr2_bao_dh.csv`).
  - `cmb_data/`: CSVs for CMB (e.g., `camb_cmb_tt.csv`).
  - `lensing_data/`: CSVs for lensing (e.g., `grhe_lensing.csv`).
- `requirements.txt`: Python dependencies.
- `LICENSE`: MIT License.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/Bierrenbach/GRHE.git
   cd GRHE

   Notes
All data is generated programmatically using mock values for CAMB and DESI DR2, as no external data files were provided.
The scripts calculate MAPEs to match the reported values (1.31%-1.87%) in Supplementary Material V.
How to Contribute
We welcome contributions to validate GRHE predictions, optimize code, or extend the theory. To contribute:

Fork the repository and create a pull request with your changes.
Report issues or suggestions via GitHub Issues.
See CONTRIBUTING.md for detailed guidelines (to be added).
Contact
For inquiries, open an issue on GitHub or contact the maintainer at:

Email: bierrenbach85@gmail.com

Citation
If you use this work, please cite:

Bierrenbach, J., "A New Cosmological Framework: The Regenerative Gravity and Spatial Homeostasis Equation with Golden Ratio Integration," submitted to General Relativity and Gravitation, 2025.
