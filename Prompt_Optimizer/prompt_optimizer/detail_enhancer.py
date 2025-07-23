from .prompt_strategy import PromptStrategy
from .optimized_prompt import OptimizedPrompt

class DetailEnhancer(PromptStrategy):
    def optimize(self, prompt: str) -> OptimizedPrompt:
        enhanced = prompt + ", với chi tiết rõ ràng và ngữ cảnh cụ thể"
        return OptimizedPrompt(
            original_prompt=prompt,
            optimized_prompt=enhanced,
            added_details=["chi tiết rõ ràng", "ngữ cảnh cụ thể"]
        )
