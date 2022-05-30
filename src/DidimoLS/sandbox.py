import os
import sys
import cv2
from segmentation import SegmentFace
from processor import ImageProcessor

sys.path.append(os.path.dirname(__file__))

def segment_lips(image_path):
    (cropped_face, processed_face) = ImageProcessor(image_path).run()
    cv2.imwrite('cropped.png', cropped_face)
    cv2.imwrite('processed.png', processed_face)
    SegmentFace(image_path, 'cropped.png', 'processed.png').run()
    for path in ['cropped.png', 'processed.png']:
        os.remove(path)
    pass


if __name__ == '__main__':
    image_path = "lol0.png"
    segment_lips(image_path)

