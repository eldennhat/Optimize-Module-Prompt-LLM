# Optimize Prompt Module

**Mục tiêu**: Tối ưu prompt đầu vào cho AI sao cho:
- Ngắn gọn
- Giữ được đặc điểm quan trọng
- Có thể bổ sung chi tiết nếu cần

## Cấu trúc Module

Module bao gồm:
- `OptimizePromptModule`: lớp chính
- `PromptStrategy`: interface
- `Shortener`: rút gọn prompt
- `FeaturePreserver`: giữ đặc điểm
- `DetailEnhancer`: bổ sung chi tiết
- `OptimizedPrompt`: chứa kết quả

## Cách dùng

```bash
python main.py
