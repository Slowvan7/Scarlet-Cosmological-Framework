

#!/usr/bin/env python3

"""
Scarlet 2.0 — Torsional Cosmology Solver (Stiff + Normalized Version)

Improvements over previous version:
- Uses stiff ODE solver (BDF)
- Normalizes torsion density to a dimensionless fractional form
- Improves numerical stability for large relaxation rates
- Maintains torsional damping proportional to density
"""

import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.integrate import solve_ivp


# --------------------------------------------------
# Cosmological constants (Planck baseline)
# --------------------------------------------------

H0_KM = 67.4                  # km/s/Mpc
MPC_TO_KM = 3.0857e19
H0 = H0_KM / MPC_TO_KM        # convert to 1/s

OMEGA_M = 0.315
OMEGA_L = 0.685


# --------------------------------------------------
# Hubble function
# --------------------------------------------------

def H(z):
    """Hubble parameter in 1/s"""
    return H0 * np.sqrt(OMEGA_M * (1 + z)**3 + OMEGA_L)


# --------------------------------------------------
# Torsion evolution equation (normalized form)
# --------------------------------------------------

def d_rho_dz(z, rho, mode_ratio, t_v):
    """
    Evolution equation in redshift space:

        dρ/dz = [3(1+w)ρ + (Γ/H)ρ] / (1+z)

    where:
        w = -mode_ratio
        Γ = 1 / t_v

    This version evolves a normalized torsion density.
    """

    rho = rho[0]

    # Prevent unphysical negative or extreme values
    rho = np.clip(rho, 0.0, 1.0)

    Hz = H(z)

    w = -mode_ratio
    Gamma = 1.0 / t_v

    # Dimensionless damping factor
    damping = (Gamma / Hz) * rho

    drho_dz = (3 * (1 + w) * rho + damping) / (1 + z)

    return [drho_dz]


# --------------------------------------------------
# Solver
# --------------------------------------------------

def solve_torsion(mode_ratio, t_v, z_initial):
    """
    Solve torsion evolution from z_initial → 0
    using a stiff solver for numerical stability.
    """

    if z_initial <= 0:
        raise ValueError("Initial redshift must be > 0")

    z_span = (z_initial, 0)
    z_eval = np.linspace(z_initial, 0, 300)

    # Normalized initial condition (dimensionless fraction)
    rho_init = [1e-5]

    solution = solve_ivp(
        d_rho_dz,
        z_span,
        rho_init,
        t_eval=z_eval,
        args=(mode_ratio, t_v),
        method="BDF",   # <-- stiff solver
        rtol=1e-8,
        atol=1e-10
    )

    if not solution.success:
        raise RuntimeError("ODE solver failed to converge")

    return solution.t, solution.y[0]


# --------------------------------------------------
# Derived observables
# --------------------------------------------------

def compute_h0(rho):
    """
    H0 correction (phenomenological mapping)
    """
    return H0_KM * (1 + 0.1 * rho)


def compute_s8(rho):
    """
    S8 suppression (phenomenological mapping)
    """
    S8_BASE = 0.83
    return S8_BASE * np.exp(-50 * rho)


# --------------------------------------------------
# Main execution
# --------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Scarlet torsion solver (stiff version)")

    parser.add_argument("--ratio", type=float, required=True, help="Mode ratio")
    parser.add_argument("--t_v", type=float, required=True, help="Relaxation time (s)")
    parser.add_argument("--zf", type=float, required=True, help="Initial redshift")

    args = parser.parse_args()

    print("\n--- Scarlet 2.0 Solver (Stiff + Normalized) ---")
    print("Mode ratio:", args.ratio)
    print("Relaxation time:", args.t_v)
    print("Initial redshift:", args.zf)

    os.makedirs("results", exist_ok=True)

    # Solve torsion evolution
    z, rho = solve_torsion(args.ratio, args.t_v, args.zf)

    # Derived observables
    h0 = compute_h0(rho)
    s8 = compute_s8(rho)

    # Save results
    df = pd.DataFrame({
        "redshift": z,
        "torsion_density": rho,
        "H0_corrected": h0,
        "S8": s8
    })

    df.to_csv("results/scarlet_torsion_results.csv", index=False)

    # Plot S8 suppression
    plt.figure()
    plt.plot(z, s8)
    plt.xlabel("Redshift")
    plt.ylabel("S8")
    plt.title("Scarlet 2.0 — Torsional Suppression (Stiff Solver)")
    plt.savefig("results/s8_suppression.png")

    print("\nResults saved to /results")
    print("Run complete.\n")


# --------------------------------------------------

if __name__ == "__main__":
    main()
