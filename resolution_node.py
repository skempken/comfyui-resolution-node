import math

class ResolutionNode:
    ASPECT_RATIOS = {
        "1:1": (1, 1),
        "4:5": (4, 5),
        "3:4": (3, 4),
        "2:3": (2, 3),
        "4:3": (4, 3),
        "16:9": (16, 9),
        "21:9": (21, 9),
        "1.85:1": (185, 100),
        "2.35:1": (235, 100),
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
                    "display": "number"
                }),
                "aspect_ratio": (list(cls.ASPECT_RATIOS.keys()), {
                    "default": "16:9"
                }),
                "orientation": (["landscape", "portrait"], {
                    "default": "landscape"
                }),
                "round_to_64": ("BOOLEAN", {
                    "default": True
                }),
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "calculate_resolution"
    CATEGORY = "image/resolution"

    def calculate_resolution(self, megapixels, aspect_ratio, orientation, round_to_64):
        # Get aspect ratio values
        aspect_w, aspect_h = self.ASPECT_RATIOS[aspect_ratio]
        
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
        
        # Apply orientation
        if orientation == "portrait":
            width, height = height, width
        
        # Round to integers
        width = int(round(width))
        height = int(round(height))
        
        # Round to nearest multiple of 64 if requested
        if round_to_64:
            width = self.round_to_multiple(width, 64)
            height = self.round_to_multiple(height, 64)
        
        return (width, height)
    
    def round_to_multiple(self, value, multiple):
        return int(multiple * round(value / multiple))