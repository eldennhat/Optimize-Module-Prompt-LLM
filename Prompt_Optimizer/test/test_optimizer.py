
import unittest
from prompt_optimizer.shortener import Shortener
from prompt_optimizer.feature_preserver import FeaturePreserver
from prompt_optimizer.detail_enhancer import DetailEnhancer

class TestStrategies(unittest.TestCase):
    def test_shortener(self):
        s = Shortener(max_len=5)
        result = s.optimize("đây là một đoạn prompt rất dài và đầy đủ")
        self.assertTrue(result.lengthReduced)
        self.assertLessEqual(len(result.optimizedPrompt.split()), 5)

    def test_feature_preserver(self):
        f = FeaturePreserver()
        result = f.optimize("chú chó có đặc điểm là tai màu vàng")
        self.assertIn("màu", " ".join(result.preservedFeatures))

    def test_detail_enhancer(self):
        d = DetailEnhancer()
        result = d.optimize("một con mèo dễ thương")
        self.assertIn("chi tiết rõ ràng", result.addedDetails)

if __name__ == "__main__":
    unittest.main()
