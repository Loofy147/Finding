import unittest
from tgi.mind import TopologicalGeneralIntelligence

class TestGrounding(unittest.TestCase):
    def test_grounding_determinism(self):
        tgi = TopologicalGeneralIntelligence(3, 3)
        query = "Logical Truth"
        coord1 = tgi.grounding.ground_to_manifold(query, 3, 3)
        coord2 = tgi.grounding.ground_to_manifold(query, 3, 3)
        self.assertEqual(coord1, coord2)
        self.assertEqual(len(coord1), 3)

    def test_ground_and_process(self):
        tgi = TopologicalGeneralIntelligence(3, 3)
        query = "Socrates is mortal"
        res = tgi.ground_and_process(query)
        self.assertEqual(res['report']['status'], "ABSOLUTE_TRUTH")
        # Check that it got mapped
        self.assertIsNotNone(tgi.mapper.get_coord("Socrates"))

    def test_sentiment_logic(self):
        tgi = TopologicalGeneralIntelligence(3, 3)
        self.assertEqual(tgi.grounding.analyze_sentiment_logic("This is true"), "HARMONY")
        self.assertEqual(tgi.grounding.analyze_sentiment_logic("This is false"), "CONTRADICTION")

if __name__ == "__main__":
    unittest.main()
