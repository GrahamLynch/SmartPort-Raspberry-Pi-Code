import unittest
import sys


class SmartPortOpenCVTest(unittest.TestCase):
  

    def test_import(self):
        import cv2

    def test_video_capture(self):
        import cv2
        cap = cv2.VideoCapture(0)
        self.assertTrue(cap.isOpened())