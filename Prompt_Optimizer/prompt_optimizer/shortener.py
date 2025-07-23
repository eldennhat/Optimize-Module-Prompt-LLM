from .prompt_strategy import PromptStrategy
from .optimized_prompt import OptimizedPrompt

class Shortener(PromptStrategy):
    def __init__(self, max_len: int = 20):
        self.maxLen = max_len

    def optimize(self, prompt: str) -> OptimizedPrompt:
        words = prompt.split()
        short_prompt = " ".join(words[:self.maxLen])
        return OptimizedPrompt(
            original_prompt=prompt,
            optimized_prompt=short_prompt,
            length_reduced=True
        )
