from .prompt_strategy import PromptStrategy
from .optimized_prompt import OptimizedPrompt

class OptimizePromptModule:
    def __init__(self, strategy: PromptStrategy = None):
        self.strategy = strategy

    def setStrategy(self, strategy: PromptStrategy):
        self.strategy = strategy

    def optimize(self, prompt: str) -> OptimizedPrompt:
        if not self.strategy:
            raise ValueError("No strategy set.")
        return self.strategy.optimize(prompt)
