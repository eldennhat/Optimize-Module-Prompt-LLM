from .prompt_strategy import PromptStrategy
from .optimized_prompt import OptimizedPrompt

class FeaturePreserver(PromptStrategy):
    def optimize(self, prompt: str) -> OptimizedPrompt:
        features = [word for word in prompt.split() if "màu" in word or "đặc điểm" in word]
        return OptimizedPrompt(
            original_prompt=prompt,
            optimized_prompt=prompt,
            preserved_features=features
        )
