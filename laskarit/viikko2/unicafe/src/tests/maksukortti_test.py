import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000) 

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(200)

        self.assertEqual(self.maksukortti.saldo, 1200)  

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(200)

        self.assertEqual(self.maksukortti.saldo, 800)  

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1200)

        self.assertEqual(self.maksukortti.saldo, 1000)  

    def test_palautus_oikein_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1200), False)  

    def test_palautus_oikein_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1000), True)  

    def test_str_on_oikein(self):
        self.assertEqual(str(self.maksukortti), 'Kortilla on rahaa 10.00 euroa')
