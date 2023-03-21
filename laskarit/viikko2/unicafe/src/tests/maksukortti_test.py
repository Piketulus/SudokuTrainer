import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
# tee testit tänne
#-Kortin saldo alussa oikein
#-Rahan lataaminen kasvattaa saldoa oikein
#-Rahan ottaminen toimii:
#-Saldo vähenee oikein, jos rahaa on tarpeeksi
#-Saldo ei muutu, jos rahaa ei ole tarpeeksi
#-Metodi palauttaa True, jos rahat riittivät ja muuten False

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")