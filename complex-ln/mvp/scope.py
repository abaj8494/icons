#!/usr/bin/env python3
"""
Generate three separate SVG images:
1) Re[ln(x + i y)]
2) Im[ln(x + i y)]
3) |ln(x + i y)|

All plotted over x,y in [-4,4], with discrete color bands.

Usage:
  python plot_ln_complex.py [--cmap CMAP]

Example:
  python plot_ln_complex.py --cmap rainbow

This will produce:
  real_part.svg,
  imag_part.svg,
  abs_part.svg
"""

import numpy as np
import matplotlib.pyplot as plt
import argparse

def main():
    # A list of common matplotlib colormaps you might try for discrete color blocks
    all_cmaps = [
        'rainbow', 'hsv', 'jet', 'plasma', 'inferno', 'magma',
        'cividis', 'viridis', 'turbo'
    ]

    parser = argparse.ArgumentParser(
        description="Generate discrete color-band plots for Re, Im, and |ln(x + i y)| over [-4,4]x[-4,4]."
    )
    parser.add_argument(
        '--cmap',
        type=str,
        default='rainbow',
        help=(
            "Colormap to use. Some options include:\n"
            f"{', '.join(all_cmaps)}\n"
            "For more, see: https://matplotlib.org/stable/tutorials/colors/colormaps.html"
        )
    )
    args = parser.parse_args()

    # ---------------------------------------------------
    # Domain: x,y in [-4,4]
    # We'll include 401 points per axis so that 0 is included.
    # ---------------------------------------------------
    n_points = 401
    x_vals = np.linspace(-4, 4, n_points)
    y_vals = np.linspace(-4, 4, n_points)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Avoid log(0) by masking out the point z=0
    Z = X + 1j * Y
    zero_mask = (X == 0) & (Y == 0)
    Z[zero_mask] = np.nan

    # Compute principal branch of the complex log
    with np.errstate(divide='ignore', invalid='ignore'):
        Z_ln = np.log(Z)

    # Extract real part, imaginary part, and magnitude
    ln_real = np.real(Z_ln)
    ln_imag = np.imag(Z_ln)
    ln_abs  = np.abs(Z_ln)

    # Decide how many discrete levels to use
    n_levels = 12  # Adjust if you want more or fewer color bands

    # ---------------------------------------------------
    # 1) Real part of ln(z)
    # ---------------------------------------------------
    fig_re, ax_re = plt.subplots(figsize=(6, 5), dpi=100)
    # For discrete color bands, use contourf with a fixed number of levels
    # letting Matplotlib pick the min/max automatically, or we can specify them
    cs_re = ax_re.contourf(
        X, Y, ln_real,
        levels=n_levels,
        cmap=args.cmap
    )
    ax_re.set_aspect('equal', 'box')
    ax_re.set_title(r"Re$[\ln(x + i y)]$")
    ax_re.set_xlabel("x")
    ax_re.set_ylabel("y")
    cbar_re = fig_re.colorbar(cs_re, ax=ax_re)
    cbar_re.set_label("Real part")
    fig_re.tight_layout()
    fig_re.savefig("real_part.svg", format="svg")
    plt.close(fig_re)

    # ---------------------------------------------------
    # 2) Imag part of ln(z)
    # ---------------------------------------------------
    fig_im, ax_im = plt.subplots(figsize=(6, 5), dpi=100)
    cs_im = ax_im.contourf(
        X, Y, ln_imag,
        levels=n_levels,
        cmap=args.cmap
    )
    ax_im.set_aspect('equal', 'box')
    ax_im.set_title(r"Im$[\ln(x + i y)]$")
    ax_im.set_xlabel("x")
    ax_im.set_ylabel("y")
    cbar_im = fig_im.colorbar(cs_im, ax=ax_im)
    cbar_im.set_label("Imag part")
    fig_im.tight_layout()
    fig_im.savefig("imag_part.svg", format="svg")
    plt.close(fig_im)

    # ---------------------------------------------------
    # 3) Absolute value of ln(z)
    # ---------------------------------------------------
    fig_abs, ax_abs = plt.subplots(figsize=(6, 5), dpi=100)
    cs_abs = ax_abs.contourf(
        X, Y, ln_abs,
        levels=n_levels,
        cmap=args.cmap
    )
    ax_abs.set_aspect('equal', 'box')
    ax_abs.set_title(r"$|\ln(x + i y)|$")
    ax_abs.set_xlabel("x")
    ax_abs.set_ylabel("y")
    cbar_abs = fig_abs.colorbar(cs_abs, ax=ax_abs)
    cbar_abs.set_label("Magnitude")
    fig_abs.tight_layout()
    fig_abs.savefig("abs_part.svg", format="svg")
    plt.close(fig_abs)


if __name__ == "__main__":
    main()

