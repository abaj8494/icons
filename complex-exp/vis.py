import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
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

def plot_imaginary_exp(cmap='RdYlBu_r', output_file=None, resolution=1001, singularity_size=0.01):
    """
    Plot the imaginary component of exp(1/z) using the specified colormap.
    
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
    imag_part = np.imag(W)
    imag_part = np.clip(imag_part, -2, 2)

    # Create minimal plot
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    im = ax.imshow(
        imag_part,
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

def plot_absolute_exp(cmap='hsv', output_file=None, resolution=1001, singularity_size=0.01):
    """
    Plot the absolute value of exp(1/z) using the specified colormap.
    The color represents the argument (phase) of the complex number.
    
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
    abs_val = np.abs(W)
    arg_val = np.angle(W, deg=True)
    
    # Normalize absolute value for better visualization
    abs_val = np.clip(abs_val, 0, 2)

    # Create minimal plot
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    
    # Plot the absolute value with phase coloring
    im = ax.imshow(
        abs_val,  # Use absolute value for the data
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
    """Main function to handle command line arguments and create the plots."""
    parser = argparse.ArgumentParser(
        description='Visualize various components of exp(1/z) with customizable colormap.',
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
        '--output-prefix',
        type=str,
        default=None,
        help='Prefix for output SVG files. If not provided, displays the plots instead.'
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
    
    # Generate all three visualizations
    if args.output_prefix:
        real_output = f"{args.output_prefix}_real.svg"
        imag_output = f"{args.output_prefix}_imag.svg"
        abs_output = f"{args.output_prefix}_abs.svg"
    else:
        real_output = None
        imag_output = None
        abs_output = None
    
    # Plot real part
    plot_complex_exp(args.cmap, real_output, args.resolution, args.singularity_size)
    
    # Plot imaginary part
    plot_imaginary_exp(args.cmap, imag_output, args.resolution, args.singularity_size)
    
    # Plot absolute value with the same colormap as the others
    plot_absolute_exp(args.cmap, abs_output, args.resolution, args.singularity_size)

if __name__ == '__main__':
    main() 