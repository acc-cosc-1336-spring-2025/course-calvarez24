import unittest

from src.homework.h_strings.strings import get_hamming_distance , get_dna_complement

class TestStrings(unittest.TestCase):
    def test_get_hamming_distance(self):
        self.assertEqual(get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7)

    def test_get_dna_complement(self):
        self.assertEqual(get_dna_complement("AAAACCCGGT"), ("ACCGGGTTTT"))
