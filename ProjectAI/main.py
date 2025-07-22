from prompt_optimizer.cleaner import clean_prompt
from prompt_optimizer.analyzer import extract_key_features
from prompt_optimizer.rewriter import rewrite_prompt

def optimize(prompt: str) -> str:
    cleaned = clean_prompt(prompt)
    features = extract_key_features(cleaned)
    rewritten = rewrite_prompt(features)
    return rewritten

if __name__ == "__main__":
    raw_prompt = "Hãy tạo tôi con chó có tai màu vàng"
    print("📝 Prompt gốc: ", raw_prompt)
    print("✨ Prompt tối ưu:", optimize(raw_prompt))
