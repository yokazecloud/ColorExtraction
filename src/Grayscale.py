import cv2

def grayscale_video(input_file: str) -> None:
    
    OUTPUT_FILE_NAME: str = f"{input_file}_output.mp4"
    
    CAP = cv2.VideoCapture(input_file)
    
    ORIGINAL_FPS   : int = CAP.get(cv2.CAP_PROP_FPS)
    ORIGINAL_WIDTH : int = CAP.get(cv2.CAP_PROP_FRAME_WIDTH)
    ORIGINAL_HEIGHT: int = CAP.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
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
        
        gray_image = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        output.write(gray_image)
        
    CAP.release()
    output.release()