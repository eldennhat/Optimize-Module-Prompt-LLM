def clean_prompt(prompt: str) -> str:
    """
    Làm sạch prompt: viết thường, xóa khoảng trắng thừa, ký tự đặc biệt.
    """
    import re
    prompt = prompt.strip().lower()
    prompt = re.sub(r"[^\w\sàáảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵ]", "", prompt)
    prompt = re.sub(r"\s+", " ", prompt)
    return prompt
