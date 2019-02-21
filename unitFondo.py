import unittest
from pygame import *
from pantalla import *


class RectTypeTest(unittest.TestCase):
    def testConstructionXYWidthHeight(self):
        param=0
        login= Login(param)
        r = login.sprites["background"].image.get_rect()
        self.assertEqual(0, r.left)
        self.assertEqual(0, r.top)
        self.assertEqual(800, r.width)
        self.assertEqual(600, r.height)

    def testConstructionTopLeftSize(self):
        param=0
        escenario= ListaEscenarios(param)
        r = escenario.sprites["fondo"].image.get_rect()
        self.assertEqual(0, r.left)
        self.assertEqual(0, r.top)
        self.assertEqual(800, r.width)
        self.assertEqual(600, r.height)

    def testCalculatedAttributes(self):
        param=0
        escenario= ListaEscenarios(param)
        r = escenario.sprites["fondo"].image.get_rect()

        self.assertEqual(r.left + r.width, r.right)
        self.assertEqual(r.top + r.height, r.bottom)
        self.assertEqual((r.width, r.height), r.size)
        self.assertEqual((r.left, r.top), r.topleft)
        self.assertEqual((r.right, r.top), r.topright)
        self.assertEqual((r.left, r.bottom), r.bottomleft)
        self.assertEqual((r.right, r.bottom), r.bottomright)

        midx = r.left + r.width // 2
        midy = r.top + r.height // 2

        self.assertEqual(midx, r.centerx)
        self.assertEqual(midy, r.centery)
        self.assertEqual((r.centerx, r.centery), r.center)
        self.assertEqual((r.centerx, r.top), r.midtop)
        self.assertEqual((r.centerx, r.bottom), r.midbottom)
        self.assertEqual((r.left, r.centery), r.midleft)
        self.assertEqual((r.right, r.centery), r.midright)


    def test_left(self):
        """Changing the left attribute moves the rect and does not change
           the rect's width
        """
        param=0
        login= Login(param)
        r = login.sprites["background"].image.get_rect()
        new_left = 10

        r.left = new_left
        self.assertEqual(new_left, r.left)
        self.assertEqual(Rect(new_left, 0, 800, 600), r)

    def test_right(self):
        """Changing the right attribute moves the rect and does not change
           the rect's width
        """
        param=0
        escenario= ListaEscenarios(param)
        r = escenario.sprites["fondo"].image.get_rect()
        new_right = r.right + 20
        expected_left = r.left + 20
        old_width = r.width

        r.right = new_right
        self.assertEqual(new_right, r.right)
        self.assertEqual(expected_left, r.left)
        self.assertEqual(old_width, r.width)

    def test_top(self):
        """Changing the top attribute moves the rect and does not change
           the rect's width
        """
        param=0
        login= Login(param)
        r = login.sprites["background"].image.get_rect()
        new_top = 10

        r.top = new_top
        self.assertEqual(Rect(0, new_top, 800, 600), r)
        self.assertEqual(new_top, r.top)

    def test_bottom(self):
        """Changing the bottom attribute moves the rect and does not change
           the rect's height
        """
        param=0
        escenario= ListaEscenarios(param)
        r = escenario.sprites["fondo"].image.get_rect()
        new_bottom = r.bottom + 20
        expected_top = r.top + 20
        old_height = r.height

        r.bottom = new_bottom
        self.assertEqual(new_bottom, r.bottom)
        self.assertEqual(expected_top, r.top)
        self.assertEqual(old_height, r.height)



if __name__ == '__main__':
    unittest.main()