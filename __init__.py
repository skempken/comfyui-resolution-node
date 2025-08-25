from .resolution_node import ResolutionNode

NODE_CLASS_MAPPINGS = {
    "ResolutionNode": ResolutionNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionNode": "Resolution Calculator",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']