import unittest
from prompt_optimizer.cleaner import clean_prompt
from prompt_optimizer.analyzer import extract_key_features
from prompt_optimizer.rewriter import rewrite_prompt

class TestPromptOptimizer(unittest.TestCase):

    def test_clean_prompt(self):
        dirty = "  HÃY tạo Tôi CON chó có TAI màu VÀNG!! "
        clean = clean_prompt(dirty)
        self.assertEqual(clean, "hãy tạo tôi con chó có tai màu vàng")

    def test_extract_features(self):
        prompt = "hãy tạo tôi con chó có tai màu vàng"
        features = extract_key_features(prompt)
        self.assertIn("chó", features)
        self.assertIn("đôi tai màu vàng", features)

    def test_rewrite_prompt(self):
        features = ["chó", "đôi tai màu vàng"]
        rewritten = rewrite_prompt(features)
        self.assertEqual(rewritten, "Tạo hình ảnh một chú chó, đôi tai màu vàng.")

if __name__ == '__main__':
    unittest.main()
