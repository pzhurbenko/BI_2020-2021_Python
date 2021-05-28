import unittest
from DNA_classes import *

class test_NucleoSeq(unittest.TestCase):

    def test_gc_content(self):
        dna1 = NucleoSeq('AGTCCCCT')
        dna2 = NucleoSeq('AgTcCCct')
        dna3 = NucleoSeq('TTTTTTT')
        self.assertEqual(dna1.gc_content(), 0.625)
        self.assertEqual(dna2.gc_content(), 0.625)
        self.assertEqual(dna3.gc_content(), 0)

    def test_next_letter(self):
        self.assertEqual(next(DNA('AGCT')), 'A')
        self.assertEqual(next(DNA('AGCT')), 'A')
        DNA_next = DNA('AGCT')
        self.assertEqual(next(DNA_next), 'A')
        self.assertEqual(next(DNA_next), 'G')
        self.assertEqual(next(DNA_next), 'C')
        self.assertEqual(next(DNA_next), 'T')

class test_DNA(unittest.TestCase):

    def test_contain_U(self):
        self.assertRaises(TypeError, DNA, 'ACGU')

    def test_contain_wrong_other_letters(self):
        self.assertRaises(TypeError, DNA, 'ACGR')

    def test_reverse_complement(self):
        dna1 = DNA('AGCT')
        dna2 = DNA('AGCtt')
        self.assertEqual(dna1.reverse_complement(), 'AGCT')
        self.assertNotEqual(dna1.reverse_complement(), 'agct')
        self.assertEqual(dna2.reverse_complement(), 'aaGCT')

    def test_transcribe(self):
        dna1 = DNA('AGTC')
        self.assertEqual(dna1.transcribe().seq, RNA('AGUC').seq)

class test_RNA(unittest.TestCase):

    def test_contain_wrong_other_letters(self):
        self.assertRaises(TypeError, RNA, 'ACGR')

    def test_RNA_reverse_complement(self):
        rna1 = RNA('AGUGCUAGC')
        rna2 = RNA('AGUGCUagc')
        self.assertEqual(rna1.reverse_complement(), 'GCUAGCACU')
        self.assertNotEqual(rna1.reverse_complement(), 'gcuagcacu')
        self.assertEqual(rna2.reverse_complement(), 'gcuAGCACU')
