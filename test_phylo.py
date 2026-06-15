import unittest
import numpy as np
from phylo_pipeline import jc69_distance, k2p_distance, compute_alignment_counts

class TestPhyloModels(unittest.TestCase):
    
    def test_jc69_zero_diff(self):
        """JC69 distance should be 0 when there are no differences."""
        self.assertEqual(jc69_distance(0.0), 0.0)
        
    def test_jc69_standard_val(self):
        """Test JC69 distance with a typical proportion of differences."""
        # p = 0.1 -> d = -0.75 * ln(1 - 4/3 * 0.1) approx 0.1072958
        d = jc69_distance(0.1)
        self.assertAlmostEqual(d, 0.1072958, places=6)
        
    def test_jc69_infinite_limit(self):
        """JC69 distance should return infinity when base differences are >= 0.75."""
        self.assertEqual(jc69_distance(0.75), np.inf)
        self.assertEqual(jc69_distance(0.80), np.inf)

    def test_k2p_zero_diff(self):
        """K2P distance should be 0 when differences are 0."""
        self.assertEqual(k2p_distance(0.0, 0.0), 0.0)

    def test_k2p_standard_val(self):
        """Test K2P distance with typical transition/transversion counts."""
        # p = 0.05, q = 0.02 -> d = -0.5 * ln(1 - 2*0.05 - 0.02) - 0.25 * ln(1 - 2*0.02)
        # = -0.5 * ln(0.88) - 0.25 * ln(0.96) approx 0.07412
        d = k2p_distance(0.05, 0.02)
        self.assertAlmostEqual(d, 0.0741219, places=6)

    def test_k2p_infinite_limit(self):
        """K2P distance should return infinity for mathematically invalid values."""
        self.assertEqual(k2p_distance(0.4, 0.3), np.inf)  # 1 - 2*0.4 - 0.3 = -0.1 (<= 0)
        self.assertEqual(k2p_distance(0.1, 0.6), np.inf)  # 1 - 2*0.6 = -0.2 (<= 0)

    def test_alignment_counts(self):
        """Test alignment classification for matches, transitions, transversions, and gaps."""
        # Purines: A, G; Pyrimidines: C, T
        # Col 1: A / A -> Match
        # Col 2: A / G -> Transition (Purines)
        # Col 3: C / T -> Transition (Pyrimidines)
        # Col 4: A / C -> Transversion (Purine/Pyrim)
        # Col 5: - / T -> Gap (Ignored in comparison sites)
        aligned_a = "AACAG-"
        aligned_b = "AGTCTT"
        
        counts = compute_alignment_counts(aligned_a, aligned_b)
        
        # Total sites without gaps should be 5
        self.assertEqual(counts["n_sites"], 5)
        # Matches: A-A (col 1), G-G (col 5) -> 2 matches
        # Transitions: A-G (col 2), C-T (col 4) -> 2 transitions
        # Transversions: A-C (col 3) -> 1 transversion
        self.assertEqual(counts["n_P"], 2)
        self.assertEqual(counts["n_Q"], 1)
        self.assertEqual(counts["p"], 2/5)
        self.assertEqual(counts["q"], 1/5)

if __name__ == "__main__":
    unittest.main()
