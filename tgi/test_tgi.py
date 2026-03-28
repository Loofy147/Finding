import unittest
from tgi.mind import TopologicalGeneralIntelligence

class TestTGI(unittest.TestCase):
    def test_symbolic_mapping(self):
        tgi = TopologicalGeneralIntelligence(3, 3)
        tgi.mapper.map_concept("Truth", (0, 0, 0))
        self.assertEqual(tgi.mapper.get_coord("Truth"), (0, 0, 0))
        self.assertEqual(tgi.mapper.get_concept((0, 0, 0)), "Truth")

    def test_parity_obstruction(self):
        # m=4 (even), k=3 (odd) -> Obstructed
        tgi = TopologicalGeneralIntelligence(4, 3)
        res = tgi.process_hypothesis((0, 0, 0), verbose=False)
        self.assertEqual(res['report']['status'], "PARADOX_DETECTED")
        self.assertFalse(res['report']['valid'])

    def test_hamiltonian_truth(self):
        # m=3 (odd), k=2 -> Harmonious
        tgi = TopologicalGeneralIntelligence(3, 2)
        res = tgi.process_hypothesis((0, 0), verbose=False)
        self.assertEqual(res['report']['status'], "ABSOLUTE_TRUTH")
        self.assertTrue(res['report']['valid'])
        self.assertEqual(len(res['chain']), 3**2 + 1)

    def test_hyper_parity_harmony(self):
        # m=4 (even), k=2 (even) -> Harmonious
        tgi = TopologicalGeneralIntelligence(4, 2)
        res = tgi.process_hypothesis((0, 0), verbose=False)
        self.assertEqual(res['report']['status'], "ABSOLUTE_TRUTH")
        self.assertTrue(res['report']['valid'])
        self.assertEqual(len(res['chain']), 4**2 + 1)

if __name__ == "__main__":
    unittest.main()
