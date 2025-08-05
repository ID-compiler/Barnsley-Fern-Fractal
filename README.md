#  Barnsley Fern Fractal - Mathematical Leaf Visualization

A Python implementation of the famous Barnsley Fern fractal using Iterated Function Systems (IFS) with custom matrix transformations and professional coordinate visualization.

##  Overview

This project generates a mathematically elegant leaf structure that closely resembles natural fern leaves using only four simple transformation matrices. The Barnsley Fern demonstrates how complex, organic-looking patterns can emerge from simple mathematical rules.

##  Features

- **25,000+ high-resolution points** for detailed fractal generation
- **Custom coordinate system** with 0-3 range and 0.1 precision
- **Professional visualization** with major/minor grid lines
- **Custom tick formatting** (0.0, 1.0, 2.0, 3.0 in bold black; others in gray)
- **Modified transformation matrices** for enhanced visual appeal
- **High-DPI export** (300 DPI PNG output)

##  Technical Implementation

### Core Algorithm
The fern is generated using four probabilistic transformations:
1. **Stem formation** (1% probability)
2. **Main leaflet structure** (85% probability) 
3. **Left leaflets** (7% probability)
4. **Right leaflets** (7% probability)

### Matrix Transformation Format
Each transformation follows the standard affine transformation:
```
x_new = a*x + b*y + e
y_new = c*x + d*y + f
```

##  Custom Matrix Modifications

I enhanced the original Barnsley Fern by modifying key transformation parameters to create a more visually appealing and realistic fern structure:

###  Transformation 1: Stem (1% probability)
- **Vertical scaling 'd'**: 0.16 → **0.25** (+56% increase)
- **All others (a,b,c,e,f)**: Remained **zero**
- **Result**: Taller, more prominent central stem

###  Transformation 2: Main Leaflet (85% probability)
- **Curvature 'b'**: 0.02 → **0.08** (+300% increase)
- **Curvature 'c'**: -0.02 → **-0.08** (+300% increase)
- **Scaling 'a' & 'd'**: 0.87 → **0.80** (-8% adjustment)
- **Vertical shift 'f'**: 1.6 → **1.8** (+12.5% increase)
- **Result**: More graceful curvature and enhanced structure in main leaf

###  Transformation 3: Left Leaflet (7% probability)
- **a**: 0.20 → **0.30** (+50% increase)
- **b**: -0.26 → **-0.35** (+35% increase)
- **c**: 0.23 → **0.35** (+52% increase)
- **d**: 0.22 → **0.30** (+36% increase)
- **f**: 1.6 → **1.8** (+12.5% increase)
- **Result**: Sharper and more prominent left leaflets

###  Transformation 4: Right Leaflet (7% probability)
- **a**: -0.15 → **-0.25** (+67% increase)
- **b**: 0.28 → **0.35** (+25% increase)
- **c**: 0.26 → **0.35** (+35% increase)
- **d**: 0.24 → **0.30** (+25% increase)
- **f**: 0.44 → **0.6** (+36% increase)
- **Result**: Symmetrical right leaflets with enhanced curve

##  Getting Started

### Prerequisites
```bash
pip install numpy matplotlib
```

### Running the Code
```bash
python barnsley_fern.py
```

### Output
- **Console**: Detailed fractal analysis and generation statistics
- **Display**: Interactive matplotlib visualization
- **File**: High-resolution PNG saved as `barnsley_fern_fractal.png`

## Technical Specifications

| Feature | Specification |
|---------|---------------|
| **Points Generated** | 25,000 |
| **Coordinate System** | 0.0 to 3.0 (both axes) |
| **Grid Precision** | Major: 0.1, Minor: 0.02 |
| **Output Resolution** | 300 DPI |
| **Figure Size** | 8×6 inches |
| **File Format** | PNG with white background |

##  Visualization Features

- **Dual-level grid system** for precise coordinate reading
- **Custom tick formatting** with hierarchical text styling
- **Professional color scheme** (black leaf on white background)
- **No axis rotation** for natural upright orientation
- **Centered positioning** within coordinate space

`#ComputationalGeometry` `#IFS` `#NumPy` `#Matplotlib` `#STEM`

---

*"Mathematics is the language in which God has written the universe."* - Galileo Galilei

**Created with ❤️ and mathematical precision**
