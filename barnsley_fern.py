"""
Barnsley Fern Fractal - A Mathematical Leaf Visualization

This script generates a beautiful leaf-like structure using the Barnsley Fern fractal.
The fern is created using an Iterated Function System (IFS) with four transformation
matrices that mimic the natural growth patterns of a fern leaf.

The four transformations represent:
1. Stem (1% probability)
2. Successively smaller leaflets (85% probability)
3. Largest left-hand leaflet (7% probability)  
4. Largest right-hand leaflet (7% probability)
"""

import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.colors import LinearSegmentedColormap

def barnsley_fern(num_points=25000):
    """
    Generate points for the Barnsley Fern fractal.
    
    Args:
        num_points (int): Number of points to generate (default: 25,000)
    
    Returns:
        tuple: Arrays of x and y coordinates
    """
    # Initialize arrays to store points
    x = np.zeros(num_points)
    y = np.zeros(num_points)
    
    # Starting point
    x[0], y[0] = 0, 0
    
    # Generate points using the four transformation matrices
    for i in range(1, num_points):
        # Get previous point
        prev_x, prev_y = x[i-1], y[i-1]
        
        # Random number to determine which transformation to use
        r = random.random()
        
        if r < 0.01:
            # Transformation 1: Stem (1% probability)
            # Matrix: a=0, b=0, c=0, d=0.25, e=0, f=0 (much taller stem)
            x[i] = 0 * prev_x + 0 * prev_y + 0          # a=0, b=0, e=0
            y[i] = 0 * prev_x + 0.25 * prev_y + 0       # c=0, d=0.25, f=0
        elif r < 0.86:
            # Transformation 2: Main leaflets (85% probability) - More curved
            # Matrix: a=0.80, b=0.08, c=-0.08, d=0.80, e=0, f=1.8
            x[i] = 0.80 * prev_x + 0.08 * prev_y + 0    # a=0.80, b=0.08, e=0
            y[i] = -0.08 * prev_x + 0.80 * prev_y + 1.8 # c=-0.08, d=0.80, f=1.8
        elif r < 0.93:
            # Transformation 3: Left leaflet (7% probability) - Much more pronounced
            # Matrix: a=0.30, b=-0.35, c=0.35, d=0.30, e=0, f=1.8
            x[i] = 0.30 * prev_x + (-0.35) * prev_y + 0  # a=0.30, b=-0.35, e=0
            y[i] = 0.35 * prev_x + 0.30 * prev_y + 1.8  # c=0.35, d=0.30, f=1.8
        else:
            # Transformation 4: Right leaflet (7% probability) - Much more pronounced
            # Matrix: a=-0.25, b=0.35, c=0.35, d=0.30, e=0, f=0.6
            x[i] = -0.25 * prev_x + 0.35 * prev_y + 0   # a=-0.25, b=0.35, e=0
            y[i] = 0.35 * prev_x + 0.30 * prev_y + 0.6 # c=0.35, d=0.30, f=0.6
    
    return x, y

def create_custom_colormap():
    """Create a custom black colormap for the fern."""
    colors = ["#000", '#000']  
    return LinearSegmentedColormap.from_list('fern_black', colors)

