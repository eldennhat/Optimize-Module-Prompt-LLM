from typing import List

class OptimizedPrompt:
    def __init__(self, original_prompt: str, optimized_prompt: str,
                 length_reduced: bool = False, preserved_features: List[str] = None,
                 added_details: List[str] = None):
        self.originalPrompt = original_prompt
        self.optimizedPrompt = optimized_prompt
        self.lengthReduced = length_reduced
        self.preservedFeatures = preserved_features or []
        self.addedDetails = added_details or []

    def preview(self):
        print("Original:", self.originalPrompt)
        print("Optimized:", self.optimizedPrompt)
        print("Length reduced:", self.lengthReduced)
        print("Preserved features:", self.preservedFeatures)
        print("Added details:", self.addedDetails)
