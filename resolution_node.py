import math

class ResolutionNode:
    ASPECT_RATIOS = {
        "9:16 Mobile/Stories": (9, 16),
        "2:3 Photography Portrait": (2, 3),
        "3:4 Classic Portrait": (3, 4),
        "4:5 Print Standard Portrait": (4, 5),
        "6:7 Medium Format Portrait": (6, 7),
        "1:1 Square": (1, 1),
        "7:6 Medium Format Landscape": (7, 6),
        "5:4 Print Standard Landscape": (5, 4),
        "4:3 Classic Landscape": (4, 3),
        "3:2 Photography Landscape": (3, 2),
        "16:9 Widescreen": (16, 9),
        "21:9 Cinematic": (21, 9),
    }

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "megapixels": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.1,
                    "max": 100.0,
                    "step": 0.1,
                    "display": "number",
                    "tooltip": "Target resolution in megapixels (millions of pixels)"
                }),
                "format": (list(cls.ASPECT_RATIOS.keys()), {
                    "default": "3:2 Photography Landscape",
                    "tooltip": "Image aspect ratio format"
                }),
                "round_to_64": ("BOOLEAN", {
                    "default": True,
                    "tooltip": "Round dimensions to multiples of 64 for better AI model compatibility"
                }),
            },
        }

    RETURN_TYPES = ("INT", "INT", "STRING")
    RETURN_NAMES = ("width", "height", "info")
    FUNCTION = "calculate_resolution"
    CATEGORY = "image/resolution"

    def calculate_resolution(self, megapixels, format, round_to_64):
        # Get aspect ratio values
        aspect_w, aspect_h = self.ASPECT_RATIOS[format]
        
        # Calculate total pixels from megapixels
        total_pixels = megapixels * 1_000_000
        
        # Calculate aspect ratio as a decimal
        aspect_decimal = aspect_w / aspect_h
        
        # Calculate base width and height
        # total_pixels = width * height
        # aspect_decimal = width / height
        # So: width = aspect_decimal * height
        # total_pixels = aspect_decimal * height^2
        # height = sqrt(total_pixels / aspect_decimal)
        
        height = math.sqrt(total_pixels / aspect_decimal)
        width = aspect_decimal * height
        
        # Round to integers
        width = int(round(width))
        height = int(round(height))
        
        # Round to nearest multiple of 64 if requested
        if round_to_64:
            width = self.round_to_multiple(width, 64)
            height = self.round_to_multiple(height, 64)
        
        # Create info string
        info = f"{width} x {height}"
        
        return (width, height, info)
    
    def round_to_multiple(self, value, multiple):
        return int(multiple * round(value / multiple))