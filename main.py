
import numpy as np
import cv2
import os, io
# from draw_vertice import drawVertices
from google.cloud import vision
import pandas as pd

def detect_logos(path):
    """Detects logos in the file."""
    
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.logo_detection(image=image)
    print("response", response)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        print(logo.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


cap = cv2.VideoCapture('sports_footage_small.mp4')

img_path = 'lays_logo.jpg'
lays_logo = cv2.imread(img_path, -1)


detect_logos(img_path)
# if (cap.isOpened()== False):
#     print("Error opening video stream or file")
    
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         cv2.imshow('Frame',frame)
        
#         # if frame_c = 3, means RGB
#         frame_h, frame_w, frame_c = frame.shape
#         print(frame.shape)
        
#         overlay = np.zeroes((frame_h, frame_w, 4), dtype='uint8')
        
        
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break
#     else:
#         break
        
# cap.release()
# cv2.destroyAllWindows()