def visualize_fern(x, y, save_plot=True):
    """
    Visualize the Barnsley Fern fractal with proper axes.
    
    Args:
        x (array): X coordinates
        y (array): Y coordinates
        save_plot (bool): Whether to save the plot as an image
    """
    # Make the leaf smaller and position it within 0-3 x-axis range
    # Scale down the leaf to make it much smaller
    x_small = x * 0.15  # Make leaf much smaller in width
    y_small = y * 0.15  # Make leaf much smaller in height
    
    # Center the leaf within the 0-3 x-axis range
    # Shift x coordinates to center around x=1.5 (middle of 0-3 range)
    x_offset = 1.5
    y_offset = 0.5  # Small offset from bottom
    
    x_scaled = x_small + x_offset
    y_scaled = y_small + y_offset
    
    # Create figure with appropriate dimensions for 0-3 range
    plt.figure(figsize=(8, 6), dpi=150)
    
    # Create scatter plot with black points
    plt.scatter(x_scaled, y_scaled, s=1.0, c='black', alpha=0.9, edgecolors='none')
    
    # Customize the plot with proper axes
    # plt.title('Barnsley Fern Fractal - Small Leaf in 0-3 Coordinate System\n'
    #           f'{len(x):,} Points | Both axes: 0.0 to 3.0',
    #           fontsize=11, fontweight='bold', pad=12, color='black')
    
    plt.xlabel('X Coordinate (0 to 3)', fontsize=10, color='black', fontweight='bold')
    plt.ylabel('Y Coordinate (0 to 3)', fontsize=10, color='black', fontweight='bold')
    
    # Enable detailed grid for better readability
    plt.grid(True, alpha=0.4, linestyle='-', linewidth=0.4, color='gray')
    plt.grid(True, which='minor', alpha=0.2, linestyle=':', linewidth=0.2, color='lightgray')
    
    # Do NOT set equal aspect ratio to avoid rotation/distortion
    # plt.axis('equal')  # Commented out to prevent rotation
    
    # Show axes with proper styling
    plt.gca().spines['bottom'].set_color('black')
    plt.gca().spines['left'].set_color('black')
    plt.gca().spines['top'].set_color('black')
    plt.gca().spines['right'].set_color('black')
    
    # Set detailed tick parameters
    plt.tick_params(axis='both', which='major', labelsize=9, colors='black')
    plt.tick_params(axis='both', which='minor', labelsize=7, colors='gray')
    
    # Add major and minor ticks with detailed spacing
    plt.gca().tick_params(which='both', direction='in', top=True, right=True)
    
    # Create detailed coordinate system from 0 to 3 on both axes
    import numpy as np
    
    # Both X and Y axes: Major ticks every 0.1 from 0 to 3.0 (31 ticks)
    major_ticks = np.arange(0, 3.1, 0.1)
    # Both axes: Minor ticks every 0.02 for finer detail
    minor_ticks = np.arange(0, 3.02, 0.02)
    
    plt.gca().set_xticks(major_ticks)
    plt.gca().set_xticks(minor_ticks, minor=True)
    plt.gca().set_yticks(major_ticks)
    plt.gca().set_yticks(minor_ticks, minor=True)
    
    # Custom tick label formatting for both axes
    # Show 0.0, 1.0, 2.0, 3.0 in black, others in gray and smaller
    x_labels = []
    y_labels = []
    
    for tick in major_ticks:
        if tick in [0.0, 1.0, 2.0, 3.0]:
            x_labels.append(f'{tick:.1f}')
            y_labels.append(f'{tick:.1f}')
        else:
            x_labels.append(f'{tick:.1f}')
            y_labels.append(f'{tick:.1f}')
    
    plt.gca().set_xticklabels(x_labels)
    plt.gca().set_yticklabels(y_labels)
    
    # Color and size the tick labels
    for i, (tick, label) in enumerate(zip(major_ticks, plt.gca().get_xticklabels())):
        if tick in [0.0, 1.0, 2.0, 3.0]:
            label.set_color('black')
            label.set_fontsize(9)
            label.set_fontweight('bold')
        else:
            label.set_color('gray')
            label.set_fontsize(7)
            
    for i, (tick, label) in enumerate(zip(major_ticks, plt.gca().get_yticklabels())):
        if tick in [0.0, 1.0, 2.0, 3.0]:
            label.set_color('black')
            label.set_fontsize(9)
            label.set_fontweight('bold')
        else:
            label.set_color('gray')
            label.set_fontsize(7)
    
    # Set background color to white
    plt.gca().set_facecolor('white')
    plt.gcf().patch.set_facecolor('white')
    
    # Add axis lines through origin for reference
    plt.axhline(y=0, color='red', linestyle=':', alpha=0.6, linewidth=1)
    plt.axvline(x=0, color='red', linestyle=':', alpha=0.6, linewidth=1)
    
    # Set precise axis limits: Both X and Y from 0 to 3
    plt.xlim(0, 3.0)
    plt.ylim(0, 3.0)
    
    # Tight layout for better appearance
    plt.tight_layout()
    
    # Save the plot if requested
    if save_plot:
        plt.savefig('barnsley_fern_fractal.png', dpi=300, bbox_inches='tight',
                   facecolor='white', edgecolor='none')
        print("Fern fractal saved as 'barnsley_fern_fractal.png'")
    
    # Show the plot
    plt.show()

def print_fractal_info(x, y):
    """Print information about the generated fractal."""
    print(f"\n{'='*55}")
    print("SMALL BARNSLEY FERN - 0 TO 3 COORDINATE SYSTEM (BOTH AXES)")
    print(f"{'='*55}")
    print(f"Points generated: {len(x):,}")
    print(f"Original size - Width: {x.max() - x.min():.2f}, Height: {y.max() - y.min():.2f}")
    print(f"Small leaf size - Width: {(x.max() - x.min()) * 0.15:.2f}, Height: {(y.max() - y.min()) * 0.15:.2f}")
    print(f"Both axes range: 0.0 to 3.0 with 0.1 increments (31 major ticks)")
    print(f"Special formatting: 0.0, 1.0, 2.0, 3.0 in black bold; others gray small")
    print(f"Centered around X = 1.5, No rotation applied")
    print(f"{'='*55}\n")

def main():
    """Main function to generate and visualize the Barnsley Fern."""
    print("Generating Small Barnsley Fern in 0-3 Coordinate System (Both Axes)...")
    
    # Generate the fern with 25,000 points for good detail
    num_points = 25000
    print(f"Computing {num_points:,} points using modified IFS...")
    
    x, y = barnsley_fern(num_points)
    
    # Print analysis
    print_fractal_info(x, y)
    
    # Visualize the fern
    print("Creating small leaf in 0-3 coordinate system for both X and Y axes...")
    visualize_fern(x, y, save_plot=True)
    
    print("\nSmall Barnsley Fern completed!")
    print("Both X and Y axes: 0.0 to 3.0 with special formatting")
    print("0.0, 1.0, 2.0, 3.0 in black bold; other values in gray small text")

if __name__ == "__main__":
    main()
