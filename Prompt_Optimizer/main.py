from prompt_optimizer.optimize_prompt_module import OptimizePromptModule
from prompt_optimizer.shortener import Shortener
from prompt_optimizer.feature_preserver import FeaturePreserver
from prompt_optimizer.detail_enhancer import DetailEnhancer

if __name__ == "__main__":
    prompt = "Hãy tạo một hình ảnh chú chó có tai màu vàng và lông mềm mượt"

    module = OptimizePromptModule()

    # Shortening
    module.setStrategy(Shortener(max_len=10))
    result1 = module.optimize(prompt)
    result1.preview()

    print("="*40)

    # Feature Preserving
    module.setStrategy(FeaturePreserver())
    result2 = module.optimize(prompt)
    result2.preview()

    print("="*40)

    # Detail Enhancing
    module.setStrategy(DetailEnhancer())
    result3 = module.optimize(prompt)
    result3.preview()
