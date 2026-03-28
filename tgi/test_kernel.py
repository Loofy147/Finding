import unittest
from tgi.kernel import TGICognitiveKernel

class TestTGIKernel(unittest.TestCase):
    def test_parity_evaluator(self):
        # Even m, Even k -> Valid
        k1 = TGICognitiveKernel(4, 4)
        valid, _ = k1.core_1_parity_truth_evaluator()
        self.assertTrue(valid)

        # Even m, Odd k -> Invalid
        k2 = TGICognitiveKernel(3, 4)
        valid, _ = k2.core_1_parity_truth_evaluator()
        self.assertFalse(valid)

        # Odd m, any k -> Valid
        k3 = TGICognitiveKernel(3, 3)
        valid, _ = k3.core_1_parity_truth_evaluator()
        self.assertTrue(valid)

        k4 = TGICognitiveKernel(2, 3)
        valid, _ = k4.core_1_parity_truth_evaluator()
        self.assertTrue(valid)

    def test_solution_density(self):
        # m=3: phi(3)=2. N_b = 3^(3-1) * 2 = 9 * 2 = 18
        k = TGICognitiveKernel(3, 3)
        n_b, _ = k.core_2_axiom_quotient_projector()
        self.assertEqual(n_b, 18)

        # m=4: phi(4)=2. N_b = 4^(4-1) * 2 = 64 * 2 = 128
        k2 = TGICognitiveKernel(4, 4)
        n_b2, _ = k2.core_2_axiom_quotient_projector()
        self.assertEqual(n_b2, 128)

    def test_synapse_latency(self):
        k = TGICognitiveKernel(3, 3)
        _, b_vecs = k.core_2_axiom_quotient_projector()
        latency, end_state = k.core_3_spike_deduction_synapse(b_vecs)
        self.assertLess(latency, 0.1)
        self.assertEqual(len(end_state), 3)

if __name__ == "__main__":
    unittest.main()
