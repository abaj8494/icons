#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def main():
    # ---------------------------------------------------
    # 1) Set up the domain: x, y in [-4, 4]
    # ---------------------------------------------------
    n_points = 401
    x_vals = np.linspace(-4, 4, n_points)
    y_vals = np.linspace(-4, 4, n_points)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Create complex grid and avoid log(0) by masking
    Z = X + 1j * Y
    zero_mask = (X == 0) & (Y == 0)
    Z[zero_mask] = np.nan

    # Compute complex log
    with np.errstate(divide='ignore', invalid='ignore'):
        Z_ln = np.log(Z)

    # Extract components
    ln_real = np.real(Z_ln)
    ln_imag = np.imag(Z_ln)
    ln_abs  = np.abs(Z_ln)

    # Number of discrete color bands
    n_levels = 12

    # ---------------------------------------------------
    # 2) Real part with Inferno (discrete)
    # ---------------------------------------------------
    fig_re, ax_re = plt.subplots(figsize=(5, 5), dpi=100)
    ax_re.contourf(X, Y, ln_real, levels=n_levels, cmap='inferno')
    # Remove axes, labels, ticks, etc.
    ax_re.set_aspect('equal', 'box')
    ax_re.axis('off')

    fig_re.savefig('real_inferno.svg', format='svg', bbox_inches='tight', pad_inches=0)
    plt.close(fig_re)

    # ---------------------------------------------------
    # 3) Absolute value with hsv (discrete)
    # ---------------------------------------------------
    fig_abs, ax_abs = plt.subplots(figsize=(5, 5), dpi=100)
    ax_abs.contourf(X, Y, ln_abs, levels=n_levels, cmap='hsv')
    ax_abs.set_aspect('equal', 'box')
    ax_abs.axis('off')

    fig_abs.savefig('abs_hsv.svg', format='svg', bbox_inches='tight', pad_inches=0)
    plt.close(fig_abs)

    # ---------------------------------------------------
    # 4) Imag part with jet (discrete)
    # ---------------------------------------------------
    fig_im, ax_im = plt.subplots(figsize=(5, 5), dpi=100)
    ax_im.contourf(X, Y, ln_imag, levels=n_levels, cmap='jet')
    ax_im.set_aspect('equal', 'box')
    ax_im.axis('off')

    fig_im.savefig('imag_jet.svg', format='svg', bbox_inches='tight', pad_inches=0)
    plt.close(fig_im)

if __name__ == "__main__":
    main()

