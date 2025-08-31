# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a ComfyUI custom node for calculating optimal image dimensions based on megapixels and aspect ratio requirements. The node integrates into ComfyUI's workflow system as "Resolution Calculator" in the `image/resolution` category.

## Architecture

- **`__init__.py`**: ComfyUI plugin registration - defines `NODE_CLASS_MAPPINGS` and `NODE_DISPLAY_NAME_MAPPINGS`
- **`resolution_node.py`**: Core `ResolutionNode` class implementing the calculation logic
- **Node Structure**: Follows ComfyUI's node pattern with `INPUT_TYPES`, `RETURN_TYPES`, and execution function

## Key Components

### ResolutionNode Class (`resolution_node.py`)
- `ASPECT_RATIOS`: Dictionary mapping ratio strings to (width, height) tuples
- `INPUT_TYPES()`: Defines input schema (megapixels, aspect_ratio, orientation, round_to_64)
- `calculate_resolution()`: Main calculation method using mathematical pixel distribution
- `round_to_multiple()`: Utility for rounding to AI-friendly dimensions (multiples of 64)

### ComfyUI Integration (`__init__.py`)
- Maps internal class name to ComfyUI's node registry
- Provides display name "Resolution Calculator" for UI

## Development Notes

- No external dependencies beyond Python standard library (uses only `math` module)
- Calculations maintain precise aspect ratios while hitting target megapixel counts
- Portrait/landscape orientation is handled by swapping width/height after calculation
- Rounding to 64-pixel multiples is optional for AI model compatibility