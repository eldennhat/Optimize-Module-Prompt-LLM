def capitalize_first(text: str) -> str:
    #Viết hoa chữ cái đầu tiên của chuỗi (dùng nếu cần)
    if not text:
        return ""
    return text[0].upper() + text[1:]