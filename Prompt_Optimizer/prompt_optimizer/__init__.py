from abc import ABC, abstractmethod
from .optimized_prompt import OptimizedPrompt

class PromptStrategy(ABC):
    @abstractmethod
    def optimize(self, prompt: str) -> OptimizedPrompt:
        pass
