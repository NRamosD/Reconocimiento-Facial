from asyncore import read
from importlib.resources import path
import cv2
import os

import unittest
from reconocimiento.servidorReconocimiento import getImagePaths

class TestReconocimientoFacial(unittest.TestCase):

    def test_Reconocimiento(self):
        path = "C:\\Users\\jhony\\Desktop\\Proyectos\\Reconocimiento-Facial-1\\reconocimiento\\img\\Yo_mismo"

        self.assertEqual("C:\\Users\\jhony\\Desktop\\Proyectos\\Reconocimiento-Facial-1\\reconocimiento\\img\\" + getImagePaths()[0], path)

    def test_no_path(self):
        path = "C:\\Users\\jhony\\Desktop\\Proyectos\\Reconocimiento-Facial-1\\reconocimiento\\img"

        self.assertEqual("C:\\Users\\jhony\\Desktop\\Proyectos\\Reconocimiento-Facial-1\\reconocimiento\\img\\" + getImagePaths()[0], path)

    def test_n_3():
        dato = os.path(__file__)
        path = os.path.join(dato,'img')
        print(bool(path))
    
    def test_4_():
        path = None
        print('NO PATH')
    

if __name__ == '__main__':
    unittest.main()