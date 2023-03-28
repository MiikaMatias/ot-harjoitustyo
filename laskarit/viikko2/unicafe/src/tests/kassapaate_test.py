import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(410)

    def test_setup_olemassa(self):
        self.assertNotEqual(self.kassapaate,None)

    def test_setup_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_setup_maukkaat_myyty_nolla(self):
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_setup_edullisia_myyty_nolla(self):
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_edullisia_myyty_oikein_kortti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_maukkaat_myyty_oikein_kortti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_edullisia_myyty_oikein_kortti_kahdesti_epaonnistuminen(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_maukkaat_myyty_oikein_kortti_kahdesti_epaonnistuminen(self):
        maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_syo_edullisesti_kortilla_raha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),True)

    def test_syo_maukkaasti_kortilla_raha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),True)

    def test_syo_edullisesti_kortilla_raha_vaarin(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),False)

    def test_syo_maukkaasti_kortilla_raha_vaarin(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),False)

    def test_kassa_ei_muutu_kortilla_edullisesti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassa_ei_muutu_kortilla_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_raha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(260),20)

    def test_syo_maukkaasti_kateisella_raha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410),10)

    def test_syo_edullisesti_kateisella_raha_vaarin(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200),200)

    def test_syo_maukkaasti_kateisella_raha_vaarin(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200),200)

    def test_kassapaate_rahanlataus(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,50)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000-50)
        self.assertEqual(self.maksukortti.saldo,410+50)

    def test_kassapaate_rahanlataus_negatiivinen(self):
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-40),None)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.maksukortti.saldo,410)
