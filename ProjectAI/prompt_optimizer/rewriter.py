def rewrite_prompt(key_features: list) -> str:
    #Viết lại prompt với các đặc điểm rõ ràng, súc tích

    description = ", ".join(key_features)
    return f"Tạo hình ảnh một chú {description}."

