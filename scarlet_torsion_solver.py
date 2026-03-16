#!/usr/bin/env python3

import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --------------------------------------------
# Cosmology baseline parameters
# --------------------------------------------

H0_LCDM = 67.4        # km/s/Mpc baseline Planck value
Omega_m = 0.315
Omega_lambda = 0.685

# --------------------------------------------
# Torsion evolution equation
# dρ_tors/dt + 3H(1+w)ρ_tors = -Γ
# --------------------------------------------

def torsion_evolution(z, rho_tors, mode_ratio, t_v):
   H = H0_LCDM * np.sqrt(Omega_m * (1+z)**3 + Omega_lambda)

   # Effective equation-of-state for torsion
   w_eff = -1 + (1 - mode_ratio)

   # decay constant tied to relaxation time
   Gamma = 1.0 / t_v

   drho_dz = -(3 * (1 + w_eff) * rho_tors) + (Gamma * 1e-50)

   return drho_dz


# --------------------------------------------
# Solve torsion density evolution
# --------------------------------------------

def solve_torsion(mode_ratio, t_v, z_max):

   z_span = (0, z_max)
   z_eval = np.linspace(0, z_max, 200)

   rho0 = [1e-5]

   sol = solve_ivp(
       torsion_evolution,
       z_span,
       rho0,
       t_eval=z_eval,
       args=(mode_ratio, t_v),
       method="RK45"
   )

   return sol.t, sol.y[0]


# --------------------------------------------
# Compute H0 correction
# --------------------------------------------

def compute_h0_shift(rho_tors):

   # simple scaling relation
   correction = rho_tors * 0.1
   h0_values = H0_LCDM * (1 + correction)

   return h0_values


# --------------------------------------------
# Compute S8 suppression curve
# --------------------------------------------

def compute_s8_suppression(z, rho_tors):

   s8_base = 0.83
   suppression = np.exp(-rho_tors * 50)

   s8 = s8_base * suppression

   return s8


# --------------------------------------------
# Main pipeline
# --------------------------------------------

def main():

   parser = argparse.ArgumentParser()
   parser.add_argument("--ratio", type=float, required=True)
   parser.add_argument("--t_v", type=float, required=True)
   parser.add_argument("--zf", type=float, required=True)

   args = parser.parse_args()

   mode_ratio = args.ratio
   t_v = args.t_v
   zf = args.zf

   print("Running Scarlet torsion solver...")
   print("Mode ratio:", mode_ratio)
   print("Relaxation time:", t_v)

   z, rho_tors = solve_torsion(mode_ratio, t_v, zf)

   h0 = compute_h0_shift(rho_tors)
   s8 = compute_s8_suppression(z, rho_tors)

   # ----------------------------------------
   # Save H0 correction
   # ----------------------------------------

   df = pd.DataFrame({
       "redshift": z,
       "torsion_density": rho_tors,
       "H0_corrected": h0
   })

   df.to_csv("results/h0_correction.csv", index=False)

   # ----------------------------------------
   # Plot S8 suppression
   # ----------------------------------------

   plt.figure()
   plt.plot(z, s8)
   plt.xlabel("Redshift")
   plt.ylabel("S8")
   plt.title("Scarlet 2.0 Torsional Suppression")
   plt.savefig("results/s8_suppression_curve.png")

   print("Outputs written to results/")


if __name__ == "__main__":
   main()
