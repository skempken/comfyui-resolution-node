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
- `ASPECT_RATIOS`: Dictionary with 12 professional formats sorted by mathematical ratio (portrait to landscape)
- `INPUT_TYPES()`: Defines input schema (megapixels, format, round_to_64) with tooltips
- `calculate_resolution()`: Main calculation method using mathematical pixel distribution
- `round_to_multiple()`: Utility for rounding to AI-friendly dimensions (multiples of 64)
- Returns width, height, and info string showing computed resolution

### ComfyUI Integration (`__init__.py`)
- Maps internal class name to ComfyUI's node registry
- Provides display name "Resolution Calculator" for UI

## Development Notes

- No external dependencies beyond Python standard library (uses only `math` module)
- Calculations maintain precise aspect ratios while hitting target megapixel counts
- Formats include classic photography, print standards, medium format, and modern digital ratios
- Rounding to 64-pixel multiples is optional for AI model compatibility
- All inputs include explanatory tooltips for user guidance

## Git Workflow Reminder

**IMPORTANT**: Before any git commit, always check if documentation needs updates:
- Review `README.md` for user-facing changes (features, usage examples, installation)
- Review `CLAUDE.md` for development changes (API, architecture, parameters)
- Update both files if the code changes affect their accuracy

## Format Categories

- **Portrait formats** (ratio < 1.0): Mobile/Stories, Photography, Classic, Print Standard, Medium Format
- **Square format** (ratio = 1.0): Perfect 1:1 aspect ratio
- **Landscape formats** (ratio > 1.0): Medium Format, Print Standard, Classic, Photography, Widescreen, Cinematic