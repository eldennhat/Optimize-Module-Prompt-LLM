def extract_key_features(prompt: str) -> list[str]:
    #Trích xuất các đặc điểm chính trong prompt đầu vào.(tạm thời hardcore đơn giản, nâng cấp sau bằng NLP)

    features = []

    if "chó" in prompt:
        features.append("chó")
    if "tai màu vàng" in prompt or "tai vàng" in prompt:
        features.append("đôi tai màu vàng")
    if "lông" in prompt:
        features.append("bộ lông đẹp")

    return features if features else ["đối tượng không rõ"]