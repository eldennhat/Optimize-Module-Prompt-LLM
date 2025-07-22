# Optimize-Module-Prompt-LLM

A Python module that optimizes input prompts for AI models to generate more accurate and specific single-result outputs.

## Features
- Clean unnecessary words
- Extract key visual attributes
- Rewrite prompt for clarity and image generation

## Usage
```python
from prompt_optimizer import optimize_prompt

prompt = "Hãy tạo tôi con chó có tai màu vàng"
optimized = optimize_prompt(prompt)
print(optimized)

