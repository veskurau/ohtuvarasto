import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_laitetaan_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_lisaa_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_konstruktorin_negatiiviset_arvot(self):
        self.varasto_toinen = Varasto(-1, -1)
        #self.varasto_toinen
        self.assertEqual(self.varasto_toinen.tilavuus, 0)
        self.assertEqual(self.varasto_toinen.saldo, 0)
        self.varasto_toinen = Varasto(10, 11)
        self.assertEqual(self.varasto_toinen.saldo, self.varasto_toinen.tilavuus)

    def test_ota_varastosta_liikaa_tai_negatiivinen_maara(self):
        self.varasto.ota_varastosta(-1)
        self.assertEqual(self.varasto.saldo, 0)

        self.varasto.ota_varastosta(10)
        self.assertEqual(self.varasto.saldo, 0)

    def test_str_testaus(self):
        tulostus = str(self.varasto)
        self.assertEqual(tulostus, "saldo = 0, vielä tilaa 10")
