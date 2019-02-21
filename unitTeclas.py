import unittest
import pygame
import pygame.key
from pantalla import *


class KeyModuleTest(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_import(self):
        import pygame.key



    def test_get_pressed(self):
        states = pygame.key.get_pressed()
        self.assertEqual(states[pygame.K_RIGHT], 0)

    def test_name(self):
        self.assertEqual(pygame.key.name(pygame.K_RETURN), "return")
        self.assertEqual(pygame.key.name(pygame.K_0), "0")
        self.assertEqual(pygame.key.name(pygame.K_SPACE), "space")

   # def test_set_and_get_mods(self):
    #    pygame.key.set_mods(pygame.KMOD_CTRL)
     #   self.assertEqual(pygame.key.get_mods(), pygame.KMOD_CTRL)

        pygame.key.set_mods(pygame.KMOD_ALT)
        self.assertEqual(pygame.key.get_mods(), pygame.KMOD_ALT)
        pygame.key.set_mods(pygame.KMOD_CTRL | pygame.KMOD_ALT)
        self.assertEqual(pygame.key.get_mods(), pygame.KMOD_CTRL | pygame.KMOD_ALT)

    def test_set_and_get_repeat(self):
        self.assertEqual(pygame.key.get_repeat(), (0, 0))

        pygame.key.set_repeat(10, 15)
        self.assertEqual(pygame.key.get_repeat(), (10, 15))

        pygame.key.set_repeat()
        self.assertEqual(pygame.key.get_repeat(), (0, 0))


if __name__ == '__main__':
    unittest.main()