import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

def get_available_colormaps():
    """Returns a list of all available colormaps in matplotlib."""
    return plt.colormaps()

def exp_inv_complex(Z):
    """Compute exp(1/z) for a complex array Z."""
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.exp(1 / Z)

def plot_complex_exp(cmap='RdYlBu_r', output_file=None, resolution=1001, singularity_size=0.01):
    """
    Plot the real component of exp(1/z) using the specified colormap.
    
    Args:
        cmap (str): Name of the matplotlib colormap to use.
                   Must be one of the available matplotlib colormaps.
        output_file (str, optional): Path to save the SVG file.
                                   If None, displays the plot instead.
        resolution (int): Number of points in each dimension. Higher values give better detail.
        singularity_size (float): Radius around z=0 to mask for the singularity.
    """
    # Generate grid points with high resolution
    x_vals = np.linspace(-1, 1, resolution)
    y_vals = np.linspace(-1, 1, resolution)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Create complex grid Z = X + iY with smaller singularity
    Z = X + 1j * Y
    Z[np.abs(Z) < singularity_size] = np.nan

    # Compute exp(1/Z)
    W = exp_inv_complex(Z)
    real_part = np.real(W)
    real_part = np.clip(real_part, -2, 2)

    # Create minimal plot
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    im = ax.imshow(
        real_part,
        extent=[-1, 1, -1, 1],
        cmap=cmap,
        origin='lower',
        aspect='equal',
        interpolation='bilinear'
    )
    
    # Remove all decorations
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    
    plt.tight_layout()
    
    if output_file:
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_file) if os.path.dirname(output_file) else '.', exist_ok=True)
        plt.savefig(output_file, format='svg', bbox_inches='tight', pad_inches=0)
        plt.close()
    else:
        plt.show()

def main():
    """Main function to handle command line arguments and create the plot."""
    parser = argparse.ArgumentParser(
        description='Visualize the real component of exp(1/z) with customizable colormap.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument(
        '--cmap',
        type=str,
        default='RdYlBu_r',
        choices=get_available_colormaps(),
        help='Matplotlib colormap to use for visualization'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default=None,
        help='Output SVG file path. If not provided, displays the plot instead.'
    )
    
    parser.add_argument(
        '--resolution',
        type=int,
        default=1001,
        help='Number of points in each dimension. Higher values give better detail.'
    )
    
    parser.add_argument(
        '--singularity-size',
        type=float,
        default=0.01,
        help='Radius around z=0 to mask for the singularity.'
    )
    
    args = parser.parse_args()
    plot_complex_exp(args.cmap, args.output, args.resolution, args.singularity_size)

if __name__ == '__main__':
    main() 