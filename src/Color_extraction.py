import os
import cv2
import numpy as np
from moviepy.editor import *
from HUE import HUE

FILENAME  = input("処理するファイル名を入力：")
HUE_VALUE = input("""
残したい色を選択
    - RED, 
    - ORANGE,
    - YELLOW,
    - GREEN,
    - EMERALD,
    - CYAN,
    - BLUE,
    - PURPLE,
    - MAGENTA
""").upper()

def color_extraction_video(input_file: str, hue) -> None:
    OUTPUT_FILE_NAME: str = f"../{input_file}_{hue}_colorextraction_video.mp4"
    
    CAP = cv2.VideoCapture(input_file)
    
    ORIGINAL_FPS   : int = CAP.get(cv2.CAP_PROP_FPS)
    ORIGINAL_WIDTH : int = int(CAP.get(cv2.CAP_PROP_FRAME_WIDTH))
    ORIGINAL_HEIGHT: int = int(CAP.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    FOURCC = cv2.VideoWriter_fourcc(*"mp4v")
    output = cv2.VideoWriter(
        OUTPUT_FILE_NAME,
        FOURCC,
        ORIGINAL_FPS,
        (
            ORIGINAL_WIDTH,
            ORIGINAL_HEIGHT
        )
    )

    while True:
        ret, frame = CAP.read()
        
        if not ret:
            break
        
        HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        TARGET_HUE: int = HUE.value(hue)
        upper_hue : int = TARGET_HUE + 10
        lower_hue : int = TARGET_HUE - 10
        mask = None
        
        mask_lower  = np.array([lower_hue, 50, 50])
        mask_upper  = np.array([upper_hue, 255, 255])
        mask        = cv2.inRange(HSV, mask_lower, mask_upper)
        
        gray_image  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_mask   = cv2.bitwise_not(mask)
        gray_masked = cv2.bitwise_and(gray_image, gray_image, mask=gray_mask)
        
        color_image = cv2.bitwise_and(frame, frame, mask=mask)
        result      = cv2.bitwise_or(color_image, cv2.cvtColor(gray_masked, cv2.COLOR_GRAY2BGR))
        
        output.write(result)
        
    CAP.release()
    output.release()

color_extraction_video("../input.mp4", HUE_VALUE)