# ComfyUI Resolution Calculator Node

A custom node for ComfyUI that calculates optimal image dimensions based on megapixels and aspect ratio requirements.

## Features

- **Megapixel Input**: Specify target resolution in megapixels (0.1 - 100.0 MP)
- **Aspect Ratio Selection**: Choose from common aspect ratios
- **Orientation Control**: Toggle between landscape and portrait modes
- **Smart Rounding**: Optional rounding to nearest multiple of 64 (AI-friendly)
- **Precise Calculations**: Maintains exact aspect ratios while hitting target megapixel count

## Supported Aspect Ratios

| Ratio | Description |
|-------|-------------|
| 1:1   | Square (social media) |
| 4:5   | Instagram portrait |
| 3:4   | Traditional photo |
| 2:3   | Classic photo format |
| 4:3   | Old TV/monitor standard |
| 16:9  | Widescreen standard |
| 21:9  | Ultra-wide/cinematic |
| 1.85:1| Cinema standard |
| 2.35:1| Cinema widescreen |

## Installation

1. Clone or download this repository into your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/skempken/comfyui-resolution-node.git comfyui-resolution-node
   ```

2. Restart ComfyUI

3. The "Resolution Calculator" node will appear in the `image/resolution` category

## Usage

1. Add the "Resolution Calculator" node to your workflow
2. Set your desired **megapixels** (e.g., 1.0 for ~1 million pixels)
3. Choose an **aspect ratio** from the dropdown
4. Select **orientation** (landscape or portrait)
5. Toggle **round_to_64** if you need AI-compatible dimensions
6. Connect the width/height outputs to your image generation nodes

## Node Inputs

- **megapixels** (float): Target resolution in megapixels (0.1 - 100.0)
- **aspect_ratio** (dropdown): Desired aspect ratio
- **orientation** (dropdown): "landscape" or "portrait"
- **round_to_64** (boolean): Round dimensions to nearest multiple of 64

## Node Outputs

- **width** (int): Calculated image width in pixels
- **height** (int): Calculated image height in pixels

## Examples

| Input | Output | Actual MP |
|-------|--------|-----------|
| 1.0 MP, 16:9 landscape, rounded | 1344×768 | 1.03 MP |
| 1.0 MP, 16:9 portrait, rounded | 768×1344 | 1.03 MP |
| 2.0 MP, 4:3 landscape, not rounded | 1633×1225 | 2.00 MP |
| 0.5 MP, 1:1 square, rounded | 704×704 | 0.50 MP |

## Why Round to 64?

Many AI image generation models work optimally with dimensions that are multiples of 64. This ensures:
- Better model performance
- Reduced artifacts
- Consistent results across different resolutions

## Development

This project is set up for PyCharm development with included `.idea` configuration files.

## License

MIT License - see LICENSE file for details.